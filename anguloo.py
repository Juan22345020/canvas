from tkinter import * 

BASE=460
ALTURA=220
RADIO=50
ventana_principal=Tk()
ventana_principal.geometry("500x500")
ventana_principal.title("Graficas en 2D,Lineas rectas")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="black")

frame_graficacion=Frame(ventana_principal)
frame_graficacion.config(bg="white",width=480 , height=240)
frame_graficacion.place(x=10, y=10)

c=Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="pink")
c.place(x=10, y=10)
#funcion para modificar arco
def modificar_arco(angulo):
    c.itemconfig(arco,extent=angulo)

#arco
arco=c.create_arc(BASE/2-RADIO,ALTURA/2-RADIO,BASE/2+RADIO,ALTURA/2+RADIO,start=0,extent=0, fill="blue")
#frame de controles
frame_controles=Frame(ventana_principal)
frame_controles.config(bg="green",width=480, height=230)
frame_controles.place(x=10,y=260)
#Barra de deslisamiento
barra_deslizamiento=Scale(frame_controles, label="Angulo", from_=0, to= 360, orient="horizontal", length=455,tickinterval=90,command=modificar_arco)
barra_deslizamiento.place(x=10,y=10)



ventana_principal.mainloop()