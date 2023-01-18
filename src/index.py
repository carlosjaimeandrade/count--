from tkinter import *
from tkinter  import ttk
from ttkthemes import *

class Count:
    def __init__(self):
        if __name__ == '__main__':
            self.main()

    def main(self):
        window = ThemedTk(theme='Black')
        window.title('Count+-')
        #self.window.resizable(0, 0)
        window.geometry("300x400+500+25")
        window.iconbitmap(".icon/logoF.ico")
        window.config(background="#ffffff")

        countFrame = Frame(window, background="#ffffff")
        countFrame.pack(fill="x",pady=40)
        
        nameLabel = Label(countFrame, text="Contador", font="Gadugi 10", background="#ffffff")
        nameLabel.pack(pady=30)

        self.numberLabel = Label(countFrame, text="0", font="Gadugi 40", background="#ffffff")
        self.numberLabel.pack()

        buttonFrame = Frame(window, background="#ffffff" )
        buttonFrame.pack(pady=55)

        buttonAdd = Button(buttonFrame, text="Adicionar",bd=0, width=18, height=2, background="#0E5369", fg="#ffffff")
        buttonAdd.pack(side="left",padx=2)

        buttonRemove = Button(buttonFrame, text="Remover", bd=0, width=18, height=2, background="#CC5354", fg="#ffffff")
        buttonRemove.pack(side="left",padx=2)

        developerFrame = Frame(window, background="#ffffff")
        developerFrame.pack(fill="x")

        developerLabel = Label(developerFrame, text="Desenvolvido por Carlos Jaime", font="Gadugi 8", background="#ffffff")
        developerLabel.pack() 

        mainloop()

Count()