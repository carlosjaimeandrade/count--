from tkinter import *
from tkinter  import ttk
from ttkthemes import *
import threading 
from Number import Number

class Count:
    def __init__(self):
        if __name__ == '__main__':
            self.main()

    def main(self):
        window = ThemedTk(theme='Black')
        window.title('Count+-')
        window.resizable(0, 0)
        window.geometry("300x400+500+25")
        window.iconbitmap("icon/logoF.ico")
        window.config(background="#ffffff")

        countFrame = Frame(window, background="#ffffff")
        countFrame.pack(fill="x",pady=25)
        
        nameLabel = Label(countFrame, text="Contador", font="Gadugi 10", background="#ffffff")
        nameLabel.pack(pady=30)

        numberLabel = Label(countFrame, text=Number.getRegister(self), font="Gadugi 40", background="#ffffff")
        numberLabel.pack()

        buttonFrame = Frame(window, background="#ffffff" )
        buttonFrame.pack(pady=55)

        buttonAdd = Button(buttonFrame, command=lambda: threading.Thread(target=Number().add(numberLabel)).start(), text="Adicionar",bd=0, width=10, height=2, background="#0E5369", fg="#ffffff")
        buttonAdd.pack(side="left",padx=2)

        buttonRemove = Button(buttonFrame, command=lambda: threading.Thread(target=Number().remove(numberLabel)).start(), text="Remover", bd=0, width=10, height=2, background="#CC5354", fg="#ffffff")
        buttonRemove.pack(side="left",padx=2)
        
        buttonZerar = Button(buttonFrame, command=lambda: threading.Thread(target=Number().returnDefault(numberLabel)).start() , text="Redefinir", bd=0, width=10, height=2, fg="black")
        buttonZerar.pack(side="left",padx=2)

        developerFrame = Frame(window, background="#ffffff")
        developerFrame.pack(fill="x")

        developerLabel = Label(developerFrame, text="Desenvolvido por Carlos Jaime", font="Gadugi 8", background="#ffffff")
        developerLabel.pack() 

        developerSiteLabel = Label(developerFrame, text="reqsolution.com.br", font="Gadugi 8", background="#ffffff")
        developerSiteLabel.pack() 

        mainloop()

Count()