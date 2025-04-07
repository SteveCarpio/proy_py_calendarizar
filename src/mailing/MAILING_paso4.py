# ----------------------------------------------------------------------------------------
#  PASO4: Enviar Email Mensual   
#  Autor: SteveCarpio-2025
# ----------------------------------------------------------------------------------------

import cfg.MAILING_variables as sTv
from   cfg.MAILING_library import *

# ----------------------------------------------------------------------------------------
#                                  FUNCIONES
# ----------------------------------------------------------------------------------------

def Mandar_Email_SemanalMensual(destinatarios_to, destinatarios_cc, asunto, cuerpo, var_Fecha, df1, df2, p_Lunes, p_Domingo, p_AnoMes):
    
    registros1 = len(df1)
    registros2 = len(df2)
    print(f"Se han recibido: {registros1} registros para el informe Semanal ")
    print(f"Se han recibido: {registros2} registros para el informe Mensual ")

    if (registros1 + registros2) >= 0:
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
        df1['DETALLE_DEL_EVENTO'] = df1['DETALLE_DEL_EVENTO'].apply(lambda x: str(x).replace('\r', '').replace('\n', '<br>'))
        df2['DETALLE_DEL_EVENTO'] = df2['DETALLE_DEL_EVENTO'].apply(lambda x: str(x).replace('\r', '').replace('\n', '<br>'))

        # Convertir el DataFrame a HTML, escarpe=False para que tenga en cuenta los BR
        tabla_html1 = df1.to_html(index=True, escape=False)  # con el índice
        tabla_html2 = df2.to_html(index=True, escape=False)  # con el índice

        

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
                    background-color: #800000;   /* #800000 ori#96C60F */
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
        
                <h2>LISTA DE TAREAS DE LA PRÓXIMA SEMANA.</h2>
                <p>{cuerpo}</p>
                A continuación, se enumeran las tareas pendientes de la próxima semana que requieren revisión: <br> <br>
                <table style="border-collapse: collapse;">
                    <tr>
                        <th style="text-align: left; padding: 8px; width: 200px; border: 1px solid white;">Próximo_Lunes:</th>
                        <td style="padding: 8px; border: 1px solid white;">{p_Lunes.year}-{p_Lunes.month:02}-{p_Lunes.day:02} </td>
                    </tr>
                    <tr>
                        <th style="text-align: left; padding: 8px; width: 200px; border: 1px solid white;">Próximo_Domingo:</th>
                        <td style="padding: 8px; border: 1px solid white;">{p_Domingo.year}-{p_Domingo.month:02}-{p_Domingo.day:02}</td>
                    </tr>
                    <tr>
                        <th style="text-align: left; padding: 8px; width: 200px; border: 1px solid white;">Tareas Pendientes:</th>
                        <td style="padding: 8px; border: 1px solid white;">{len(df1)}</td>
                    </tr>
                </table>
                <br>
                {tabla_html1}


                <br><br><br>

              

                <h2>LISTA DE TAREAS DEL PRÓXIMO MES.</h2>
                <p>{cuerpo}</p>
                A continuación, se enumeran las tareas pendientes del próximo mes que requieren revisión: <br> <br>
                <table style="border-collapse: collapse;">
                    <tr>
                        <th style="text-align: left; padding: 8px; width: 200px; border: 1px solid white;">Año Mes:</th>
                        <td style="padding: 8px; border: 1px solid white;">{p_AnoMes} </td>
                    </tr>
                    <tr>
                        <th style="text-align: left; padding: 8px; width: 200px; border: 1px solid white;">Tareas Pendientes:</th>
                        <td style="padding: 8px; border: 1px solid white;">{len(df2)}</td>
                    </tr>
                </table>
                <br>

                {tabla_html2} 

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
        print("No se mandará email porque no hay registros a informar.")

# Leo el CSV generado por el proceso VBA de access de Eventos
def Leer_Csv_DataFrame():
    df = pd.read_csv(f'{sTv.loc_RutaAccess}{sTv.var_NombreCsvMensual}', delimiter=';', quotechar='"', encoding='latin1')
    df['FECHA_LIMITE'] = pd.to_datetime(df['FECHA_LIMITE'], errors='coerce', dayfirst=True)  # Convertir a fecha
    return df

