Attribute VB_Name = "M_UNAVEZ"
Option Compare Database
Option Explicit

Function CALCULO_UNAVEZ(Id2 As Integer, idPlanif As String, fechaInicio, fechaFinal As Date, dias1 As Integer, dias2 As Integer, hn1 As String, hn2 As String) As Integer
    Dim fechaAnalizar As Date
    Dim nuevaFecha As Date
    Dim fechaLimite As Date
    Dim fechaAviso As Date
    Dim db As DAO.Database
    Dim rs As DAO.Recordset
    Dim strSQL As String
    
    Dim countDiasHabiles, dia, cont As Integer
    Dim festivo As Boolean
    Dim i As Integer
    
    ' Conexión con la tabla de festivos
    Set db = CurrentDb
      
    cont = 0
    fechaAnalizar = fechaFinal
        
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

    'Debug.Print ("FECHA_LIMITE: " & fechaLimite & " - " & hn1 & dias1)
    'Debug.Print ("FECHA_AVISO:  " & fechaAviso &  " - " & hn2 & dias2)
            
    ' Insertar nuevos datos en la tabla LANZADOR
    strSQL = "INSERT INTO 3_LANZADOR (id2, ID_PLANIF, FECHA_LIMITE, FECHA_AVISO) " & _
             "VALUES (" & Id2 & ",'" & idPlanif & "', #" & Format(fechaLimite, "yyyy-mm-dd") & "#, #" & Format(fechaAviso, "yyyy-mm-dd") & "#);"
    db.Execute strSQL, dbFailOnError
    Set db = Nothing
    
    cont = cont + 1
    CALCULO_UNAVEZ = cont
End Function

