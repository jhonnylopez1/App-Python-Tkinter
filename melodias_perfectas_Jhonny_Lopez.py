import tkinter as tk
from datetime import datetime

class GestionParticipantes:
    def __init__(self,identificacion,nombre_completo,genero,tecnica_artistica,numero_clases_tomadas):
        self.identificacion=identificacion
        self.nombre_completo=nombre_completo
        self.genero=genero
        self.tecnica_artistica=tecnica_artistica
        self.numero_clases_tomadas=numero_clases_tomadas
        self.fecha=datetime.now()
        self.costo_clase=tecnicas[tecnica_artistica]

    def costo_taller(self):
        costo_total=self.numero_clases_tomadas * self.costo_clase
        return(costo_total)

tecnicas = {
    "Dibujo":70000,
    "Pintura":85000,
    "Escritura":100000,
    "Fotografia":90000,
    "Grabado":75000
}

ensayo=GestionParticipantes(1026147279,"Jhonny Lopez","Masculino","Fotografia",2)
total=ensayo.costo_taller()
print(total)

#Validar Contraseña
def validar_password():
    if password.get()=="3971":
        ventana.destroy()
        registrar_datos()
    else: print("incorrecto")

#Registrar Datos
def registrar_datos():
    ventana_registrar_datos = tk.Tk()
    ventana_registrar_datos.title("Registro de Datos del Estudiante")
    ventana_registrar_datos.geometry("500x300")

    tk.Label(ventana_registrar_datos,text="Identificacion").pack(pady=5)
    identificacion_entry=tk.Entry(ventana_registrar_datos)
    identificacion_entry.pack(pady=2)

    tk.Label(ventana_registrar_datos,text="Nombre Completo").pack(pady=5)
    nombre_entry=tk.Entry(ventana_registrar_datos)
    nombre_entry.pack(pady=2)

    tk.Label(ventana_registrar_datos, text="Genero").pack()
    genero= tk.StringVar(value="Seleccione")
    tk.OptionMenu(ventana_registrar_datos, genero, "Masculino", "Femenino").pack()

    # genero=tk.StringVar(value=" ")
    # tk.Label(ventana_registrar_datos,text="Genero").pack()
    # tk.Radiobutton(ventana_registrar_datos,text="Masculino",variable=genero,value="Masculino").pack()
    # tk.Radiobutton(ventana_registrar_datos,text="Femenino",variable=genero,value="Femenino").pack()


    ventana_registrar_datos.mainloop()

#crear la ventana login
ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("400x300")

#LOGIN
nombre_app=tk.Label(ventana,text="Aplicacion:\nGestion de Participantes")
#agregar un widget(etiqueta)
nombre_app.pack(pady=10)

nombre_autor=tk.Label(ventana,text="Autor:\nJhonny Andres Lopez")
#agregar un widget(etiqueta)
nombre_autor.pack(pady=10)

label_password=tk.Label(ventana,text="Contraseña:")
#agregar un widget(etiqueta)
label_password.pack(pady=10)

password=tk.Entry(ventana, show="*")
password.pack(pady=5)

boton_login=tk.Button(ventana,text="Ingresar",command=validar_password)
boton_login.pack(pady=5)

#Iniciar el bucle principal
ventana.mainloop()




# self.identificacion=identificacion
#         self.nombre_completo=nombre_completo
#         self.genero=genero
#         self.tecnica_artistica=tecnica_artistica
#         self.numero_clases_tomadas=numero_clases_tomadas
#         self.fecha=datetime.now()
#         self.costo_clase=tecnicas[tecnica_artistica]