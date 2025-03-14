Attribute VB_Name = "M_PRINCIPAL"
Option Compare Database
Option Explicit

Sub CALENDARIZAR_MAIN()
    Dim c_id2 As Integer
    Dim c_fechaInicio, c_fechaFin As Date
    Dim c_idPlanif As String
    Dim c_periodicidad As String
    Dim c_hn_1, c_hn_2 As String
    Dim c_limitEjecucion, c_aviso As Integer
    Dim db As DAO.Database
    Dim rs As DAO.Recordset
    Dim strSQL As String
    Dim numTareas, totalTareas1 As Integer
       
    Set db = CurrentDb()
    strSQL = "DELETE FROM 3_LANZADOR;"
    db.Execute strSQL, dbFailOnError
    strSQL = "SELECT id2, ID_PLANIF, PERIODICIDAD, FECHA_INI, FECHA_FIN, LIMITE_EJECUCION, HN_1, AVISO, HN_2 FROM 2_PLANIFICADOR WHERE P_ACT = 'S' "
    Set rs = db.OpenRecordset(strSQL)
    
    If Not rs.EOF Then
 
        Do While Not rs.EOF
            
            ' Leer datos del planificador
            c_id2 = rs!Id2
            c_idPlanif = rs!ID_PLANIF
            c_periodicidad = rs!PERIODICIDAD
            c_fechaInicio = Date ' #12/31/2023#  puedes poner un IF si viene vacia poner DATE si no poner lo de la tabla
            c_fechaFin = rs!FECHA_FIN
            c_limitEjecucion = rs!LIMITE_EJECUCION
            c_hn_1 = rs!HN_1
            c_aviso = rs!AVISO
            c_hn_2 = rs!HN_2
            
            ' FUNCION - CALCULO_ANUAL_31 ---------------------------------
            If c_periodicidad = "Anual-31" Then
                numTareas = CALCULO_ANUAL_31(c_id2, c_idPlanif, c_fechaInicio, c_fechaFin, c_limitEjecucion, c_aviso, c_hn_1, c_hn_2)
                totalTareas1 = totalTareas1 + numTareas
            End If
            

            rs.MoveNext
        Loop
        INICIALIZA_ID3
        Debug.Print ("Número de tareas programadas para (ANUL-31): " & totalTareas1)
        
    Else
        Debug.Print "No se encontraron registros con la condición especificada."
    End If
    rs.Close
    Set rs = Nothing
    Set db = Nothing
End Sub
