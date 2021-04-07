from tkinter import *
import random

array = [[]]
fallados = []
contador = 0
ventana = Tk()
pp = StringVar()
pf = StringVar()
bf = StringVar()
aleatorioB = False
puntaje = 0
arrayNumeros = []

def crearVentana():
    global ventana
    ventana.geometry("850x600+300+60")
    ventana.title("Verbs For Dummies")
    ventana.resizable(width=False, height=False)

def obtenerVerbo():
    global array
    verbo=""
    contadorVerbo = 0
    archivo = open("datos/verbs.txt", "r")
    for c in archivo.readlines():
        for letra in c:
            if not ("|") in letra:
                if ("\n") in letra:
                    array.append([])
                    contadorVerbo += 1
                else:
                    verbo += letra
            else:
                array[contadorVerbo].append(verbo)
                verbo = ""

def jugar():
    global contador,fallados,aleatorioB,puntaje
    puntaje = 0
    imagenFondo = PhotoImage(file="imagenes/fondo.pgm")
    Label(ventana, image=imagenFondo).place(x=0, y=0)

    Label(ventana, text="Verbs For Dummies",
                 font=("Arial", 45)).place(x=170, y=10)

    Label(ventana, text="Selecciona un Nivel:",
                 font=("Arial", 30)).place(x=290, y=110)

    fallados = []
    #contador = 0
    pp.set("")

    if aleatorioB:
        Button(ventana, text=" Modo Random (SI)  ", cursor="hand2",
                          bd=12, background="#00FF22", height=2, command=desactivarModoRandom,
                          font=("Arial", 15)).place(x=20, y=90)
    else:
        Button(ventana, text=" Modo Random (NO) ", cursor="hand2",
               bd=12, background="#F66C75", height=2, command=activarModoRandom,
               font=("Arial", 15)).place(x=20, y=90)


    Button(ventana, text=" NIVEL 1 ",cursor="hand2",bd=12,
                      background="#EB29FF", command=preguntarN1,
                      font=("Arial", 20)).place(x=50, y=200)
    Label(ventana, text=" Sólo tienes que acertar los verbos en Past Participle "
                      , background="#ADF566",
                      font=("Arial", 18)).place(x=230, y=224)

    Button(ventana, text=" NIVEL 2 ", bd=12,cursor="hand2",
                      background="#EB29FF", command=preguntarN2,
                      font=("Arial", 20)).place(x=50, y=340)
    Label(ventana, text=" Tienes que acertar los verbos en Past Participle y "
                    , background="#ADF566",
                    font=("Arial", 18)).place(x=230, y=346)
    Label(ventana, text=" Past Form "
                    , background="#ADF566",
                    font=("Arial", 18)).place(x=230, y=379)

    Button(ventana, text=" NIVEL 3 ",cursor="hand2",
                      bd=12, background="#EB29FF", command=preguntarN3,
                      font=("Arial", 20)).place(x=50, y=480)
    Label(ventana, text=" Tienes que acertar los verbos en Past Participle, "
                    , background="#ADF566",
                    font=("Arial", 18)).place(x=230, y=486)
    Label(ventana, text=" Past Form y Base Form"
                    , background="#ADF566",
                    font=("Arial", 18)).place(x=230, y=519)

    ventana.mainloop()

def obtenerAleatorio():
    global arrayNumeros
    i=0
    while i<len(array):
        numero = random.randint(0, (len(array) - 1))
        if not(numero) in arrayNumeros:
            arrayNumeros.append(numero)
            i += 1
    arrayNumeros.append(3)

def activarModoRandom():
    global contador,fallados,aleatorioB,arrayNumeros
    aleatorioB = True
    arrayNumeros = []
    obtenerAleatorio()
    contador = arrayNumeros[0]
    arrayNumeros.remove(contador)
    jugar()

def desactivarModoRandom():
    global aleatorioB,contador
    aleatorioB = False
    contador = 0
    jugar()

