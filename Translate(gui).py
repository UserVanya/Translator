from tkinter import *
from googletrans import Translator

def tran():
    text = t.get('1.0', END)
    a = translator.translate(text, dest='ru')
    t1.delete('1.0', END)
    t1.insert('1.0', a.text)

root = Tk()
root.geometry("500x500")
root.title("Translator")
root.resizable(width=False, height=False)
root['bg'] = 'black'
translator = Translator()

label = Label(root, fg='white', bg='black', font='Arial 15 bold', text='Введите текст на английском')
label.place(relx=0.5, y=30, anchor=CENTER)
t = Text(root, width=35, height=5, font='Arial 12 bold')
t.place(relx=0.5, y=100, anchor=CENTER)

bth = Button(root, width=45, text='Перевести', command=tran)
bth.place(relx=0.5, y=180, anchor=CENTER)

t1 = Text(root, width=35, height=5, font='Arial 12 bold')
t1.place(relx=0.5, y=260, anchor=CENTER)

root.mainloop()