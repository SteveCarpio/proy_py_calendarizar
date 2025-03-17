Attribute VB_Name = "M_MENSUAL_31"
Option Compare Database
Option Explicit

Function CALCULO_MENSUAL_31(Id2 As Integer, idPlanif As String, fechaInicio, fechaFinal As Date, dias1, dias2 As Integer, hn1, hn2 As String) As Integer

    Dim fechaAnalizar As Date
    Dim fechaActual As Date
    Dim ultimo_dia_mes As Date
    Dim nuevaFecha As Date
    Dim fechaLimite As Date



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
        
        
        If dias1 > 0 Then
                fechaAnalizar = fechaAnalizar + 1
            End If
            If dias1 < 0 Then
                fechaAnalizar = fechaAnalizar - 1
        End If
        
        
        
        ' ---------------- LIMITE DE EJECUCION ----------------
            
            ' 1- Para días Naturales --------------
            If hn1 = "DN" Then
                fechaLimite = fechaAnalizar
                fechaAnalizar = fechaAnalizar + dias1
                
            End If
 
            ' 2- Para días Hábiles ----------------
            If hn1 = "DH" Then
                         
                ' Analizamos cuando el valor es POSITIVO ----
                nuevaFecha = fechaAnalizar
                countDiasHabiles = 0
                    
                Do While countDiasHabiles < Abs(dias1)
                    
                    ' Verificar si el día no es sábado (7) ni domingo (1)
                    dia = Weekday(nuevaFecha)
                    If dia <> 7 And dia <> 1 Then
                            
                        ' Verificar si el día no es festivo usando DLookup
                        festivo = Not IsNull(DLookup("Festivo", "Festivos", "Festivo = #" & nuevaFecha & "#"))
                
                        ' Si no es festivo, contar como día hábil
                        If Not festivo Then
                            countDiasHabiles = countDiasHabiles + 1
                            fechaAnalizar = nuevaFecha
                            'Debug.Print ("hb 1: " & countDiasHabiles & " - " & nuevaFecha & " - " & dia)
                         End If
                    End If
                        
                    ' Si el valor es POSITIVO
                    If dias1 > 0 Then
                        fechaLimite = nuevaFecha
                        nuevaFecha = nuevaFecha + 1
                    End If
                    ' Si el valor es NEGATIVO
                    If dias1 < 0 Then
                        fechaLimite = nuevaFecha
                        nuevaFecha = nuevaFecha - 1
                    End If
                Loop
            End If
                     
            
            ' -------------------- AVISO --------------------
            
            ' 1- Para días Naturales ------------------------
            If hn2 = "DN" Then
                fechaAnalizar = fechaAnalizar + dias2
            End If
            
            ' 2- Para días Hábiles --------------------------
            If hn2 = "DH" Then
            
                If dias2 > 0 Then
                    fechaAnalizar = fechaAnalizar + 1
                End If
                If dias2 < 0 Then
                    fechaAnalizar = fechaAnalizar - 1
                End If
            
                nuevaFecha = fechaAnalizar
                
                countDiasHabiles = 0
                Do While countDiasHabiles < Abs(dias2)
                    
                    ' Verificar si el día no es sábado (7) ni domingo (1)
                    dia = Weekday(nuevaFecha)
                    If dia <> 7 And dia <> 1 Then
                            
                        ' Verificar si el día no es festivo usando DLookup
                        festivo = Not IsNull(DLookup("Festivo", "Festivos", "Festivo = #" & nuevaFecha & "#"))
                
                        ' Si no es festivo, contar como día hábil
                        If Not festivo Then
                            countDiasHabiles = countDiasHabiles + 1
                            fechaAnalizar = nuevaFecha
                            'Debug.Print ("hb 2: " & countDiasHabiles & " - " & nuevaFecha & " - " & dia)
                            
                         End If
                    End If
                        
                    ' Si el valor es POSITIVO
                    If dias2 > 0 Then
                        nuevaFecha = nuevaFecha + 1
                    End If
                    ' Si el valor es NEGATIVO
                    If dias2 < 0 Then
                        nuevaFecha = nuevaFecha - 1
                    End If
                Loop

            End If
            
            cont = cont + 1
            
            'Debug.Print (idPlanif & "       - " & fechaAnalizar & " " & cont)
            
            ' Insertar nuevos datos en la tabla LANZADOR
            'strSQL = "INSERT INTO 3_LANZADOR (id2, ID_PLANIF, FECHA_AVISO) " & _
                     "VALUES (" & Id2 & ",'" & idPlanif & "', #" & fechaAnalizar & "#);"
                     
            strSQL = "INSERT INTO 3_LANZADOR (id2, ID_PLANIF, FECHA_LIMITE, FECHA_AVISO) " & _
                      "VALUES (" & Id2 & ",'" & idPlanif & "', #" & Format(fechaLimite, "yyyy-mm-dd") & "#, #" & Format(fechaAnalizar, "yyyy-mm-dd") & "#);"

            
            db.Execute strSQL, dbFailOnError
            
            
 
        
        
        
        
        
        
        
        
        
        ' ------------------------------------------------------------------------------------------------------------------
        
        ' Mostrar el aviso Final
        Debug.Print ("OLD: " & ultimo_dia_mes & " - NEW: " & fechaAnalizar & " - ID_PLANIF: " & idPlanif & " - " & hn1 & dias1 & " " & hn2 & dias2)
        
        
        ' Avanzamos al siguiente mes
        fechaActual = DateAdd("m", 1, fechaActual)
        fechaActual = DateSerial(Year(fechaActual), Month(fechaActual), 1) ' Establecer el primer día del siguiente mes
    
    Loop
    
End Function

Function ObtenerUltimoDiaDelMes(fecha As Date) As Date
    ' Devuelve el último día del mes de una fecha dada
    ObtenerUltimoDiaDelMes = DateSerial(Year(fecha), Month(fecha) + 1, 0)
End Function