def preguntarN1():
    global puntaje
    record = open("datos/record.txt", "r")
    if puntaje>int(record.read()):
        newRecord = open("datos/record.txt", "w")
        newRecord.write(str(puntaje))
        newRecord.close()
        record.close()
    record = open("datos/record.txt", "r")
    imagenFondo = PhotoImage(file="imagenes/fondo.pgm")
    Label(ventana, image=imagenFondo).place(x=0, y=0)

    imagen = PhotoImage(file="imagenes/"+array[contador][3]+".pgm")
    Label(ventana, image=imagen,relief="groove", borderwidth=15,
                     bg="#920F06").place(x=130, y=240)

    #Verbo en ESPAÑOL
    Label(ventana, text=array[contador][3],
                 font=("Arial", 40)).place(x=320, y=10)

    Label(ventana, text="Past Participle",
                 font=("Arial", 30)).place(x=570, y=90)

    Label(ventana, text="Past Form",
                 font=("Arial", 30)).place(x=320, y=90)
    Label(ventana, text=array[contador][1],
                 font=("Arial", 30)).place(x=360, y=155)

    Label(ventana, text="Base Form",
                 font=("Arial", 30)).place(x=30, y=90)
    Label(ventana, text=array[contador][0],
                 font=("Arial", 30)).place(x=85, y=155)

    Entry(ventana, textvariable=pp,width=9,
                       font=("Arial", 30)).place(x=590, y=155)

    Label(ventana, text="Record",
                   bg="#FFF776", background="#7668F6",
                   font=("Arial", 25)).place(x=10, y=240)
    Label(ventana, text=record.read(),
                   bg="#FFF776", background="#7668F6",
                   font=("Arial", 25)).place(x=10, y=284)


    Label(ventana, text="Puntaje",
                   bg="#FFF776", background="#6897F6",
                   font=("Arial", 25)).place(x=10, y=363)
    Label(ventana, text=str(puntaje),
                   bg="#FFF776", background="#6897F6",
                   font=("Arial", 25)).place(x=10, y=407)


    Label(ventana, text="Vidas",
                   bg="#FFF776",background="#66F5F5",
                   font=("Arial", 25)).place(x=10, y=483)
    Label(ventana, text="♥" *(4 - len(fallados)),
                   bg="#FFF776", background="#66F5F5",
                   font=("Arial", 25)).place(x=10, y=527)

    record.close()
    Button(ventana, text=" Validar ",cursor="hand2",bg="#FFF776",
                              bd=12,activebackground="#12FF32" ,command=validarN1,
                          font=("Arial",25)).place(x=360, y=510)

    ventana.mainloop()

def preguntarN2():
    global puntaje
    record = open("datos/record.txt", "r")
    if puntaje>int(record.read()):
        newRecord = open("datos/record.txt", "w")
        newRecord.write(str(puntaje))
        newRecord.close()
        record.close()
    record = open("datos/record.txt", "r")
    imagenFondo = PhotoImage(file="imagenes/fondo.pgm")
    lbImagenFondo = Label(ventana, image=imagenFondo).place(x=0, y=0)

    imagen = PhotoImage(file="imagenes/"+array[contador][3]+".pgm")
    lbImagen = Label(ventana, image=imagen,relief="groove", borderwidth=15,
                     bg="#920F06").place(x=130, y=240)

    #Verbo en ESPAÑOL
    lbBF = Label(ventana, text=array[contador][3],
                 font=("Arial", 40)).place(x=320, y=10)

    lbPP = Label(ventana, text="Past Participle",
                 font=("Arial", 30)).place(x=570, y=90)
    txtUsuario = Entry(ventana, textvariable=pp, width=9,
                       font=("Arial", 30)).place(x=590, y=155)

    lbPF = Label(ventana, text="Past Form",
                 font=("Arial", 30)).place(x=320, y=90)
    xtUsuario = Entry(ventana, textvariable=pf, width=9,
                      font=("Arial", 30)).place(x=315, y=155)

    lbBF = Label(ventana, text="Base Form",
                 font=("Arial", 30)).place(x=30, y=90)
    lbBF = Label(ventana, text=array[contador][0],
                 font=("Arial", 30)).place(x=85, y=155)

    lbVida = Label(ventana, text="Record",
                   bg="#FFF776", background="#7668F6",
                   font=("Arial", 25)).place(x=10, y=240)
    lbVida = Label(ventana, text=record.read(),
                   bg="#FFF776", background="#7668F6",
                   font=("Arial", 25)).place(x=10, y=284)

    lbVida = Label(ventana, text="Puntaje",
                   bg="#FFF776", background="#6897F6",
                   font=("Arial", 25)).place(x=10, y=363)
    lbVida = Label(ventana, text=str(puntaje),
                   bg="#FFF776", background="#6897F6",
                   font=("Arial", 25)).place(x=10, y=407)

    lbVida = Label(ventana, text="Vidas",
                   bg="#FFF776", background="#66F5F5",
                   font=("Arial", 25)).place(x=10, y=483)
    lbVida = Label(ventana, text="♥" * (4 - len(fallados)),
                   bg="#FFF776", background="#66F5F5",
                   font=("Arial", 25)).place(x=10, y=527)

    record.close()
    Button(ventana, text=" Validar ", cursor="hand2", bg="#FFF776",
           bd=12, activebackground="#12FF32", command=validarN2,
           font=("Arial", 25)).place(x=360, y=510)

    ventana.mainloop()

