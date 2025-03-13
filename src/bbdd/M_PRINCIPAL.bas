Attribute VB_Name = "M_PRINCIPAL"
Option Compare Database
Option Explicit

Sub CALENDARIZAR_MAIN()
    Dim c_fechaFin As Date
    Dim c_idPlanif As String
    Dim c_periodicidad As String
    Dim c_hn_1, c_hn_2 As String
    Dim c_limitEjecucion, c_aviso As Integer
    Dim db As DAO.Database
    Dim rs As DAO.Recordset
    Dim strSQL As String
    Dim resultado As String
    
    
    Set db = CurrentDb()
    strSQL = "SELECT ID_PLANIF, PERIODICIDAD, FECHA_FIN, LIMITE_EJECUCION, HN_1, AVISO, HN_2 FROM PLANIFICADOR WHERE P_ACT = 'S' "
    Set rs = db.OpenRecordset(strSQL)
    
    If Not rs.EOF Then
        Do While Not rs.EOF
            
            ' Leer datos del planificador
            c_idPlanif = rs!id_planif
            c_periodicidad = rs!periodicidad
            c_fechaFin = rs!fecha_fin
            c_limitEjecucion = rs!limite_ejecucion
            c_hn_1 = rs!hn_1
            c_aviso = rs!aviso
            c_hn_2 = rs!hn_2
            
            ' FUNCION - CALCULO_ANUAL_31 ---------------------------------
            If c_periodicidad = "Anual-31" Then
                resultado = CALCULO_ANUAL_31(c_idPlanif, c_fechaFin, c_limitEjecucion, c_aviso, c_hn_1, c_hn_2)
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
