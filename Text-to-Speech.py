from tkinter import *
from tkinter import font
from gtts import gTTS
from playsound import playsound

#Inicialização da GUI feita em Tkinter.

root = Tk()
root.geometry('350x350')
root.resizable(0, 0)
root.config(bg = 'black')
root.title("Leleo's Tabajara - Síntese de fala")



#Cabeçario

Label(root, text = "Síntese de fala", font = "Arial 20 bold", bg = 'white smoke').pack()
Label(root, text = "Leleo's Tabajara - Síntese de fala ", font = "Arial 15 bold", bg = "White smoke").pack(side = BOTTOM)


#Label 

Label(root, text = "Digite seu texto. ", font = "Arial 15 bold", bg = 'white smoke').pack(side = BOTTOM)


#Variável do Texto

Msg = StringVar()

#Entrada

entry_field = Entry(root, textvariable = Msg, width='50')
entry_field.place(x=20, y=100)


# Definir a função

def Text_To_Speech():
    Message = entry_field.get()
    speech = gTTS(text=Message)
    speech.save('LeleosTabajara.mp3')
    playsound('LeleosTabajara.mp3')
def Exit():
    root.destroy()
def Reset():
    Msg.set("")


#Butão hehe

#Button
Button(root, text = "PLAY" , font = 'arial 15 bold', command = Text_To_Speech, width = 4).place(x = 25, y = 140)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'OrangeRed1').place(x = 100,y = 140)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset).place(x = 175 , y = 140)

#Loop para rodar o programa

root.mainloop()