def preguntarN3():
    global puntaje
    record = open("datos/record.txt", "r")
    if puntaje>int(record.read()):
        newRecord = open("datos/record.txt", "w")
        newRecord.write(str(puntaje))
        newRecord.close()
        record.close()
    record = open("datos/record.txt", "r")
    imagenFondo = PhotoImage(file="imagenes/fondo.pgm")
    Label(ventana, image=imagenFondo).place(x=0, y=0)
    imagen = PhotoImage(file="imagenes/"+array[contador][3]+".pgm")
    Label(ventana, image=imagen,relief="groove", borderwidth=15,
                     bg="#920F06").place(x=130, y=240)

    #Verbo en ESPAÑOL
    Label(ventana, text=array[contador][3],
                 font=("Arial", 40)).place(x=320, y=10)

    Label(ventana, text="Past Participle",
                 font=("Arial", 30)).place(x=570, y=90)
    Entry(ventana, textvariable=pp, width=9,
                       font=("Arial", 30)).place(x=590, y=155)

    Label(ventana, text="Past Form",
                 font=("Arial", 30)).place(x=320, y=90)
    Entry(ventana, textvariable=pf, width=9,
                      font=("Arial", 30)).place(x=315, y=155)

    Label(ventana, text="Base Form",
                 font=("Arial", 30)).place(x=30, y=90)
    Entry(ventana, textvariable=bf, width=9,
                 font=("Arial", 30)).place(x=30, y=155)

    Label(ventana, text="Record",
                   bg="#FFF776", background="#7668F6",
                   font=("Arial", 25)).place(x=10, y=240)
    Label(ventana, text=record.read(),
                   bg="#FFF776", background="#7668F6",
                   font=("Arial", 25)).place(x=10, y=284)

    Label(ventana, text="Puntaje",
                   bg="#FFF776", background="#6897F6",
                   font=("Arial", 25)).place(x=10, y=363)
    Label(ventana, text=str(puntaje),
                   bg="#FFF776", background="#6897F6",
                   font=("Arial", 25)).place(x=10, y=407)

    Label(ventana, text="Vidas",
                   bg="#FFF776", background="#66F5F5",
                   font=("Arial", 25)).place(x=10, y=483)
    Label(ventana, text="♥" * (4 - len(fallados)),
                   bg="#FFF776", background="#66F5F5",
                   font=("Arial", 25)).place(x=10, y=527)
    record.close()
    Button(ventana, text=" Validar ", cursor="hand2", bg="#FFF776",
           bd=12, activebackground="#12FF32", command=validarN3,
           font=("Arial", 25)).place(x=360, y=510)
    ventana.mainloop()

