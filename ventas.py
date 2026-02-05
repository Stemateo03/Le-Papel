import tkinter as tk
from tkinter import messagebox
from conexion import conectar

def ventana_ventas():
    ventana = tk.Tk()
    ventana.title("Facturación / Ventas")
    ventana.geometry("500x400")

    tk.Label(
        ventana,
        text="FACTURACIÓN",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    tk.Label(ventana, text="ID Producto").pack()
    e_producto = tk.Entry(ventana)
    e_producto.pack()

    tk.Label(ventana, text="Cantidad").pack()
    e_cantidad = tk.Entry(ventana)
    e_cantidad.pack()

    def registrar_venta():
        producto_id = e_producto.get()
        cantidad = int(e_cantidad.get())

        con = conectar()
        cur = con.cursor()

        # Obtener precio y stock
        cur.execute(
            "SELECT precio, stock FROM productos WHERE id=%s",
            (producto_id,)
        )
        producto = cur.fetchone()

        if not producto:
            messagebox.showerror("Error", "Producto no existe")
            con.close()
            return

        precio, stock = producto

        if cantidad > stock:
            messagebox.showerror("Error", "Stock insuficiente")
            con.close()
            return

        total = precio * cantidad

        # Insertar venta
        cur.execute(
            "INSERT INTO ventas (total) VALUES (%s)",
            (total,)
        )
        venta_id = cur.lastrowid

        # Insertar detalle
        cur.execute(
            "INSERT INTO detalle_venta (venta_id, producto_id, cantidad, precio) VALUES (%s,%s,%s,%s)",
            (venta_id, producto_id, cantidad, precio)
        )

        # Descontar stock
        cur.execute(
            "UPDATE productos SET stock = stock - %s WHERE id = %s",
            (cantidad, producto_id)
        )

        con.commit()
        con.close()

        messagebox.showinfo("OK", f"Venta registrada\nTotal: ${total:.2f}")

    tk.Button(
        ventana,
        text="Registrar Venta",
        font=("Arial", 12),
        width=20,
        height=2,
        command=registrar_venta
    ).pack(pady=20)

    ventana.mainloop()
