import tkinter as libgorsel #
from tkinter import ttk as gorselNesne

import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("hesap makinesi- hüsamettin")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_779=tk.Button(root)
        GButton_779["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_779["font"] = ft
        GButton_779["fg"] = "#000000"
        GButton_779["justify"] = "center"
        GButton_779["text"] = "+"
        GButton_779.place(x=90,y=400,width=30,height=25)
        GButton_779["command"] = self.GButton_779_command

        GButton_304=tk.Button(root)
        GButton_304["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_304["font"] = ft
        GButton_304["fg"] = "#000000"
        GButton_304["justify"] = "center"
        GButton_304["text"] = "-"
        GButton_304.place(x=180,y=400,width=30,height=25)
        GButton_304["command"] = self.GButton_304_command

        GButton_428=tk.Button(root)
        GButton_428["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_428["font"] = ft
        GButton_428["fg"] = "#000000"
        GButton_428["justify"] = "center"
        GButton_428["text"] = "*"
        GButton_428.place(x=270,y=400,width=30,height=25)
        GButton_428["command"] = self.GButton_428_command

        GButton_931=tk.Button(root)
        GButton_931["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_931["font"] = ft
        GButton_931["fg"] = "#000000"
        GButton_931["justify"] = "center"
        GButton_931["text"] = "/"
        GButton_931.place(x=360,y=400,width=30,height=25)
        GButton_931["command"] = self.GButton_931_command

        GLineEdit_185=tk.Entry(root)
        GLineEdit_185["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_185["font"] = ft
        GLineEdit_185["fg"] = "#333333"
        GLineEdit_185["justify"] = "center"
        GLineEdit_185["text"] = "Entry1"
        GLineEdit_185.place(x=140,y=240,width=70,height=25)

        GLineEdit_392=tk.Entry(root)
        GLineEdit_392["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_392["font"] = ft
        GLineEdit_392["fg"] = "#333333"
        GLineEdit_392["justify"] = "center"
        GLineEdit_392["text"] = "Entry2"
        GLineEdit_392.place(x=230,y=240,width=70,height=25)

        GLineEdit_236=tk.Entry(root)
        GLineEdit_236["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_236["font"] = ft
        GLineEdit_236["fg"] = "#333333"
        GLineEdit_236["justify"] = "center"
        GLineEdit_236["text"] = "Entry"
        GLineEdit_236.place(x=330,y=240,width=70,height=25)

        GLabel_700=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_700["font"] = ft
        GLabel_700["fg"] = "#333333"
        GLabel_700["justify"] = "center"
        GLabel_700["text"] = "rakam1"
        GLabel_700.place(x=130,y=200,width=70,height=25)

        GLabel_340=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_340["font"] = ft
        GLabel_340["fg"] = "#333333"
        GLabel_340["justify"] = "center"
        GLabel_340["text"] = "rakam2"
        GLabel_340.place(x=220,y=200,width=70,height=25)

        GLabel_395=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_395["font"] = ft
        GLabel_395["fg"] = "#333333"
        GLabel_395["justify"] = "center"
        GLabel_395["text"] = "sonuc"
        GLabel_395.place(x=320,y=200,width=70,height=25)

    def GButton_779_command(self):
        print("buton1e basıldı")


    def GButton_304_command(self):
        print("buton2 ye basıldı")


    def GButton_428_command(self):
        print("buton3 e basıldı")


    def GButton_931_command(self):
        print("buton4 e basıldı")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    textBoxYazilanlar1 = tk.StringVar()
    textBoxYazilanlar2 = tk.StringVar()
    textBoxYazilanlar3 = tk.StringVar()
    root.mainloop()


