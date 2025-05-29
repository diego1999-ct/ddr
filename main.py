import tkinter as tk
from tkinter import scrolledtext
from dashboard import generate_report  # Importa la función que genera el reporte

def main():
    # Crear ventana principal de la aplicación
    root = tk.Tk()
    root.title("Dashboard Clima y Noticias - Tema Oscuro")  # Título de la ventana
    root.geometry("700x600")  # Tamaño fijo de la ventana (ancho x alto)
    root.configure(bg="#222222")  # Color de fondo oscuro (hexadecimal)

    # Crear un área de texto con barra de scroll para mostrar el reporte
    text_area = scrolledtext.ScrolledText(
        root,                # Ventana padre
        wrap=tk.WORD,        # Ajusta texto por palabras
        width=80,            # Ancho en caracteres
        height=30,           # Alto en líneas
        bg="#333333",        # Fondo del área de texto (oscuro)
        fg="white",          # Color del texto
        insertbackground='white', # Color del cursor
        font=("Consolas", 11)     # Fuente y tamaño del texto
    )
    text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)  # Empaquetar con relleno y expansión

    # Crear un frame (contenedor) para agrupar los botones en una fila
    button_frame = tk.Frame(root, bg="#222222")
    button_frame.pack(pady=(0, 10))  # Separación vertical abajo

    # Función que carga y muestra el reporte en el área de texto
    def mostrar_reporte():
        text_area.delete("1.0", tk.END)  # Limpia el contenido actual
        reporte = generate_report()      # Obtiene el reporte generado
        text_area.insert(tk.END, reporte) # Inserta el reporte en el área de texto

    # Botón para cargar el reporte y mostrarlo en el área de texto
    btn_cargar = tk.Button(
        button_frame, text="Cargar Reporte", command=mostrar_reporte,
        bg="#555555", fg="white", activebackground="#777777",
        font=("Arial", 12)
    )
    btn_cargar.pack(side=tk.LEFT, padx=10)  # Empaquetar a la izquierda con separación horizontal

    # Función para borrar el contenido del área de texto
    def borrar_texto():
        text_area.delete("1.0", tk.END)  # Limpia todo el texto del widget

    # Botón para borrar el texto mostrado
    btn_borrar = tk.Button(
        button_frame, text="Borrar", command=borrar_texto,
        bg="#aa2222", fg="white", activebackground="#cc4444",
        font=("Arial", 12)
    )
    btn_borrar.pack(side=tk.LEFT, padx=10)  # Empaquetar a la izquierda con separación horizontal

    # Ejecuta el loop principal de la ventana (espera eventos)
    root.mainloop()

# Si el archivo se ejecuta directamente, corre la función main()
if __name__ == "__main__":
    main()
