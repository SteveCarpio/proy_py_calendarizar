Attribute VB_Name = "M_ANUAL_31"
Option Compare Database
Option Explicit

Function CALCULO_ANUAL_31(Id2 As Integer, idPlanif As String, fechaInicio, fechaFinal As Date, dias1, dias2 As Integer, hn1, hn2 As String) As Integer
    
    Dim fechaAnalizar, nuevaFecha As Date
    Dim db As DAO.Database
    Dim rs As DAO.Recordset
    Dim strSQL As String
    Dim ano_ini, ano_fin As Integer
    Dim countDiasHabiles, dia, cont As Integer
    Dim festivo As Boolean
    Dim i As Integer
    
    ' Conexi�n con la tabla de festivos
    Set db = CurrentDb
    Set rs = db.OpenRecordset("SELECT Festivo FROM Festivos", dbOpenSnapshot)
      
    ano_ini = Year(fechaInicio)  ' Year(Date) ''
    ano_fin = Year(fechaFinal)
    cont = 0
    
    ' Recorro todos los a�os a analizar
    For i = ano_ini To ano_fin Step 1
    
        
    
        If hn1 = "DN" Then
            fechaAnalizar = DateSerial(i, 12, 31)
          Else
            If dias1 > 0 Then
                fechaAnalizar = DateSerial(i, 12, 31) + 1
            End If
            If dias1 < 0 Then
                fechaAnalizar = DateSerial(i, 12, 31) - 1
            End If
        End If
        
        ' Compuebo que no supero la fecha final
        If fechaAnalizar < fechaFinal Then
            
            ' ---------------- LIMITE DE EJECUCION ----------------
            
            ' 1- Para d�as Naturales --------------
            If hn1 = "DN" Then
                fechaAnalizar = fechaAnalizar + dias1
            End If
 
            ' 2- Para d�as H�biles ----------------
            If hn1 = "DH" Then
                         
                ' Analizamos cuando el valor es POSITIVO ----
                nuevaFecha = fechaAnalizar
                countDiasHabiles = 0
                    
                Do While countDiasHabiles < Abs(dias1)
                    
                    ' Verificar si el d�a no es s�bado (7) ni domingo (1)
                    dia = Weekday(nuevaFecha)
                    If dia <> 7 And dia <> 1 Then
                            
                        ' Verificar si el d�a no es festivo usando DLookup
                        festivo = Not IsNull(DLookup("Festivo", "Festivos", "Festivo = #" & nuevaFecha & "#"))
                
                        ' Si no es festivo, contar como d�a h�bil
                        If Not festivo Then
                            countDiasHabiles = countDiasHabiles + 1
                            fechaAnalizar = nuevaFecha
                            'Debug.Print ("hb 1: " & countDiasHabiles & " - " & nuevaFecha & " - " & dia)
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
                     
            
            ' -------------------- AVISO --------------------
            
            ' 1- Para d�as Naturales ------------------------
            If hn2 = "DN" Then
                fechaAnalizar = fechaAnalizar + dias2
            End If
            
            ' 2- Para d�as H�biles --------------------------
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
                    
                    ' Verificar si el d�a no es s�bado (7) ni domingo (1)
                    dia = Weekday(nuevaFecha)
                    If dia <> 7 And dia <> 1 Then
                            
                        ' Verificar si el d�a no es festivo usando DLookup
                        festivo = Not IsNull(DLookup("Festivo", "Festivos", "Festivo = #" & nuevaFecha & "#"))
                
                        ' Si no es festivo, contar como d�a h�bil
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
            strSQL = "INSERT INTO 3_LANZADOR (id2, ID_PLANIF, FECHA_AVISO) " & _
                     "VALUES (" & Id2 & ",'" & idPlanif & "', #" & fechaAnalizar & "#);"
            db.Execute strSQL, dbFailOnError
            
        End If
        
    Next i
    ' Cerrar la conexi�n
    Set db = Nothing
    CALCULO_ANUAL_31 = cont
End Function










