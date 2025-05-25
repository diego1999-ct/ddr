import tkinter as tk
from tkinter import scrolledtext
from dashboard import generate_report  # Asegúrate que dashboard.py tenga esta función

def main():
    root = tk.Tk()
    root.title("Dashboard Clima y Noticias - Tema Oscuro")
    root.geometry("700x600")
    root.configure(bg="#222222")  # Fondo oscuro

    # Área de texto con scroll para mostrar el reporte
    text_area = scrolledtext.ScrolledText(
        root, wrap=tk.WORD, width=80, height=30,
        bg="#333333", fg="white", insertbackground='white',
        font=("Consolas", 11)
    )
    text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Función para cargar el reporte en el área de texto
    def mostrar_reporte():
        text_area.delete("1.0", tk.END)
        reporte = generate_report()
        text_area.insert(tk.END, reporte)

    # Botón para cargar reporte
    btn_cargar = tk.Button(
        root, text="Cargar Reporte", command=mostrar_reporte,
        bg="#555555", fg="white", activebackground="#777777", font=("Arial", 12)
    )
    btn_cargar.pack(pady=(0, 5))

    # Función para borrar el contenido del área de texto
    def borrar_texto():
        text_area.delete("1.0", tk.END)

    # Botón para borrar contenido (el botón sí debe aparecer aquí)
    btn_borrar = tk.Button(
        root, text="Borrar", command=borrar_texto,
        bg="#aa2222", fg="white", activebackground="#cc4444", font=("Arial", 12)
    )
    btn_borrar.pack(pady=(0, 10))

    root.mainloop()

if __name__ == "__main__":
    main()