def fallarN1():
    global contador,fallados,puntaje,arrayNumeros
    record = open("datos/record.txt", "r")
    if puntaje>int(record.read()):
        newRecord = open("datos/record.txt", "w")
        newRecord.write(str(puntaje))
        newRecord.close()
        record.close()
    record = open("datos/record.txt", "r")
    imagenFondo = PhotoImage(file="imagenes/fondoError.pgm")
    Label(ventana, image=imagenFondo).place(x=0, y=0)

    imagen = PhotoImage(file="imagenes/" + array[contador][3] + ".pgm")
    Label(ventana, image=imagen,bg="#920F06",
                     relief="groove", borderwidth=15).place(x=130, y=240)

    Label(ventana, text="¡¡HAS FALLADO!!",bg="#F70E0E",
                 font=("Arial", 40)).place(x=220, y=10)

    Label(ventana, text="Past Participle",
                 font=("Arial", 30)).place(x=570, y=90)
    Label(ventana, text=array[contador][2]+"✓",background="#64F937",
                 font=("Arial", 25)).place(x=695, y=170)
    Label(ventana, text=pp.get()+ "✗", background="#F50743",
                 font=("Arial", 25)).place(x=530, y=170)

    Label(ventana, text="Past Form",
                 font=("Arial", 30)).place(x=320, y=90)
    Label(ventana, text=array[contador][1],
                 font=("Arial", 25)).place(x=365, y=170)

    Label(ventana, text="Base Form",
                 font=("Arial", 30)).place(x=30, y=90)
    Label(ventana, text=array[contador][0],
                 font=("Arial", 25)).place(x=95, y=170)
    fallados.append(array[contador])
    pp.set("")

    Label(ventana, text="Record",
                   bg="#FFF776", background="#7668F6",
                   font=("Arial", 25)).place(x=10, y=240)
    Label(ventana, text=record.read(),
                   bg="#FFF776", background="#7668F6",
                   font=("Arial", 25)).place(x=10, y=284)

    Label(ventana, text="Puntaje",
                   bg="#FFF776", background="#6897F6",
                   font=("Arial", 25)).place(x=10, y=363)
    Label(ventana, text=str(puntaje),
                   bg="#FFF776", background="#6897F6",
                   font=("Arial", 25)).place(x=10, y=407)

    Label(ventana, text="Vidas",
                   bg="#FFF776", background="#66F5F5",
                   font=("Arial", 25)).place(x=10, y=483)
    Label(ventana, text="♥" * (4 - len(fallados)),
                   bg="#FFF776", background="#66F5F5",
                   font=("Arial", 25)).place(x=10, y=527)
    record.close()

    if len(fallados)==4:
        Button(ventana, text=" Has perdido ", bd=12, background="#F50743", command=perder,
                          font=("Arial", 25)).place(x=330, y=510)
    else:
        if aleatorioB:
            contador = arrayNumeros[0]
            arrayNumeros.remove(contador)
            if len(arrayNumeros) == 0:
                Button(ventana, text=" Terminar ", bd=12, background="#F50743", command=terminar,
                                  font=("Arial", 25)).place(x=353, y=510)
            else:
                Button(ventana, text=" Continuar ", bd=12, background="#F50743", command=preguntarN1,
                                  font=("Arial", 25)).place(x=353, y=510)
        else:
            contador += 1
            if contador < len(array):
                Button(ventana, text=" Continuar ", bd=12, background="#F50743", command=preguntarN1,
                                  font=("Arial", 25)).place(x=353, y=510)
            else:
                Button(ventana, text=" Terminar ", bd=12, background="#F50743", command=terminar,
                                  font=("Arial", 25)).place(x=353, y=510)

    ventana.mainloop()

