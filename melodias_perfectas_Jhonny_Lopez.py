import tkinter as tk
from datetime import datetime
from tkinter import messagebox

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
    ventana_registrar_datos.geometry("300x500")

    datos = None

    tk.Label(ventana_registrar_datos,text="Identificacion").pack(pady=5)
    identificacion_entry=tk.Entry(ventana_registrar_datos)
    identificacion_entry.pack(pady=2)

    tk.Label(ventana_registrar_datos,text="Nombre Completo").pack(pady=5)
    nombre_entry=tk.Entry(ventana_registrar_datos)
    nombre_entry.pack(pady=2)

    tk.Label(ventana_registrar_datos, text="Genero").pack()
    genero= tk.StringVar(value="Seleccione")
    tk.OptionMenu(ventana_registrar_datos, genero, "Masculino", "Femenino").pack()

    
    tecnica_artistica =tk.StringVar(value="Seleccione")
    tk.Label(ventana_registrar_datos,text="Tecnica Artistica").pack()

    def actualizar_costo(tecnica_seleccionada):
        costo=tecnicas[tecnica_seleccionada]
        costo_clase.config(text=f"{costo}")
    
    menu_tecnica_artistica=tk.OptionMenu(
        ventana_registrar_datos,tecnica_artistica,"Dibujo","Pintura","Escritura","Fotografia","Grabado",command=actualizar_costo)
    menu_tecnica_artistica.pack(pady=2)
    
    tk.Label(ventana_registrar_datos,text="Costo clase").pack()
    costo_clase=tk.Label(ventana_registrar_datos,text="$0")
    costo_clase.pack(pady=2)

    tk.Label(ventana_registrar_datos,text="Numero de Clases").pack(pady=5)
    numero_clases_entry=tk.Entry(ventana_registrar_datos)
    numero_clases_entry.pack(pady=2)

    def registrar_info():
        try:
            nonlocal datos
            datos=GestionParticipantes(
                int(identificacion_entry.get()),
                nombre_entry.get(),
                genero.get(),
                tecnica_artistica.get(),
                int(numero_clases_entry.get())
            )
            messagebox.showinfo("Aprobado", "Registro guardado correctamente")
        except:
            messagebox.showerror("Error", "Datos invalidos")
    
    def mostrar_info():
        if datos is None:
            messagebox.showerror("Error", "Debe guardar primero")
            return
        ventana_reporte = tk.Toplevel()
        ventana_reporte.title("Reporte")
        ventana_reporte.geometry("300x500")
        
        total_info= f"""
        Nombre:{datos.nombre_completo}
        ID:{datos.identificacion}
        Genero:{datos.genero}
        Tecnica:{datos.tecnica_artistica}
        Clases:{datos.numero_clases_tomadas}
        Fecha de Registro:{datos.fecha}
        Costo por clase:{datos.costo_clase}
        Total a pagar:{datos.costo_taller()}"""

        tk.Label(ventana_reporte,text=f"{total_info}").pack(pady=10,padx=10)
    
    def salir():
        opcion = messagebox.askyesno(
            "Confirmar",
            "Desea salir del programa?"
        )
        if opcion:
            ventana_registrar_datos.destroy()

    boton_registrar=tk.Button(ventana_registrar_datos,text="Guardar",command=registrar_info)
    boton_registrar.pack(pady=5)

    boton_reporte=tk.Button(ventana_registrar_datos,text="Calcular Costo/Mostrar Reporte",command=mostrar_info)
    boton_reporte.pack(pady=5)

    boton_salir=tk.Button(ventana_registrar_datos,text="Salir",command=salir)
    boton_salir.pack(pady=5)

    ventana_registrar_datos.mainloop()

    def mostrar_info():
        if datos is None:
            messagebox.showerror("Error", "Debe guardar primero")
            return
        ventana_reporte = tk.Toplevel()
        ventana_reporte.title("Reporte")
        ventana_reporte.geometry("300x500")
        
        total_info= f"""
        Nombre:{datos.nombre_completo}
        ID:{datos.identificacion}
        Genero:{datos.genero}
        Tecnica:{datos.tecnica_artistica}
        Clases:{datos.numero_clases_tomadas}
        Fecha de Registro:{datos.fecha}
        Costo por clase:{datos.costo_clase}
        Total a pagar:{datos.costo_taller()}"""

        tk.Label(ventana_reporte,text=f"{total_info}").pack(pady=10,padx=10)



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






