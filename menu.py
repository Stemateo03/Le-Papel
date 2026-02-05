import tkinter as tk
from stock import ventana_stock
from ventas import ventana_ventas   # 👈 IMPORTANTE

def abrir_menu(rol):
    ventana = tk.Tk()
    ventana.title("Menú Principal")
    ventana.geometry("350x250")

    tk.Label(
        ventana,
        text=f"Rol: {rol}",
        font=("Arial", 12, "bold")
    ).pack(pady=10)

    tk.Button(
        ventana,
        text="Stock / Almacén",
        width=20,
        height=2,
        command=ventana_stock
    ).pack(pady=5)

    tk.Button(
        ventana,
        text="Ventas / Facturación",
        width=20,
        height=2,
        command=ventana_ventas
    ).pack(pady=5)

    if rol == "DUENA":
        tk.Button(
            ventana,
            text="Reportes",
            width=20,
            height=2
        ).pack(pady=5)

    tk.Button(
        ventana,
        text="Salir",
        width=20,
        command=ventana.destroy
    ).pack(pady=10)

    ventana.mainloop()
