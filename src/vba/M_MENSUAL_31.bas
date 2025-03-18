Attribute VB_Name = "M_MENSUAL_31"
Option Compare Database
Option Explicit
  
Function CALCULO_MENSUAL_31(Id2 As Integer, idPlanif As String, fechaInicio, fechaFinal As Date, dias1 As Integer, dias2 As Integer, hn1 As String, hn2 As String) As Integer

    Dim fechaAnalizar As Date
    Dim fechaActual As Date
    Dim ultimo_dia_mes As Date
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
    Set rs = db.OpenRecordset("SELECT Festivo FROM Festivos", dbOpenSnapshot)

    cont = 0
    
    ' Inicializar fecha_actual con la fecha de inicio
    fechaActual = fechaInicio
    
    ' Bucle para iterar sobre cada mes
    Do While fechaActual <= fechaFinal
    
        ' Obtener el último día del mes actual
        ultimo_dia_mes = ObtenerUltimoDiaDelMes(fechaActual)
        
        ' Si el último día es mayor que la fecha de fin, salimos del bucle
        If ultimo_dia_mes > fechaFinal Then Exit Do
        
        fechaAnalizar = ultimo_dia_mes
        
        ' Compuebo que no supero la fecha final
        If fechaAnalizar <= fechaFinal Then
            
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
            'Debug.Print ("FECHA_AVISO:  " & fechaAviso & " - " & hn2 & dias2)
            
            ' Insertar nuevos datos en la tabla LANZADOR
            strSQL = "INSERT INTO 3_LANZADOR (id2, ID_PLANIF, FECHA_LIMITE, FECHA_AVISO) " & _
                    "VALUES (" & Id2 & ",'" & idPlanif & "', #" & Format(fechaLimite, "yyyy-mm-dd") & "#, #" & Format(fechaAviso, "yyyy-mm-dd") & "#);"
            db.Execute strSQL, dbFailOnError
            
            cont = cont + 1
        End If
        ' ------------------------------------------------------------------------------------------------------------------
        ' Avanzamos al siguiente mes
        fechaActual = DateAdd("m", 1, fechaActual)
        fechaActual = DateSerial(Year(fechaActual), Month(fechaActual), 1) ' Establecer el primer día del siguiente mes
    Loop
    CALCULO_MENSUAL_31 = cont
End Function

Function ObtenerUltimoDiaDelMes(fecha As Date) As Date
    ' Devuelve el último día del mes de una fecha dada
    ObtenerUltimoDiaDelMes = DateSerial(Year(fecha), Month(fecha) + 1, 0)
End Function

