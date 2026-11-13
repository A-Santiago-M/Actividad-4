import math
import tkinter as tk
from tkinter import ttk


class CalculosNumericos:
    @staticmethod
    def calcular_logaritmo_neperiano(valor):
        if valor <= 0:
            raise ArithmeticError("El valor debe ser un numero positivo")
        return math.log(valor)

    @staticmethod
    def calcular_raiz_cuadrada(valor):
        if valor < 0:
            raise ArithmeticError("El valor debe ser un numero positivo")
        return math.sqrt(valor)


class VentanaCalculos:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculos Numericos")
        self.ventana.geometry("450x330")

        marco = ttk.Frame(self.ventana)
        marco.pack(pady=10)

        ttk.Label(marco, text="Valor numerico:").grid(row=0, column=0, padx=5)
        self.campo_valor = ttk.Entry(marco, width=20)
        self.campo_valor.grid(row=0, column=1)

        self.boton = ttk.Button(self.ventana, text="Calcular", command=self.calcular)
        self.boton.pack(pady=10)

        self.caja_texto = tk.Text(self.ventana, width=50, height=10)
        self.caja_texto.pack(padx=10, pady=5)

    def imprimir(self, texto):
        self.caja_texto.insert(tk.END, texto + "\n")

    def calcular(self):
        self.caja_texto.delete("1.0", tk.END)

        try:
            valor = float(self.campo_valor.get())
            
        except ValueError:
            self.imprimir("El valor debe ser numerico")
            return

        try:
            resultado = CalculosNumericos.calcular_logaritmo_neperiano(valor)
            self.imprimir(f"Logaritmo neperiano = {resultado}")
            
        except ArithmeticError:
            self.imprimir("El valor debe ser un numero positivo para calcular el logaritmo")

        try:
            resultado = CalculosNumericos.calcular_raiz_cuadrada(valor)
            self.imprimir(f"Raiz cuadrada = {resultado}")
            
        except ArithmeticError:
            self.imprimir("El valor debe ser un numero positivo para calcular la raíz cuadrada")

    def iniciar(self):
        self.ventana.mainloop()


app = VentanaCalculos()
app.iniciar()