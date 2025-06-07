Public Class Form1
    Private Sub Button1_Click(sender As Object, e As EventArgs)
        MsgBox("HI BRO")
        MsgBox("HOW ARE YOU")
        MsgBox("I'm fine")
    End Sub

    Private Sub Label1_Click(sender As Object, e As EventArgs) Handles Label1.Click

    End Sub

    Private Sub Timer1_Tick(sender As Object, e As EventArgs) Handles Timer1.Tick
        If Label1.Visible Then
            Label1.Visible = False
            Label2.Visible = True
            Label3.Visible = False
        ElseIf Label2.Visible Then
            Label1.Visible = False
            Label2.Visible = False
            Label3.Visible = True
        ElseIf Label3.Visible Then
            Label1.Visible = True
            Label2.Visible = False
            Label3.Visible = False
        End If
    End Sub
End Class
