from tkinter import *
BASE=460
ALTURA=220
RADIO=50

# funcion para modificar arco
def modificar_arco(angulo):
    angulo2=int(angulo)+90
    angulo3=int(angulo)+180
    angulo4=int(angulo)+270
    c.itemconfig(arco,start=angulo )
    c.itemconfig(arco2,start=angulo2)
    c.itemconfig(arco3,start=angulo3)
    c.itemconfig(arco4,start=angulo4)


ventana_principal = Tk()
ventana_principal.title("Graficas 2d - lineas rectas")
ventana_principal.geometry("500x500")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="white")

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=480, height=240)
frame_graficacion.place(x=10, y=10)

# creacion canvas
c= Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10,y=10)

poligono3=c.create_polygon(BASE/2,ALTURA/2,BASE*2/5,ALTURA,BASE*3/5,ALTURA,fill="white", outline="black")

#arco
arco=c.create_arc(BASE/2-RADIO,ALTURA/2-RADIO,BASE/2+RADIO,ALTURA/2+RADIO,start=0,extent=45, fill="blue")
arco2=c.create_arc(BASE/2-RADIO,ALTURA/2-RADIO,BASE/2+RADIO,ALTURA/2+RADIO,start=90,extent=45, fill="red")
arco3=c.create_arc(BASE/2-RADIO,ALTURA/2-RADIO,BASE/2+RADIO,ALTURA/2+RADIO,start=180,extent=45, fill="yellow")
arco4=c.create_arc(BASE/2-RADIO,ALTURA/2-RADIO,BASE/2+RADIO,ALTURA/2+RADIO,start=270,extent=45, fill="purple")

#frame de controles 
frame_controles=Frame(ventana_principal)
frame_controles.config(bg="green",width=480,height=230)
frame_controles.place(x=10,y=260)

# barra de deslizamiento
barra_deslizamiento=Scale(frame_controles ,label="Angulo",from_=0,to=360,orient="horizontal",length=460,tickinterval=45,command=modificar_arco)
barra_deslizamiento.place(x=10,y=10)    

ventana_principal.mainloop()