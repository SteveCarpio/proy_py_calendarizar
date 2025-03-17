Attribute VB_Name = "M_LANZADOR"
Option Compare Database
Option Explicit

' Inicializa el campo ID3 y ID_LANZADOR secuensialmente
Sub INICIALIZA_ID3()
    Dim db As DAO.Database
    Dim rs As DAO.Recordset
    Dim id3, cont As Integer
    cont = 1
    Set db = CurrentDb()
    Set rs = db.OpenRecordset("SELECT * FROM 3_LANZADOR", dbOpenDynaset)
    While Not rs.EOF
        rs.Edit
        rs!id3 = cont
        rs!ID_LANZADOR = "LANZ" & Format(cont, "000000")
        rs.Update
        rs.MoveNext
        cont = cont + 1
    Wend
    rs.Close
    Set rs = Nothing
    Set db = Nothing
End Sub