def fallarN2():
    global contador,fallados,puntaje,arrayNumeros
    record = open("datos/record.txt", "r")
    if puntaje>int(record.read()):
        newRecord = open("datos/record.txt", "w")
        newRecord.write(str(puntaje))
        newRecord.close()
        record.close()
    record = open("datos/record.txt", "r")
    imagenFondo = PhotoImage(file="imagenes/fondoError.pgm")
    lbImagenFondo = Label(ventana, image=imagenFondo).place(x=0, y=0)

    imagen = PhotoImage(file="imagenes/"+array[contador][3]+".pgm")
    lbImagen = Label(ventana, image=imagen,bg="#920F06",
                     relief="groove", borderwidth=15).place(x=130, y=240)

    lbBF = Label(ventana, text="¡¡HAS FALLADO!!", bg="#F70E0E",
                 font=("Arial", 40)).place(x=220, y=10)


    lbPP = Label(ventana, text="Past Participle",
                 font=("Arial", 30)).place(x=570, y=90)
    if ((pp.get()).lower()==array[contador][2]):
        lbBF = Label(ventana, text=array[contador][2] + "✓", background="#64F937",
                     font=("Arial", 25)).place(x=630, y=170)
    else:
        lbBF = Label(ventana, text=array[contador][2] + "✓", background="#64F937",
                     font=("Arial", 25)).place(x=695, y=170)
        lbBF = Label(ventana, text=pp.get() + "✗", background="#F50743",
                     font=("Arial", 25)).place(x=530, y=170)


    lbPF = Label(ventana, text="Past Form",
                 font=("Arial", 30)).place(x=320, y=90)
    if ((pf.get()).lower()==array[contador][1]):
        lbBF = Label(ventana, text=array[contador][1] + "✓", background="#64F937",
                     font=("Arial", 25)).place(x=360, y=170)
    else:
        lbBF = Label(ventana, text=array[contador][1] + "✓", background="#64F937",
                     font=("Arial", 25)).place(x=415, y=170)
        lbBF = Label(ventana, text=pf.get() + "✗", background="#F50743",
                     font=("Arial", 25)).place(x=290, y=170)



    lbBF = Label(ventana, text="Base Form",
                 font=("Arial", 30)).place(x=30, y=90)
    lbBF = Label(ventana, text=array[contador][0],
                 font=("Arial", 25)).place(x=95, y=170)
    fallados.append(array[contador])
    pf.set("")
    pp.set("")
    lbVida = Label(ventana, text="Record",
                   bg="#FFF776", background="#7668F6",
                   font=("Arial", 25)).place(x=10, y=240)
    lbVida = Label(ventana, text=record.read(),
                   bg="#FFF776", background="#7668F6",
                   font=("Arial", 25)).place(x=10, y=284)

    lbVida = Label(ventana, text="Puntaje",
                   bg="#FFF776", background="#6897F6",
                   font=("Arial", 25)).place(x=10, y=363)
    lbVida = Label(ventana, text=str(puntaje),
                   bg="#FFF776", background="#6897F6",
                   font=("Arial", 25)).place(x=10, y=407)

    lbVida = Label(ventana, text="Vidas",
                   bg="#FFF776", background="#66F5F5",
                   font=("Arial", 25)).place(x=10, y=483)
    lbVida = Label(ventana, text="♥" * (4 - len(fallados)),
                   bg="#FFF776", background="#66F5F5",
                   font=("Arial", 25)).place(x=10, y=527)
    record.close()

    if len(fallados) == 4:
        btnAyuda = Button(ventana, text=" Has perdido ", bd=12, background="#F50743", command=perder,
                          font=("Arial", 25)).place(x=330, y=510)
    else:
        if aleatorioB:
            contador = arrayNumeros[0]
            arrayNumeros.remove(contador)
            if len(arrayNumeros) == 0:
                btnAyuda = Button(ventana, text=" Terminar ", bd=12, background="#F50743", command=terminar,
                                  font=("Arial", 25)).place(x=353, y=510)
            else:
                Button(ventana, text=" Continuar ", bd=12, background="#F50743", command=preguntarN2,
                                  font=("Arial", 25)).place(x=353, y=510)
        else:
            contador += 1
            if contador < len(array):
                Button(ventana, text=" Continuar ", bd=12, background="#F50743", command=preguntarN2,
                                  font=("Arial", 25)).place(x=353, y=510)
            else:
                Button(ventana, text=" Terminar ", bd=12, background="#F50743", command=terminar,
                                  font=("Arial", 25)).place(x=353, y=510)

    ventana.mainloop()

