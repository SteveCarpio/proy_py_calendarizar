Attribute VB_Name = "M_ANUAL_31"
Option Compare Database
Option Explicit

Function CALCULO_ANUAL_31(idPlanif As String, fechaFinal As Date, dias1, dias2 As Integer, hn1, hn2 As String) As String
    
    Dim fechaInicio, fechaAnalizar, nuevaFecha As Date
    Dim db As DAO.Database
    Dim rs As DAO.Recordset
    Dim ano_ini, ano_fin As Integer
    Dim countDiasHabiles, dia As Integer
    Dim festivo As Boolean
    Dim i As Integer
    
    ' Conexión con la tabla de festivos
    Set db = CurrentDb
    Set rs = db.OpenRecordset("SELECT Festivo FROM Festivos", dbOpenSnapshot)
    
    'fechaHoy = Date
    ano_ini = Year(Date)
    ano_fin = Year(fechaFinal)
    
    ' Recorro todos los años a analizar
    For i = ano_ini To ano_fin Step 1
    
        If dias1 > 0 Then
            fechaAnalizar = DateSerial(i, 12, 31) + 1
        End If
        If dias1 < 0 Then
            fechaAnalizar = DateSerial(i, 12, 31) - 1
        End If
        
        ' Compuebo que no supero la fecha final
        If fechaAnalizar <= fechaFinal Then
            
            ' -------- LIMITE DE EJECUCION --------
            ' 1- Para días Naturales --------------
            If hn1 = "DN" Then
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
                            'Debug.Print ("num dia habil: " & countDiasHabiles & " - " & nuevaFecha)
                         End If
                    End If
                        
                    ' Si el valor es POSITIVO
                    If dias1 > 0 Then
                        nuevaFecha = nuevaFecha + 1
                    End If
                    ' Si el valor es NEGATIVO
                    If dias1 < 0 Then
                        nuevaFecha = nuevaFecha - 1
                    End If
                Loop
            End If
            
            ' ------------ AVISO ------------
            ' 1- Para días Naturales --------
            If hn2 = "DN" Then
                fechaAnalizar = fechaAnalizar + dias2
            End If
            
            ' 2- Para días Hábiles --------
            If hn2 = "DH" Then
                fechaAnalizar = fechaAnalizar
                
               
            End If
            
            ' RESULTADO FINAL A PLANIFICAR
            Debug.Print (idPlanif & "       - " & fechaAnalizar)
            
        End If
    Next i
End Function