def Crear_DF_Semanal(df, var_Ano, var_Mes, var_Dia):
    
    # Fecha de hoy
    hoy = datetime.date(var_Ano, var_Mes, var_Dia)

    # Calcular cuántos días faltan para el próximo lunes
    dias_para_lunes = (7 - hoy.weekday()) % 7
    if dias_para_lunes == 0:
        dias_para_lunes = 7  # Si hoy es lunes, tomamos el siguiente lunes

    # Si hoy es lunes, se tomará el próximo lunes (no el de hoy)
    proximo_lunes = hoy + datetime.timedelta(days=dias_para_lunes)

    # El próximo domingo será 6 días después del próximo lunes
    proximo_domingo = proximo_lunes + datetime.timedelta(days=6)

    # Convertir las fechas de cadena a tipo datetime
    proximo_lunes = pd.to_datetime(proximo_lunes)
    proximo_domingo = pd.to_datetime(proximo_domingo)

    # Filtrar el DataFrame entre las fechas inicial y final
    df_filtrado = df[(df['FECHA_LIMITE'] >= proximo_lunes) & (df['FECHA_LIMITE'] <= proximo_domingo)]
    df_filtrado = df_filtrado.reset_index(drop=True)
    df_filtrado.index = df_filtrado.index + 1

    # Eliminar las columnas que nos necesarias del DataFrame
    df_resultado = df_filtrado.drop(columns=['ANO', 'MES', 'SEMANA'])

    # Mostrar los resultados
    print(f"\nDatos para el informe Semanal.")
    print(f"Próximo lunes:   {proximo_lunes}")
    print(f"Próximo domingo: {proximo_domingo}")
    print(f" \n{df_resultado}")

    return df_resultado, proximo_lunes, proximo_domingo

def Crear_DF_Mensual(df, var_Ano, var_Mes):

    print(var_Ano, var_Mes)

    # Me situó en el mes siguiente
    var_Mes += 1
    if (var_Mes) > 12:
        var_Mes = 1
        var_Ano += 1

    print(var_Ano, var_Mes)

    # Filtro el mes siguiente
    df_filtrado = df[(df['ANO'] == var_Ano) & (df['MES'] == var_Mes)]
    df_filtrado = df_filtrado.reset_index(drop=True)
    df_filtrado.index = df_filtrado.index + 1

    # Eliminar las columnas que nos necesarias del DataFrame
    df_resultado = df_filtrado.drop(columns=['ANO', 'MES', 'SEMANA'])

    # Mostrar los resultados
    print(f"\nDatos para el informe Mensual.\nPróximo Año y Mes: {var_Ano}-{var_Mes}")
    print(f"\n{df_resultado}")
    var_AnoMes = f"{var_Ano}-{var_Mes:02}"

    return df_resultado, var_AnoMes

# ----------------------------------------------------------------------------------------
#                               INICIO PROGRAMA
# ----------------------------------------------------------------------------------------

def sTv_paso4(tiempo_inicio, var_Entorno):

    # Ruta del archivo
    var_csv = f'{sTv.loc_RutaAccess}{sTv.var_NombreCsvDiario}'
    print(f"File:  {var_csv}")

    # Leer CSV en un DataFrame
    df = Leer_Csv_DataFrame()
    df_Semanal, p_Lunes, p_Domingo = Crear_DF_Semanal(df, tiempo_inicio.year, tiempo_inicio.month, tiempo_inicio.day)
    df_Mensual, p_AnoMes = Crear_DF_Mensual(df, tiempo_inicio.year, tiempo_inicio.month)
    

    # Mandar Email Diario con el DataFrame filtrado
    if var_Entorno == "PRO":
        print("\nEnvió del email en modo: PRO")
        destinatarios_to=['repcomun@tda-sgft.com']
        destinatarios_cc=['carpios@tda-sgft.com']
    else:
        print("\nEnvió del email en modo: DEV")
        destinatarios_to=['carpios@tda-sgft.com']
        destinatarios_cc=['carpios@tda-sgft.com']
    
    var_Asunto=f"Resumen Tareas Pendientes a Revisar - Informe {tiempo_inicio.year}-{tiempo_inicio.month:02}-{tiempo_inicio.day:02} | TDA Update"
    var_Cuerpo=""

    Mandar_Email_SemanalMensual(destinatarios_to, destinatarios_cc, var_Asunto, var_Cuerpo, tiempo_inicio, df_Semanal, df_Mensual, p_Lunes, p_Domingo, p_AnoMes)