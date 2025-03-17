Attribute VB_Name = "M_CALCULO_DIAS"
Option Compare Database
Option Explicit
Function CALCULO_NATURALES(dias As Integer, hn As String, fechaAnalizar As Date) As Date
    fechaAnalizar = fechaAnalizar + dias
    CALCULO_NATURALES = fechaAnalizar
End Function
Function CALCULO_HABILES(dias As Integer, hn As String, fechaAnalizar As Date) As Date
    Dim db As DAO.Database
    Dim rs As DAO.Recordset
    Dim dia As Integer
    Dim countDiasHabiles As Integer
    Dim nuevaFecha As Date
    Dim festivo As Boolean
    Set db = CurrentDb
    Set rs = db.OpenRecordset("SELECT Festivo FROM Festivos", dbOpenSnapshot)
    countDiasHabiles = 0
    nuevaFecha = fechaAnalizar
    If dias > 0 Then
        nuevaFecha = nuevaFecha + 1
    End If
    If dias < 0 Then
        nuevaFecha = nuevaFecha - 1
    End If
    Do While countDiasHabiles < Abs(dias)
        dia = Weekday(nuevaFecha)
        If dia <> 7 And dia <> 1 Then    ' Verificar si el día no es sábado (7) ni domingo (1)
            ' Verificar si el día no es festivo usando DLookup
            festivo = Not IsNull(DLookup("Festivo", "Festivos", "Festivo = #" & nuevaFecha & "#"))
            If Not festivo Then  ' Si no es festivo, contar como día hábil
                countDiasHabiles = countDiasHabiles + 1
                fechaAnalizar = nuevaFecha
            End If
        End If
        If dias > 0 Then
            nuevaFecha = nuevaFecha + 1
        End If
        If dias < 0 Then
            nuevaFecha = nuevaFecha - 1
        End If
    Loop
    CALCULO_HABILES = fechaAnalizar
End Function

