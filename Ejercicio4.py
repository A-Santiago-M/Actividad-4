import tkinter as tk
from tkinter import ttk


class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos


class EquipoMaratonProgramacion:
    MAX_INTEGRANTES = 3

    def __init__(self, nombre_equipo, universidad, lenguaje_programacion):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.programadores = []

    def esta_lleno(self):
        return len(self.programadores) == self.MAX_INTEGRANTES

    def anadir(self, programador):
        if self.esta_lleno():
            raise Exception("El equipo esta completo. No se pudo agregar programador.")
        self.programadores.append(programador)

    @staticmethod
    def validar_campo(campo):
        for c in campo:
            if c.isdigit():
                raise Exception("El nombre no puede tener digitos.")
        if len(campo) >= 20:
            raise Exception("La longitud no debe ser superior a 20 caracteres.")


class VentanaEquipo:
    def __init__(self):
        self.equipo = None

        self.ventana = tk.Tk()
        self.ventana.title("Maraton de Programacion")
        self.ventana.geometry("480x560")

        # --- Datos del equipo ---
        marco_equipo = ttk.LabelFrame(self.ventana, text="Datos del equipo")
        marco_equipo.pack(padx=10, pady=8, fill="x")

        ttk.Label(marco_equipo, text="Nombre del equipo:").grid(row=0, column=0, padx=5, pady=3, sticky="e")
        self.campo_equipo = ttk.Entry(marco_equipo, width=25)
        self.campo_equipo.grid(row=0, column=1)

        ttk.Label(marco_equipo, text="Universidad:").grid(row=1, column=0, padx=5, pady=3, sticky="e")
        self.campo_universidad = ttk.Entry(marco_equipo, width=25)
        self.campo_universidad.grid(row=1, column=1)

        ttk.Label(marco_equipo, text="Lenguaje:").grid(row=2, column=0, padx=5, pady=3, sticky="e")
        self.campo_lenguaje = ttk.Entry(marco_equipo, width=25)
        self.campo_lenguaje.grid(row=2, column=1)

        self.boton_crear = ttk.Button(marco_equipo, text="Crear equipo", command=self.crear_equipo)
        self.boton_crear.grid(row=3, column=0, columnspan=2, pady=5)

        # --- Datos del integrante ---
        marco_prog = ttk.LabelFrame(self.ventana, text="Integrante")
        marco_prog.pack(padx=10, pady=8, fill="x")

        ttk.Label(marco_prog, text="Nombre:").grid(row=0, column=0, padx=5, pady=3, sticky="e")
        self.campo_nombre = ttk.Entry(marco_prog, width=25)
        self.campo_nombre.grid(row=0, column=1)

        ttk.Label(marco_prog, text="Apellidos:").grid(row=1, column=0, padx=5, pady=3, sticky="e")
        self.campo_apellidos = ttk.Entry(marco_prog, width=25)
        self.campo_apellidos.grid(row=1, column=1)

        self.boton_anadir = ttk.Button(marco_prog, text="Añadir integrante",
                                       command=self.anadir_programador, state="disabled")
        self.boton_anadir.grid(row=2, column=0, columnspan=2, pady=5)

        self.caja_texto = tk.Text(self.ventana, width=55, height=12)
        self.caja_texto.pack(padx=10, pady=5)

    def imprimir(self, texto):
        self.caja_texto.insert(tk.END, texto + "\n")

    def crear_equipo(self):
        self.caja_texto.delete("1.0", tk.END)
        self.equipo = EquipoMaratonProgramacion(
            self.campo_equipo.get(),
            self.campo_universidad.get(),
            self.campo_lenguaje.get()
        )
        self.boton_anadir.config(state="normal")
        self.imprimir(f"Equipo '{self.equipo.nombre_equipo}' creado.")
        self.imprimir(f"Universidad: {self.equipo.universidad}")
        self.imprimir(f"Lenguaje: {self.equipo.lenguaje_programacion}")
        self.imprimir("Datos de los integrantes del equipo")

    def anadir_programador(self):
        nombre = self.campo_nombre.get()
        apellidos = self.campo_apellidos.get()
        try:
            EquipoMaratonProgramacion.validar_campo(nombre)
            EquipoMaratonProgramacion.validar_campo(apellidos)
            self.equipo.anadir(Programador(nombre, apellidos))
            self.imprimir(f"Integrante agregado: {nombre} {apellidos}")
            self.campo_nombre.delete(0, tk.END)
            self.campo_apellidos.delete(0, tk.END)
        except Exception as e:
            self.imprimir(f"Error: {e}")

    def iniciar(self):
        self.ventana.mainloop()


app = VentanaEquipo()
app.iniciar()