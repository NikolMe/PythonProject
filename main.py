from tkinter import Tk, Frame, Text, BOTH, X, N, LEFT, Menu, Checkbutton, BooleanVar
from tkinter.ttk import Button, Style, Label, Entry
 
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Grafector")

        self.pack(fill=BOTH, expand=True)
        
        self.var = BooleanVar()
 
        cb = Checkbutton(self, text="Орієнтований граф", variable=self.var, command=self.onClick)
        cb.select()
        cb.place(x=50, y=50)
 
        menubar = Menu(self.master)   #файл меню
        self.master.config(menu=menubar)
 
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Допомога")
        fileMenu.add_command(label="Зберегти")
        fileMenu.add_command(label="Довідка")
        menubar.add_cascade(label="Меню", menu=fileMenu)
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self)   #хз зачем именно это тут
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Введіть ребра графа:", width=20)   #это тоже тут надо
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(frame1)        #ввод ребёр 
        entry1.pack(fill=X, padx=5, expand=True)

        button1 = Button(self, text="Розв'язати")    #кнопка пока еще не работает
        button1.pack(padx=5, pady=5)

    def onClick(self): #функция для чекбокса
        if self.var.get():
            self.master.title("Флажки")
        else:
            self.master.title("")
    
        
def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()  
 
if __name__ == '__main__':
    main()