# ----------------------------------------------------------------------------------------
#  PASO3: Enviar Email Diario   
#  Autor: SteveCarpio-2025
# ----------------------------------------------------------------------------------------

import cfg.MAILING_variables as sTv
from   cfg.MAILING_library import *

# ----------------------------------------------------------------------------------------
#                                  FUNCIONES
# ----------------------------------------------------------------------------------------

def Mandar_Email_Diario(destinatarios_to, destinatarios_cc, asunto, cuerpo, df, var_Fecha):
    registros = len(df)
    print(f"Se han recibido: {registros} registros. ")
    if registros >= 0:
        # Configuración del servidor SMTP (Zimbra)
        smtp_server = 'zimbra.tda-sgft.com'
        smtp_port = 25  
        correo_remitente = 'publicacionesbolsasmx@tda-sgft.com'  

        # Crear el mensaje
        mensaje = MIMEMultipart()
        mensaje['From'] = correo_remitente
        mensaje['To'] = ", ".join(destinatarios_to)
        mensaje['Cc'] = ", ".join(destinatarios_cc)
        mensaje['Subject'] = asunto
        
        # Combinar destinatarios principales y en copia
        todos_destinatarios = destinatarios_to + destinatarios_cc 

        # Eliminar los /r y /n, reemplazarlos por etiquetas html br
        df['DETALLE_DEL_EVENTO'] = df['DETALLE_DEL_EVENTO'].apply(lambda x: str(x).replace('\r', '').replace('\n', '<br>'))

        # Convertir el DataFrame a HTML, scape=False para que tenga en cuenta los BR
        tabla_html = df.to_html(index=True, escape=False)  # con el índice

        # Cuerpo del correo usando HTML y CSS
        cuerpo_html = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f9;  
                    color: #333;
                }}
                .content {{
                    background-color: #ffffff;  
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                }}
                h1 {{
                    color: #8B0000;  
                }}
                h2 {{
                    color: #8B0000;  
                }}
                h3 {{
                    color: #8B0000;  
                }}
                b {{
                   color: #8B0000;  /* Este es el color rojo oscuro */
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                }}
                th, td {{
                    padding: 8px 12px;
                    text-align: left;
                    border: 1px solid #ddd;
                }}
                th {{
                    background-color: #800000;      /* #800000 ori#96C60F */
                    color: white;
                }}
                tr:nth-child(even) {{
                    background-color: #f9f9f9; 
                }}
                /* Estilo general para los enlaces */
                a {{
                    text-decoration: none;          /* Eliminar subrayado */
                    color: #8B0000;                 /* Rojo oscuro */
                    font-family: 'Georgia', serif;  /* Fuente elegante */
                    font-size: 1rem;                /* Tamaño de texto adecuado */
                    font-weight: 500;               /* Peso de fuente para mayor elegancia */
                    transition: color 0.3s ease, transform 0.3s ease; /* Transición suave */
                }}
                /* Efecto cuando el enlace es hover */
                a:hover {{
                    color: #B22222;                 /* Rojo más brillante en hover */
                    transform: translateY(-2px);    /* Efecto sutil de elevación */
                }}
                /* Efecto al hacer clic en el enlace */
                a:active {{
                    color: #A52A2A;                 /* Rojo terracota cuando se hace clic */
                    transform: translateY(0);       /* Vuelve a la posición original */
                }}
                /* Enlaces visitados */
                a:visited {{
                    color: #8B0000;                 /* El mismo rojo oscuro para enlaces visitados */
                }}
            </style>
        </head>
        <body>
            <div class="content">
                
                <h2>LISTA DE TAREAS PENDIENTES.</h2>
                
                <p>{cuerpo}</p>
          
                A continuación, se enumeran las tareas pendientes de revisión:  <br> <br>
          
                <table style="border-collapse: collapse;">
                    <tr>
                        <th style="text-align: left; padding: 8px; width: 200px; border: 1px solid white;">Fecha Aviso:</th>
                        <td style="padding: 8px; border: 1px solid white;">{var_Fecha}</td>
                    </tr>
                    <tr>
                        <th style="text-align: left; padding: 8px; width: 200px; border: 1px solid white;">Tareas Pendientes:</th>
                        <td style="padding: 8px; border: 1px solid white;">{len(df)}</td>
                    </tr>
                </table>
                <br>

                {tabla_html} 

                <br><br>
                <br><br>
                <br><br>
                <br><br>
                    
                <i> ** Este email fue enviado desde un proceso automático desde TdA. Por favor, no responder a este email. ** </i>
                
                <p>
                   <br><br>

                    <table style="border: none; padding: 10px; border-spacing: 2px; width: 600px; table-layout: fixed;">
                        <tr>
                            <td style="width: 150px; padding-right: 10px; vertical-align: middle; border: 1px solid white;">
                                <img src="https://www.tda-sgft.com/TdaWeb/images/logotipo.gif" alt="Titulización de Activos S.G.F.T., S.A" style="vertical-align: middle;">
                            </td>
                            <td style="width: 450px; padding-left: 10px; vertical-align: middle; border: 1px solid white;">
                                <pre>
 Titulización de Activos S.G.F.T., S.A.
 C/Orense, 58 - 5ª Planta
 28020 Madrid
 Tel.: 91 702 08 08
 Fax:  91 308 68 54             
 e-mail: publicacionesbolsasmx@tda-sgft.com
 http://www.tda-sgft.com       </pre>
                            </td>
                        </tr>
                    </table>
                </p>
            </div>
            <!-- By: SteveCarpio:  stv.madrid@gmail.com  -->
        </body>
        </html>
        """
        # El cuerpo del mensaje en formato: html
        mensaje.attach(MIMEText(cuerpo_html, 'html'))

        # Combinar la ruta con el nombre del archivo
        #archivo_completo = os.path.join(ruta, nombre_archivo)


        # Enviar el correo
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as servidor:
                servidor.sendmail(correo_remitente, todos_destinatarios, mensaje.as_string())
            print(f"- Correo enviado exitosamente a: {', '.join(todos_destinatarios)}")
        except Exception as e:
            print(f"- Error al enviar el correo: {e}")


    else:
        print("No se mandará email porque no hay registros a informar..")

def Leer_Csv_DataFrame(var_Fecha):
    
    # Leo el CSV generado por el proceso VBA de access de Eventos
    df = pd.read_csv(f'{sTv.loc_RutaAccess}{sTv.var_NombreCsvDiario}', delimiter=';', quotechar='"', encoding='latin1')
  
    # Convertir la columna 1 a fecha
    df['FECHA_AVISO'] = pd.to_datetime(df['FECHA_AVISO'], errors='coerce', dayfirst=True)

    # Filtramos el registros a informar 
    df_filtrado = df[df['FECHA_AVISO'].dt.date == pd.to_datetime(var_Fecha).date()]
    df_filtrado = df_filtrado.reset_index(drop=True)
    df_filtrado.index = df_filtrado.index + 1

    return df_filtrado

# ----------------------------------------------------------------------------------------
#                               INICIO PROGRAMA
# ----------------------------------------------------------------------------------------

def sTv_paso3(var_Fecha, var_Entorno):

    # Ruta del archivo
    var_csv = f'{sTv.loc_RutaAccess}{sTv.var_NombreCsvDiario}'
    print(f"- File:  {var_csv}")

    # Leer CSV en un DataFrame
    df = Leer_Csv_DataFrame(var_Fecha)

    # Mandar Email Diario con el DataFrame filtrado
    if var_Entorno == "PRO":
        if len(df) > 1:
            print("- Running en modo: PRO - OK existen datos")
            destinatarios_to=['repcomun@tda-sgft.com']                       #  repcomun@tda-sgft.com
            destinatarios_cc=['carpios@tda-sgft.com']
            var_Asunto=f"[AVISO] Tareas Pendientes de Revisión - Informe {var_Fecha} | TDA Update"
        else:
            print("- Running en modo: PRO - NO existen datos")
            destinatarios_to=['talanvanf@tda-sgft.com','blancod@tda-sgft.com'] #  'talanvanf@tda-sgft.com','blancod@tda-sgft.com'
            destinatarios_cc=['carpios@tda-sgft.com']
            var_Asunto=f"[INFO] No hay tareas Pendientes de Revisión - Informe {var_Fecha} | TDA Update"
    else:
        print("- Running en modo: DEV")
        destinatarios_to=['carpios@tda-sgft.com']
        destinatarios_cc=['carpios@tda-sgft.com']
        var_Asunto=f"[ ... ] Tareas Pendientes de Revisión - Informe {var_Fecha} | TDA Update - modo DEV"
    
    var_Cuerpo=""

    Mandar_Email_Diario(destinatarios_to, destinatarios_cc, var_Asunto, var_Cuerpo, df, var_Fecha)