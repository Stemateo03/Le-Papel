import tkinter as tk
from conexion import conectar
from tkinter import messagebox

def ventana_stock():
    ventana = tk.Tk()
    ventana.title("Gestión de Stock")
    ventana.geometry("350x250")

    tk.Label(ventana, text="Nombre").pack()
    e_nombre = tk.Entry(ventana)
    e_nombre.pack()

    tk.Label(ventana, text="Precio").pack()
    e_precio = tk.Entry(ventana)
    e_precio.pack()

    tk.Label(ventana, text="Stock").pack()
    e_stock = tk.Entry(ventana)
    e_stock.pack()

    def guardar():
        con = conectar()
        cur = con.cursor()
        cur.execute(
            "INSERT INTO productos (nombre, precio, stock) VALUES (%s,%s,%s)",
            (e_nombre.get(), e_precio.get(), e_stock.get())
        )
        con.commit()
        con.close()
        messagebox.showinfo("OK", "Producto guardado")

    tk.Button(ventana, text="Guardar Producto", command=guardar).pack(pady=10)

    ventana.mainloop()
