Public Class Form1
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim a As Integer
        a = InputBox("Enter Marks")
        If a < 40 Then
            MsgBox("Fail")
        ElseIf a < 50 Then
            MsgBox("You got c grade")
        ElseIf a < 70 Then
            MsgBox("You got B grade")
        Else
            MsgBox("You got A grade")
        End If
    End Sub
End Class
