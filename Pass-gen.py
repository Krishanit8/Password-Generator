import tkinter
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import random
import string
import pyperclip
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def main():
    win = tk.Tk()
    app = Passgen(win)
    win.mainloop()

class Passgen:
    def __init__(self, root):
        self.root = root
        self.root.title('Password Generator')
        self.root.resizable(0, 0)

        self.imglbl = ImageTk.PhotoImage(Image.open(resource_path('images\\imgbg1.jpg')).resize((600, 700)))
        Label(self.root, image=self.imglbl).pack()

        # ENTRYBOX++++++++++++++++++++++
        self.output_pass = StringVar()
        Entry(self.root, textvariable=self.output_pass, width=23, font=('Arial Rounded MT Bold', 18, 'bold'), bg='white',bd=0).place(x=125, y=135, height=65)

        # BUTTON+++++++++++
        self.imglbl1 = ImageTk.PhotoImage(Image.open(resource_path('images\\copy.jpg')).resize((35,35)))
        Button(self.root, image=self.imglbl1, bg='#C3FFFF', border=0,background='white', width=35, command=self.copy1).place(x=440, y=150)

        self.imglbl2 = ImageTk.PhotoImage(Image.open(resource_path('images\\Generatebtn.jpg')).resize((300,45)))
        Button(self.root, image=self.imglbl2, bg='#C3FFFF', border=0, width=300, command=self.Generate).place(x=150, y=520)

        self.imglbl3 = ImageTk.PhotoImage(Image.open(resource_path('images\\Exitbtn.jpg')).resize((15,13)))
        Button(self.root, image=self.imglbl3, bg='#C3FFFF', border=0,background='#C3FFFF', command=self.iExit).place(x=510, y=70)

        # SLIDER++++++++
        self.text = Label(self.root, text='Password Length', font=('Arial Rounded MT Bold', 18, 'bold'),bg='#C3FFFF').place(x=105, y=385)
        self.pass_len = IntVar()
        Scale(self.root, variable=self.pass_len,from_=1, to=12, orient=HORIZONTAL, bg='#C3FFFF', tickinterval=1, highlightthickness=0, length=400).place(x=110, y=420)

        # CHECKBUTTON+++++++++++++++
        self.vr1 = IntVar()
        self.vr2 = IntVar()
        self.vr3 = IntVar()

        Checkbutton(self.root, variable=self.vr1, text=' ALPHBATES', font=('Arial', 12), bg='#C3FFFF', activebackground='#C3FFFF', bd=0).place(x=140, y=260)
        Checkbutton(self.root, variable=self.vr2, text=' SPECIAL SYMBOLS', onvalue=1, offvalue=0, font=('Arial', 12), bg='#C3FFFF', activebackground='#C3FFFF', bd=0).place(x=140, y=300)
        Checkbutton(self.root, variable=self.vr3, text=' NUMBERS', onvalue=1, offvalue=0, font=('Arial', 12), bg='#C3FFFF', activebackground='#C3FFFF', bd=0).place(x=140, y=340)

        self.all_combi = [string.digits + string.punctuation]
        self.letters = random.sample(string.ascii_uppercase + string.ascii_lowercase, 4)
        self.combination =[self.all_combi + self.letters]

    def Generate(self):

        if self.pass_len.get() >= 4:

            if self.vr1.get()==0 and self.vr2.get()==0 and self.vr3.get() == 0:
                messagebox.showinfo('Password Generator', 'You have to choose at least two option',parent=self.root)

            elif self.vr1.get() == 1 and self.vr2.get() != 1 and self.vr3.get() != 1:
                messagebox.showinfo('Password Generator', 'You have to choose at least two option', parent=self.root)

            elif self.vr1.get() != 1 and self.vr2.get() == 1 and self.vr3.get() != 1:
                messagebox.showinfo('Password Generator', 'You have to choose at least two option', parent=self.root)
            elif self.vr1.get() != 1 and self.vr2.get() != 1 and self.vr3.get() == 1:
                messagebox.showinfo('Password Generator', 'You have to choose at least two option', parent=self.root)
            else:
                if self.vr1.get() and self.vr2.get() and self.vr3.get() == 1:
                    self.password = ''
                    for y in range(self.pass_len.get()):
                        self.char_type = random.choice(self.combination)
                        self.password += random.choice(self.char_type)
                    self.output_pass.set(self.password)

                if self.vr1.get() and self.vr2.get() == 1:
                    self.passwd = ''
                    for x in range(self.pass_len.get()):
                        self.combi = random.choice(string.ascii_letters + string.punctuation)
                        self.passwd += random.choice(self.combi)
                    self.output_pass.set(self.passwd)

                if self.vr1.get() and self.vr3.get() == 1:
                    self.passwrd = ''
                    for x in range(self.pass_len.get()):
                        self.combin = random.choice(string.ascii_letters + string.digits)
                        self.passwrd += random.choice(self.combin)
                    self.output_pass.set(self.passwrd)

                if self.vr2.get() and self.vr3.get() == 1:
                    self.passd = ''
                    for x in range(self.pass_len.get()):
                        self.combine = random.choice(string.digits + string.punctuation)
                        self.passd += random.choice(self.combine)
                    self.output_pass.set(self.passd)

        else:
            messagebox.showinfo('Password Length', 'Please select minimum 4 length of the password!', parent=self.root)

    def copy1(self):
        if self.output_pass.get() == '':
            messagebox.showerror('Copy','The Password is not generated')

        else:
            self.random_password = self.output_pass.get()
            pyperclip.copy(self.random_password)

            messagebox.showinfo('Copy Password', f'Your password is Copied:-- \n\n=> {self.random_password}',parent=self.root)

    def iExit(self):
        self.Exit = tkinter.messagebox.askyesno('Password Generator', 'Do you want to Exit! ', parent=self.root)
        if self.Exit == True:
            self.root.destroy()

        else:
            return

if __name__=='__main__':
     main()



