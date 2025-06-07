import tkinter as tk; from tkinter.messagebox import showwarning
r,d,l,e=tk.Tk(),[],tk.Listbox(width=50),tk.Entry(width=50);r.geometry("400x300");[w.pack() for w in (l,e)]
f=lambda:(l.delete(0,'end'),[l.insert('end',i) for i in d])
a=lambda:(d.append(e.get()) if e.get() else showwarning("Error","Enter text"),e.delete(0,'end'),f())
u=lambda:(d.__setitem__(s:=l.curselection()[0],e.get()) if l.curselection() and e.get() else showwarning("Error","Select & enter text"),f())
x=lambda:(d.pop(s:=l.curselection()[0]) if l.curselection() else showwarning("Error","Select item"),f())
[r.title("CRUD"),*[tk.Button(text=t,command=c).pack() for t,c in [("Add",a),("Update",u),("Delete",x)]],f(),r.mainloop()]






# import tkinter as tk; from tkinter.messagebox import showwarning
# r,d,l,e=tk.Tk(),[],tk.Listbox(),tk.Entry();[w.pack() for w in (l,e)]
# f=lambda:(l.delete(0,'end'),[l.insert('end',i) for i in d])
# a=lambda:(d.append(e.get()) if e.get() else showwarning("Error","Enter text"),e.delete(0,'end'),f())
# u=lambda:(d.__setitem__(s:=l.curselection()[0],e.get()) if l.curselection() and e.get() else showwarning("Error","Select & enter text"),f())
# x=lambda:(d.pop(s:=l.curselection()[0]) if l.curselection() else showwarning("Error","Select item"),f())
# [r.title("CRUD"),*[tk.Button(text=t,command=c).pack() for t,c in [("Add",a),("Update",u),("Delete",x)]],f(),r.mainloop()]







# import tkinter as tk; from tkinter import messagebox
# root, data = tk.Tk(), []
# root.title("CRUD App")
# lb, e = tk.Listbox(root, width=40), tk.Entry(root, width=40)
# [widget.pack(pady=2) for widget in (lb, e)]
# refresh = lambda: (lb.delete(0, tk.END), [lb.insert(tk.END, i) for i in data])
# def add():
#     t = e.get()
#     if t: data.append(t); e.delete(0, tk.END); refresh()
#     else: messagebox.showwarning("Error", "Enter text")
# def update():
#     s = lb.curselection()
#     if s and e.get(): data[s[0]] = e.get(); refresh()
#     else: messagebox.showwarning("Error", "Select item and enter new text")
# def delete():
#     s = lb.curselection()
#     if s: data.pop(s[0]); refresh()
#     else: messagebox.showwarning("Error", "Select item to delete")
# for t, cmd in ("Add", add), ("Update", update), ("Delete", delete):
#     tk.Button(root, text=t, command=cmd).pack(pady=2)
# refresh(); root.mainloop()