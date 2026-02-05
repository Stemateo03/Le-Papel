import tkinter as tk
from tkinter import messagebox
from conexion import conectar
from menu import abrir_menu

def ventana_login():
    ventana = tk.Tk()
    ventana.title("Papelería")
    ventana.geometry("300x250")

    # Etiquetas y entradas
    tk.Label(ventana, text="Usuario").pack(pady=5)
    e_user = tk.Entry(ventana)
    e_user.pack()

    tk.Label(ventana, text="Clave").pack(pady=5)
    e_pass = tk.Entry(ventana, show="*")
    e_pass.pack()

    # Función de login
    def ingresar():
        usuario = e_user.get()
        clave = e_pass.get()

        if usuario == "" or clave == "":
            messagebox.showerror("Error", "Complete todos los campos")
            return

        con = conectar()
        cur = con.cursor()

        # 🔥 AQUÍ ESTÁ LA CORRECCIÓN CLAVE (%s en lugar de ?)
        cur.execute(
            "SELECT rol FROM usuarios WHERE usuario=%s AND clave=%s",
            (usuario, clave)
        )

        fila = cur.fetchone()
        con.close()

        if fila:
            ventana.destroy()
            abrir_menu(fila[0])
        else:
            messagebox.showerror("Error", "Usuario o clave incorrectos")

    # Botón
    tk.Button(ventana, text="Ingresar", command=ingresar).pack(pady=15)

    ventana.mainloop()
