﻿Public Class Form1
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        C.Text = Val(A.Text) + Val(B.Text)
    End Sub
    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        C.Text = Val(A.Text) - Val(B.Text)
    End Sub
    Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Button3.Click
        C.Text = Val(A.Text) * Val(B.Text)
    End Sub
    Private Sub Button4_Click(sender As Object, e As EventArgs) Handles Button4.Click
        C.Text = Val(A.Text) / Val(B.Text)
    End Sub
    Private Sub Button5_Click(sender As Object, e As EventArgs) Handles Button5.Click
        C.Text = Val(A.Text) * Val(A.Text)
    End Sub
    Private Sub Button6_Click(sender As Object, e As EventArgs) Handles Button6.Click
        C.Text = Val(A.Text) * Val(A.Text) * Val(A.Text)
    End Sub

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub

End Class