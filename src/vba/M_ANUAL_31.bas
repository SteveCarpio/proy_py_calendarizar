Attribute VB_Name = "M_ANUAL_31"
Option Compare Database
Option Explicit

Function CALCULO_ANUAL_31(Id2 As Integer, idPlanif As String, fechaInicio, fechaFinal As Date, dias1 As Integer, dias2 As Integer, hn1 As String, hn2 As String) As Integer
    
    Dim fechaAnalizar As Date
    Dim nuevaFecha As Date
    Dim fechaLimite As Date
    Dim fechaAviso As Date
    Dim db As DAO.Database
    Dim rs As DAO.Recordset
    Dim strSQL As String
    Dim ano_ini, ano_fin As Integer
    Dim countDiasHabiles, dia, cont As Integer
    Dim festivo As Boolean
    Dim i As Integer
    
    ' Conexión con la tabla de festivos
    Set db = CurrentDb
      
    ano_ini = Year(fechaInicio)  ' Year(Date) ''
    ano_fin = Year(fechaFinal)
    cont = 0
    
    ' Recorro todos los años a analizar
    For i = ano_ini To ano_fin Step 1

        fechaAnalizar = DateSerial(i, 12, 31)
        
        ' Compuebo que no supero la fecha final
        If fechaAnalizar < fechaFinal Then
            
            ' FECHA_LIMITE -----------------------------
            If hn1 = "DN" Then
                fechaLimite = CALCULO_NATURALES(dias1, hn1, fechaAnalizar)
            Else
                fechaLimite = CALCULO_HABILES(dias1, hn1, fechaAnalizar)
            End If
            fechaAnalizar = fechaLimite
            
            ' FECHA_AVISO -----------------------------
            If hn2 = "DN" Then
                fechaAviso = CALCULO_NATURALES(dias2, hn2, fechaAnalizar)
            Else
                fechaAviso = CALCULO_HABILES(dias2, hn2, fechaAnalizar)
            End If

            Debug.Print ("FECHA_LIMITE: " & fechaLimite & " - " & hn1 & dias1)
            Debug.Print ("FECHA_AVISO:  " & fechaAviso & " - " & hn2 & dias2)
            
            ' Insertar nuevos datos en la tabla LANZADOR
            strSQL = "INSERT INTO 3_LANZADOR (id2, ID_PLANIF, FECHA_LIMITE, FECHA_AVISO) " & _
                    "VALUES (" & Id2 & ",'" & idPlanif & "', #" & Format(fechaLimite, "yyyy-mm-dd") & "#, #" & Format(fechaAviso, "yyyy-mm-dd") & "#);"
            db.Execute strSQL, dbFailOnError
            
            cont = cont + 1
        End If
    Next i
    ' Cerrar la conexión
    Set db = Nothing
    CALCULO_ANUAL_31 = cont
End Function

