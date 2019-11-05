from tkinter import *
class Application(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.grid()
        self.create_boton()
        self.create_boton2()
        self.create_Label()
#Boton
    def create_boton(self):
        self.myButton = Button(self, text='Etiqueta Boton')
        self.myButton.grid(row=2,column=1)
#Boton2
    def create_boton2(self):
        self.myButton2 = Button(self, text='Otro Boton')
        self.myButton2.grid(row=1,column=1)
#Creamos las etiquetas
    def create_Label(self):
        self.myLabel = Label(self, text='Usuario:')
        self.myLabel.grid(row=0,column=0)


#creamos ventana
ventana = Tk()
ventana.title('Titulo  de la Ventana')
#geometry("ancho x alto + posX + posY")
ventana.geometry('600x200')

app = Application(ventana)
app.mainloop()
