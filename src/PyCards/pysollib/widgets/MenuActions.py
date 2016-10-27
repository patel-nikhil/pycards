import Tkinter

#####   File menu commands #####

def startNew():
    pass


def listRecent():
    pass


def listGames():
    pass


def listFavorite():
    pass


def addFavorite():
    pass


def delFavorite():
    pass


def saveGame():
    pass


def loadGame():
    pass


def quitGame():
    pass


def showGames():
    pass

#####   End file commands   #####


#####   Help commands   #####

def showContents():
    pass

def showGuide():
    pass

def showRules():
    pass

def showLicense():
    window = Tkinter.Toplevel(width=400, height=500, padx=10, pady=30, background="darkblue")
    window.canvas = Tkinter.Canvas(window, background="darkblue")
    window.canvas.pack()

    window.title("License")
    scroll = Tkinter.Scrollbar(window.canvas, takefocus=1)
    scroll.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
    file = open("LICENSE","r")
    licenses = file.read()
    file.close()
    window.msg = Tkinter.Text(window.canvas, background="darkgray", relief="raised", pady=10)
    window.msg.insert(Tkinter.END, licenses)
    window.msg.tag_add("indent", 0.0, Tkinter.END)
    window.msg.tag_configure("indent", lmargin1=20, lmargin2=20, background="darkgray")
    window.msg.configure(state=Tkinter.DISABLED)
    window.msg.pack()
    scroll.config(command=window.msg.yview)
    window.msg.config(yscrollcommand=scroll.set)
    window.update()

def showInfo():
    window = Tkinter.Toplevel(width=400, height=400)
    window.title("About")