def fallarN3():
    global contador,fallados,puntaje
    record = open("datos/record.txt", "r")
    if puntaje>int(record.read()):
        newRecord = open("datos/record.txt", "w")
        newRecord.write(str(puntaje))
        newRecord.close()
        record.close()
    record = open("datos/record.txt", "r")
    imagenFondo = PhotoImage(file="imagenes/fondoError.pgm")
    Label(ventana, image=imagenFondo).place(x=0, y=0)

    imagen = PhotoImage(file="imagenes/"+array[contador][3]+".pgm")
    Label(ventana, image=imagen,bg="#920F06",
                     relief="groove", borderwidth=15).place(x=130, y=240)

    Label(ventana, text="¡¡HAS FALLADO!!", bg="#F70E0E",
                 font=("Arial", 40)).place(x=220, y=10)


    Label(ventana, text="Past Participle",
                 font=("Arial", 30)).place(x=570, y=90)
    if ((pp.get()).lower()==array[contador][2]):
        Label(ventana, text=array[contador][2] + "✓", background="#64F937",
                     font=("Arial", 20)).place(x=640, y=170)
    else:
        Label(ventana, text=array[contador][2] + "✓", background="#64F937",
                     font=("Arial", 20)).place(x=710, y=170)
        Label(ventana, text=pp.get() + "✗", background="#F50743",
                     font=("Arial", 20)).place(x=565, y=170)


    Label(ventana, text="Past Form",
                 font=("Arial", 30)).place(x=320, y=90)
    if ((pf.get()).lower()==array[contador][1]):
        Label(ventana, text=array[contador][1] + "✓", background="#64F937",
                     font=("Arial", 20)).place(x=360, y=170)
    else:
        Label(ventana, text=array[contador][1] + "✓", background="#64F937",
                     font=("Arial", 20)).place(x=425, y=170)
        Label(ventana, text=pf.get() + "✗", background="#F50743",
                     font=("Arial", 20)).place(x=290, y=170)



    Label(ventana, text="Base Form",
                 font=("Arial", 30)).place(x=30, y=90)
    if ((bf.get()).lower()==array[contador][0]):
        Label(ventana, text=array[contador][0] + "✓", background="#64F937",
                     font=("Arial", 20)).place(x=80, y=170)
    else:
        Label(ventana, text=array[contador][0] + "✓", background="#64F937",
                     font=("Arial", 20)).place(x=150, y=170)
        Label(ventana, text=bf.get() + "✗", background="#F50743",
                     font=("Arial", 20)).place(x=20, y=170)


    fallados.append(array[contador])
    pp.set("")
    pf.set("")
    bf.set("")
    Label(ventana, text="Record",
                   bg="#FFF776", background="#7668F6",
                   font=("Arial", 25)).place(x=10, y=240)
    Label(ventana, text=record.read(),
                   bg="#FFF776", background="#7668F6",
                   font=("Arial", 25)).place(x=10, y=284)

    Label(ventana, text="Puntaje",
                   bg="#FFF776", background="#6897F6",
                   font=("Arial", 25)).place(x=10, y=363)
    Label(ventana, text=str(puntaje),
                   bg="#FFF776", background="#6897F6",
                   font=("Arial", 25)).place(x=10, y=407)

    Label(ventana, text="Vidas",
                   bg="#FFF776", background="#66F5F5",
                   font=("Arial", 25)).place(x=10, y=483)
    Label(ventana, text="♥" * (4 - len(fallados)),
                   bg="#FFF776", background="#66F5F5",
                   font=("Arial", 25)).place(x=10, y=527)
    record.close()
    if len(fallados)==4:
        Button(ventana, text=" Has perdido ", bd=12, background="#F50743", command=perder,
                          font=("Arial", 25)).place(x=330, y=510)
    else:
        if aleatorioB:
            contador = arrayNumeros[0]
            arrayNumeros.remove(contador)
            if len(arrayNumeros) == 0:
                Button(ventana, text=" Terminar ", bd=12, background="#F50743", command=terminar,
                                  font=("Arial", 25)).place(x=353, y=510)
            else:
                Button(ventana, text=" Continuar ", bd=12, background="#F50743", command=preguntarN3,
                                  font=("Arial", 25)).place(x=353, y=510)
        else:
            contador += 1
            if contador < len(array):
                Button(ventana, text=" Continuar ", bd=12, background="#F50743", command=preguntarN3,
                                  font=("Arial", 25)).place(x=353, y=510)
            else:
                Button(ventana, text=" Terminar ", bd=12, background="#F50743", command=terminar,
                                  font=("Arial", 25)).place(x=353, y=510)
    ventana.mainloop()

