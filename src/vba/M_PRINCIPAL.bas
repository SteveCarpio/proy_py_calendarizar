Attribute VB_Name = "M_PRINCIPAL"
Option Compare Database
Option Explicit

Sub CALENDARIZAR_MAIN()
    Dim c_id2 As Integer
    Dim c_fechaInicio As Date
    Dim c_fechaFin As Date
    Dim c_idPlanif As String
    Dim c_periodicidad As String
    Dim c_hn_1 As String
    Dim c_hn_2 As String
    Dim c_limitEjecucion As Integer
    Dim c_aviso As Integer
    Dim db As DAO.Database
    Dim rs As DAO.Recordset
    Dim strSQL As String
    Dim numTareas, totalTareas1, totalTareas2, totalTareas3, totalTareas4 As Integer
       
    Set db = CurrentDb()
    strSQL = "DELETE FROM 3_LANZADOR;"
    db.Execute strSQL, dbFailOnError
    strSQL = "SELECT id2, ID_PLANIF, PERIODICIDAD, FECHA_INI, FECHA_FIN, LIMITE_EJECUCION, HN_1, AVISO, HN_2 FROM 2_PLANIFICADOR WHERE P_ACT = 'S' "
    Set rs = db.OpenRecordset(strSQL)
    
    If Not rs.EOF Then
        
        totalTareas1 = 0
        totalTareas2 = 0
 
        Do While Not rs.EOF
            
            ' Leer datos del planificador
            c_id2 = rs!Id2
            c_idPlanif = rs!ID_PLANIF
            c_periodicidad = rs!PERIODICIDAD
            If IsNull(rs!FECHA_INI) Then
                c_fechaInicio = Date   ' #12/31/2023#
              Else
                c_fechaInicio = rs!FECHA_INI
            End If
            c_fechaFin = rs!FECHA_FIN
            c_limitEjecucion = rs!LIMITE_EJECUCION
            c_hn_1 = rs!HN_1
            c_aviso = rs!AVISO
            c_hn_2 = rs!HN_2
            
            ' FUNCION - CALCULO_ANUAL_31 -----------------------------------
            numTareas = 0
            If c_periodicidad = "Anual-31" And c_id2 = 55 Then
                numTareas = CALCULO_ANUAL_31(c_id2, c_idPlanif, c_fechaInicio, c_fechaFin, c_limitEjecucion, c_aviso, c_hn_1, c_hn_2)
                totalTareas1 = totalTareas1 + numTareas
            End If
            
            ' FUNCION - CALCULO_MENSUAL_31 ---------------------------------
            numTareas = 0
            If c_periodicidad = "Mensual-31" Then
                'numTareas = CALCULO_MENSUAL_31(c_id2, c_idPlanif, c_fechaInicio, c_fechaFin, c_limitEjecucion, c_aviso, c_hn_1, c_hn_2)
                totalTareas2 = totalTareas2 + numTareas
                'Debug.Print ("------------------------------------------------------------ ")
            End If
            
            ' FUNCION - CALCULO_TRIMESTRAL ---------------------------------
            numTareas = 0
            If c_periodicidad = "Trimestral" Then
                'numTareas = CALCULO_TRIMESTRAL(c_id2, c_idPlanif, c_fechaInicio, c_fechaFin, c_limitEjecucion, c_aviso, c_hn_1, c_hn_2)
                totalTareas3 = totalTareas3 + numTareas
            End If
            
            ' FUNCION - CALCULO_UNAVEZ -------------------------------------
            numTareas = 0
            If c_periodicidad = "UnaVez" Then
                'numTareas = CALCULO_UNAVEZ(c_id2, c_idPlanif, c_fechaInicio, c_fechaFin, c_limitEjecucion, c_aviso, c_hn_1, c_hn_2)
                totalTareas4 = totalTareas4 + numTareas
            End If
            

            rs.MoveNext
        Loop
        'Debug.Print (vbCrLf & "Número de tareas programadas para: " & vbCrLf & vbCrLf & _
                "- (ANUL-31)   : " & totalTareas1 & vbCrLf & _
                "- (MENSUAL-31): " & totalTareas2 & vbCrLf & _
                "- (TRIMESTRAL): " & totalTareas3 & vbCrLf & _
                "- (UNAVEZ)    : " & totalTareas4 & vbCrLf)
        
        INICIALIZA_ID3
        
       ' MsgBox ("Número de tareas programadas para: " & vbCrLf & vbCrLf & _
                "- (ANUL-31)   : " & totalTareas1 & vbCrLf & _
                "- (MENSUAL-31): " & totalTareas2 & vbCrLf & _
                "- (TRIMESTRAL): " & totalTareas3 & vbCrLf & _
                "- (UNAVEZ)    : " & totalTareas4)
        
    Else
        Debug.Print "No se encontraron registros con la condición especificada."
    End If
    rs.Close
    Set rs = Nothing
    Set db = Nothing
End Sub
