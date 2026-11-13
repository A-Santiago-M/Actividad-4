import tkinter as tk
from tkinter import ttk, filedialog


class VentanaLeerArchivo:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Leer Archivo")
        self.ventana.geometry("500x400")

        marco = ttk.Frame(self.ventana)
        marco.pack(pady=10)

        ttk.Label(marco, text="Archivo:").grid(row=0, column=0, padx=5)
        self.campo_ruta = ttk.Entry(marco, width=35)
        self.campo_ruta.insert(0, "C:/prueba.txt")
        self.campo_ruta.grid(row=0, column=1)

        ttk.Button(marco, text="Examinar...", command=self.examinar).grid(row=0, column=2, padx=5)

        self.boton = ttk.Button(self.ventana, text="Leer archivo", command=self.leer)
        self.boton.pack(pady=10)

        self.caja_texto = tk.Text(self.ventana, width=58, height=14)
        self.caja_texto.pack(padx=10, pady=5)

    def imprimir(self, texto):
        self.caja_texto.insert(tk.END, texto + "\n")

    def examinar(self):
        ruta = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if ruta:
            self.campo_ruta.delete(0, tk.END)
            self.campo_ruta.insert(0, ruta)

    def leer(self):
        self.caja_texto.delete("1.0", tk.END)
        try:
            with open(self.campo_ruta.get(), "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    self.imprimir(linea.rstrip("\n"))
        except OSError:
            self.imprimir("No se pudo leer el archivo.")

    def iniciar(self):
        self.ventana.mainloop()


app = VentanaLeerArchivo()
app.iniciar()