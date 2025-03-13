Attribute VB_Name = "M_PRINCIPAL"
Option Compare Database
Option Explicit

Sub CALENDARIZAR_MAIN()
    Dim c_fechaInicio, c_fechaFin As Date
    Dim c_idPlanif As String
    Dim c_periodicidad As String
    Dim c_hn_1, c_hn_2 As String
    Dim c_limitEjecucion, c_aviso As Integer
    Dim db As DAO.Database
    Dim rs As DAO.Recordset
    Dim strSQL As String
    Dim resultado As String
    
    
    Set db = CurrentDb()
    
    strSQL = "DELETE FROM LANZADOR;"
    db.Execute strSQL, dbFailOnError
    
    strSQL = "SELECT ID_PLANIF, PERIODICIDAD, FECHA_FIN, LIMITE_EJECUCION, HN_1, AVISO, HN_2 FROM PLANIFICADOR WHERE P_ACT = 'S' "
    Set rs = db.OpenRecordset(strSQL)
    
    If Not rs.EOF Then
        Do While Not rs.EOF
            
            ' Leer datos del planificador
            c_idPlanif = rs!ID_PLANIF
            c_periodicidad = rs!PERIODICIDAD
            c_fechaFin = rs!FECHA_FIN
            c_limitEjecucion = rs!LIMITE_EJECUCION
            c_hn_1 = rs!HN_1
            c_aviso = rs!AVISO
            c_hn_2 = rs!HN_2
            c_fechaInicio = Date ' #12/31/2023#
            
            ' FUNCION - CALCULO_ANUAL_31 ---------------------------------
            If c_periodicidad = "Anual-31" Then
                resultado = CALCULO_ANUAL_31(c_idPlanif, c_fechaInicio, c_fechaFin, c_limitEjecucion, c_aviso, c_hn_1, c_hn_2)
            End If
            

            rs.MoveNext
        Loop
    Else
        Debug.Print "No se encontraron registros con la condición especificada."
    End If
    rs.Close
    Set rs = Nothing
    Set db = Nothing
End Sub
