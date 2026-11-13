import tkinter as tk
from tkinter import ttk


class Vendedor:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = 0

    def verificar_edad(self, edad):
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        if 0 <= edad < 120:
            self.edad = edad
        else:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")


class VentanaVendedor:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Vendedor")
        self.ventana.geometry("450x400")

        marco = ttk.Frame(self.ventana)
        marco.pack(pady=10)

        ttk.Label(marco, text="Nombre:").grid(row=0, column=0, padx=5, pady=3, sticky="e")
        self.campo_nombre = ttk.Entry(marco, width=25)
        self.campo_nombre.grid(row=0, column=1)

        ttk.Label(marco, text="Apellidos:").grid(row=1, column=0, padx=5, pady=3, sticky="e")
        self.campo_apellidos = ttk.Entry(marco, width=25)
        self.campo_apellidos.grid(row=1, column=1)

        ttk.Label(marco, text="Edad:").grid(row=2, column=0, padx=5, pady=3, sticky="e")
        self.campo_edad = ttk.Entry(marco, width=25)
        self.campo_edad.grid(row=2, column=1)

        self.boton = ttk.Button(self.ventana, text="Verificar edad", command=self.verificar)
        self.boton.pack(pady=10)

        self.caja_texto = tk.Text(self.ventana, width=45, height=10)
        self.caja_texto.pack(padx=10, pady=5)

    def imprimir(self, texto):
        self.caja_texto.insert(tk.END, texto + "\n")

    def verificar(self):
        self.caja_texto.delete("1.0", tk.END)
        vendedor = Vendedor(self.campo_nombre.get(), self.campo_apellidos.get())
        
        try:
            edad = int(self.campo_edad.get())
            vendedor.verificar_edad(edad)
            self.imprimir(f"Nombre del vendedor = {vendedor.nombre}")
            self.imprimir(f"Apellidos del vendedor = {vendedor.apellidos}")
            self.imprimir(f"Edad del vendedor = {vendedor.edad}")
            
        except ValueError as e:
            self.imprimir(f"Error: {e}")

    def iniciar(self):
        self.ventana.mainloop()


app = VentanaVendedor()
app.iniciar()