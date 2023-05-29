from tkinter import * 
from tkinter import messagebox
import random
BASE=460
ALTURA=220
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
#LINEAS
#linea1=c.create_line(10,10, BASE-10,10, fill="red",width=5)
#linea2=c.create_line(BASE-10,10,BASE-10, ALTURA-10, fill="red",width=5)
#linea3=c.create_line( BASE-10, ALTURA-10,10,ALTURA-10,fill="red",width=5)
#linea4=c.create_line(10, ALTURA-10,10,10, fill="red",width=5)
#linea5=c.create_line(200,20, BASE-200,20, fill="fuchsia",width=5)
#linea6=c.create_line(BASE-200,20,BASE-200, ALTURA-150, fill="fuchsia",width=5)
#linea7=c.create_line(200, ALTURA-200,200,70, fill="fuchsia",width=5)
#linea8=c.create_line(312,70, BASE-201,70, fill="fuchsia",width=5)
#linea9=c.create_line(201,70, BASE-312,70, fill="fuchsia",width=5)
#linea10=c.create_line(312, ALTURA-150,312,130, fill="fuchsia",width=5)
#linea11=c.create_line(149, ALTURA-150,149,130, fill="fuchsia",width=5)
#linea12=c.create_line(201,130, BASE-312,130, fill="fuchsia",width=5)
#linea13=c.create_line(312,130, BASE-201,130, fill="fuchsia",width=5)
#linea14=c.create_line(BASE-200,130,BASE-200, ALTURA-30, fill="fuchsia",width=5)
#linea15=c.create_line(200,189, BASE-200,189, fill="fuchsia",width=5)
#linea16=c.create_line(BASE-260,130,BASE-260, ALTURA-30, fill="fuchsia",width=5)

#ventana_principallinea1=c.create_line(10,10, BASE-10,10, fill="red")
#linea1=c.create_line(10,10, BASE-10,10, fill="red")
#TEXTOS
#texto1=c.create_text(BASE/2, ALTURA/2, text= "Sistemas UIS Socorro",anchor= "center",
#font=("Arial","20","bold"),fill="fuchsia",activefill="white")
#CUADROS Y RECTANGULOS
#rect1=c.create_rectangle(10,20, 120,120, fill="fuchsia", outline="blue",width=3)
#POLIGONOS
#poligono1=c.create_polygon(0,0,BASE/2,ALTURA/2,BASE,0, fill="fuchsia",outline="blue")
#poligono2=c.create_polygon(0,ALTURA,BASE/2,ALTURA/2,BASE,ALTURA ,fill="yellow",outline="blue")
#poligono3=c.create_polygon(0,0,BASE/2,ALTURA/2,0,ALTURA,fill="green",outline="blue")
#poligono3=c.create_polygon(0,0,BASE/2,ALTURA/2,0,ALTURA,fill="green",outline="blue")

#rombo1=c.create_polygon(BASE/4,0,BASE/2,ALTURA/2,3*BASE/4,0, fill="fuchsia",outline="blue")
#rombo1=c.create_polygon(BASE/4,0,0,ALTURA/4,BASE/4,ALTURA/2,BASE/2,ALTURA/4, fill="fuchsia",outline="blue")
#rombo2=c.create_polygon(BASE/4,ALTURA/2,0,3*ALTURA/4,BASE/4,ALTURA,BASE/2,3*ALTURA/4, fill="fuchsia",outline="blue")
#rombo3=c.create_polygon(3*BASE/4,0,BASE,ALTURA/4,3*BASE/4,ALTURA/2,BASE/2,ALTURA/4, fill="fuchsia",outline="blue")
#rombo4=c.create_polygon(ALTURA/2,3*BASE/4,3*ALTURA/4,ALTURA/2,3*BASE/4,ALTURA/2,3*BASE/4,BASE/2,3*ALTURA/4, fill="fuchsia",outline="blue")
# CIRCULO
#elipse1=c.create_oval(BASE/2,ALTURA/2,BASE,ALTURA,fill="orange")
#elipse1=c.create_oval(BASE/2-100,ALTURA/2-100,BASE/2 +100,ALTURA/2+100, fill="orange")
#arcos
#arc1=c.create_arc(BASE/2-100,ALTURA/2-100,BASE/2 +100,ALTURA/2+100,start=45,extent=45,fill="black")#
#arc2=c.create_arc(BASE/4-30,ALTURA/4-30,BASE/4 +30,ALTURA/4+30,start=45,extent=280,fill="black")
#arc3=c.create_arc(BASE/4-30,3*ALTURA/4-30,BASE/4 +30,3*ALTURA/4+30,start=45,extent=280,fill="black")
#arc4=c.create_arc(3*BASE/4-30,ALTURA/4-30,3*BASE/4 +30,ALTURA/4+30,start=45,extent=280,fill="black")
#for i in range (100):
#    x=random.randint(0, BASE-20)
#    y=random.randint(0,ALTURA-2)
#    #circulo=c.create_oval(x,y,x+20,y+20, fill="red")
#   color="#"
#    for caracter in range(6):
#        color=color+random.choice("0123456789ABCDEF")
#    circulo=c.create_oval(x,y,x+20,y+20, fill=color)
ventana_principal.mainloop()