def perder():
    global contador,fallados,puntaje,aleatorioB

    imagenFondo = PhotoImage(file="imagenes/fondoError.pgm")
    Label(ventana, image=imagenFondo).place(x=0, y=0)

    Label(ventana, text="¡¡Has Perdido!!",bg="#F70E0E",
                 font=("Arial", 35)).place(x=290, y=5)

    lbBF = Label(ventana, text="Tus errores fueron en los siguientes verbos:",bg="#F70E0E",
                 font=("Arial", 30)).place(x=50, y=60)

    lbPP = Label(ventana, text="Verbo:",
                 font=("Arial", 25)).place(x=50, y=135)
    lbPP = Label(ventana, text=fallados[0][3],bg="#87B6FD",
                 font=("Arial", 25)).place(x=50, y=210)
    lbPF = Label(ventana, text=fallados[1][3],bg="#87FDB6",
                 font=("Arial", 25)).place(x=50, y=280)
    lbBF = Label(ventana, text=fallados[2][3],bg="#FD87F1",
                 font=("Arial",25)).place(x=50, y=350)
    lbBF = Label(ventana, text=fallados[3][3],bg="#DEFD87",
                 font=("Arial",25)).place(x=50, y=420)

    lbPP = Label(ventana, text="Base Form:",
                 font=("Arial", 25)).place(x=210, y=135)
    lbPP = Label(ventana, text=fallados[0][0],bg="#87B6FD",
                 font=("Arial", 25)).place(x=210, y=210)
    lbPF = Label(ventana, text=fallados[1][0],bg="#87FDB6",
                 font=("Arial", 25)).place(x=210, y=280)
    lbBF = Label(ventana, text=fallados[2][0],bg="#FD87F1",
                 font=("Arial", 25)).place(x=210, y=350)
    lbBF = Label(ventana, text=fallados[3][0],bg="#DEFD87",
                 font=("Arial", 25)).place(x=210, y=420)

    lbPP = Label(ventana, text="Past Form:",
                 font=("Arial", 25)).place(x=410, y=135)
    lbPP = Label(ventana, text=fallados[0][1],bg="#87B6FD",
                 font=("Arial", 25)).place(x=410, y=210)
    lbPF = Label(ventana, text=fallados[1][1],bg="#87FDB6",
                 font=("Arial", 25)).place(x=410, y=280)
    lbBF = Label(ventana, text=fallados[2][1],bg="#FD87F1",
                 font=("Arial", 25)).place(x=410, y=350)
    lbBF = Label(ventana, text=fallados[3][1],bg="#DEFD87",
                 font=("Arial", 25)).place(x=410, y=420)

    lbPP = Label(ventana, text="Past Participle:",
                 font=("Arial", 25)).place(x=605, y=135)
    lbPP = Label(ventana, text=fallados[0][2],bg="#87B6FD",
                 font=("Arial", 25)).place(x=605, y=210)
    lbPF = Label(ventana, text=fallados[1][2],bg="#87FDB6",
                 font=("Arial", 25)).place(x=605, y=280)
    lbBF = Label(ventana, text=fallados[2][2],bg="#FD87F1",
                 font=("Arial",25)).place(x=605, y=350)
    lbBF = Label(ventana, text=fallados[3][2],bg="#DEFD87",
                 font=("Arial",25)).place(x=605, y=420)

    Label(ventana, text="Puntaje: "+str(puntaje),bg="#F70E0E",
          font=("Arial", 35)).place(x=50, y=520)


    fallados = []
    contador = 0
    aleatorioB = False
    pp.set("")
    btnAyuda = Button(ventana, text=" Volver al inicio ",bd=12,cursor="hand2",
                      background="#F50743",command=jugar,
                      font=("Arial", 25)).place(x=570, y=505)
    ventana.mainloop()

