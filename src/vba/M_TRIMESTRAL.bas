Attribute VB_Name = "M_TRIMESTRAL"
Option Compare Database
Option Explicit

Function CALCULO_TRIMESTRAL(Id2 As Integer, idPlanif As String, fechaInicio, fechaFinal As Date, dias1 As Integer, dias2 As Integer, hn1 As String, hn2 As String) As Integer
    Dim fechaFinalTrimestre As Date
    Dim trimestre As Integer
    Dim año As Integer
    Dim cont As Integer
    Dim listaFechas As Collection ' Colección para almacenar las fechas de fin de trimestre
    Dim fechaAnalizar As Date
    Dim fechaLimite As Date
    Dim fechaAviso As Date
    Dim db As DAO.Database
    Dim rs As DAO.Recordset
    Dim strSQL As String
    Dim i As Integer
    
    ' Conexión con la tabla de festivos
    Set db = CurrentDb
    
    ' Crear una nueva colección
    Set listaFechas = New Collection
    
    ' Definir las fechas de inicio y fin
 '   fechaInicio = #4/18/2025#
 '   fechaFin = #4/20/2026#
    
    ' Obtener el año de la fecha de inicio
    año = Year(fechaInicio)
    
    ' Calcular el primer trimestre basado en la fecha de inicio
    trimestre = Month(fechaInicio) \ 3 + 1
    
    ' Si la fecha de inicio está en un trimestre en particular y el primer trimestre de ese año aún no ha pasado hay q incluirlo.
    If fechaInicio <= DateSerial(año, 3, 31) Then
        fechaFinalTrimestre = DateSerial(año, 3, 31) ' 31 de marzo
        If fechaFinalTrimestre >= fechaInicio And fechaFinalTrimestre <= fechaFinal Then
            listaFechas.Add fechaFinalTrimestre ' Agregar a la colección
        End If
    End If
    
    ' Empezamos desde el trimestre más cercano después de FECHA_INICIO
    Do While True
        ' Calcular la fecha de final del trimestre
        Select Case trimestre
            Case 1
                fechaFinalTrimestre = DateSerial(año, 3, 31)  ' 31 de marzo
            Case 2
                fechaFinalTrimestre = DateSerial(año, 6, 30)  ' 30 de junio
            Case 3
                fechaFinalTrimestre = DateSerial(año, 9, 30)  ' 30 de septiembre
            Case 4
                fechaFinalTrimestre = DateSerial(año, 12, 31) ' 31 de diciembre
        End Select
        
        ' Si la fecha final de trimestre es mayor que la fecha de fin, terminamos
        If fechaFinalTrimestre > fechaFinal Then Exit Do
        
        ' Mostrar la fecha final del trimestre si está dentro del rango
        If fechaFinalTrimestre >= fechaInicio Then
            listaFechas.Add fechaFinalTrimestre ' Agregar a la colección
        End If
        
        ' Avanzar al siguiente trimestre
        trimestre = trimestre + 1
        If trimestre > 4 Then
            trimestre = 1
            año = año + 1 ' Avanzar al siguiente año
        End If
    Loop
    
    ' Recorro la lista
    cont = cont + 1
    For i = 1 To listaFechas.Count
        Debug.Print (listaFechas(i))
        
        fechaAnalizar = listaFechas(i)
        
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

    Next i
    Set db = Nothing
    CALCULO_TRIMESTRAL = cont
End Function
