Imports System.Windows.Forms.VisualStyles.VisualStyleElement
Public Class Form1
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Select Case TextBox1.Text
            Case "a", "e", "i", "o", "u"
                TextBox3.Text = "Alphebet is a Vovel"
            Case Else
                TextBox3.Text = "Alphebet is a consonent"
        End Select
    End Sub
End Class