def validarN1():
    global contador,puntaje,arrayNumeros
    if (pp.get()).lower() == array[contador][2]:
        pp.set("")
        puntaje+=1
        if aleatorioB:
            contador = arrayNumeros[0]
            arrayNumeros.remove(contador)
            if len(arrayNumeros)==0:
                terminar()
            else:
                preguntarN1()
        else:
            contador+=1
            if contador<len(array):
                preguntarN1()
            else:
                terminar()
    else:
        fallarN1()

def validarN2():
    global contador,puntaje
    if ((pp.get()).lower() == array[contador][2]) and \
            ((pf.get()).lower() == array[contador][1]):
        pp.set("")
        pf.set("")
        puntaje+=1
        if aleatorioB:
            contador = arrayNumeros[0]
            arrayNumeros.remove(contador)
            if len(arrayNumeros) == 0:
                terminar()
            else:
                preguntarN2()
        else:
            contador += 1
            if contador < len(array):
                preguntarN2()
            else:
                terminar()
    else:
        fallarN2()

def validarN3():
    global contador,puntaje
    if ((pp.get()).lower() == array[contador][2]) \
            and ((pf.get()).lower() == array[contador][1]) \
            and ((bf.get()).lower() == array[contador][0]):
        pp.set("")
        pf.set("")
        bf.set("")
        puntaje+=1
        if aleatorioB:
            contador = arrayNumeros[0]
            arrayNumeros.remove(contador)
            if len(arrayNumeros) == 0:
                terminar()
            else:
                preguntarN3()
        else:
            contador += 1
            if contador < len(array):
                preguntarN3()
            else:
                terminar()
    else:
        fallarN3()

def terminar():
    global contador, fallados, aleatorioB

    imagenFondo = PhotoImage(file="imagenes/fondo.pgm")
    Label(ventana, image=imagenFondo).place(x=0, y=0)

    Label(ventana, text="!!Has Terminado!!",
                 font=("Arial", 40)).place(x=225, y=10)

    if len(fallados)==1:
        Label(ventana, text="Tu único error fué el siguiente verbo:",
                     font=("Arial", 30)).place(x=120, y=80)
    elif len(fallados)>1:
        Label(ventana, text="Tus errores fueron en los siguientes verbos:",
                     font=("Arial", 30)).place(x=55, y=80)
    else:
        Label(ventana, text="Increible, no tuviste ningún error",
                     font=("Arial", 30)).place(x=150, y=180)
    if len(fallados) == 1:
        Label(ventana, text=fallados[0][3],
                     font=("Arial", 45)).place(x=320, y=250)
    if len(fallados) == 2:
        Label(ventana, text=fallados[0][3],
              font=("Arial", 45)).place(x=150, y=250)
        Label(ventana, text=fallados[1][3],
                     font=("Arial", 45)).place(x=470, y=250)
    if len(fallados) == 3:
        Label(ventana, text=fallados[0][3],
              font=("Arial", 45)).place(x=150, y=190)
        Label(ventana, text=fallados[1][3],
              font=("Arial", 45)).place(x=470, y=190)
        Label(ventana, text=fallados[2][3],
                     font=("Arial", 45)).place(x=320, y=280)


    Label(ventana, text="Puntaje: " + str(puntaje),
          font=("Arial", 35)).place(x=320, y=520)

    fallados = []
    contador = 0
    aleatorioB = False
    pp.set("")
    Button(ventana, text=" Volver a Jugar ", bd=12, background="#0022FF", command=jugar,
                      font=("Arial", 30)).place(x=270, y=410)
    ventana.mainloop()

obtenerVerbo()
crearVentana()
jugar()