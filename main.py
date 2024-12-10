import customtkinter as ctk
from tkinter import messagebox
from updater import verificar_conexion, descargar_actualizaciones
from usb_detector import detectar_usb

class ClamAVUpdaterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("ClamAV Updater")
        self.geometry("600x400")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # Título
        self.label_title = ctk.CTkLabel(self, text="ClamAV Updater", font=("Arial", 20))
        self.label_title.pack(pady=10)

        # Botón para iniciar actualización
        self.start_button = ctk.CTkButton(self, text="Iniciar Actualización", command=self.start_update)
        self.start_button.pack(pady=10)

        # Barra de progreso
        self.progress = ctk.CTkProgressBar(self, orientation="horizontal", width=400)
        self.progress.pack(pady=10)
        self.progress.set(0)

        # Campo de texto para logs
        self.log = ctk.CTkTextbox(self, width=500, height=200, state="disabled")
        self.log.pack(pady=10)

    def log_message(self, message):
        """Agregar mensajes al campo de texto."""
        self.log.configure(state="normal")
        self.log.insert("end", message + "\n")
        self.log.configure(state="disabled")
        self.log.see("end")

    def start_update(self):
        """Inicia el proceso de actualización."""
        self.log_message("Verificando conexión al servidor...")
        if not verificar_conexion():
            self.log_message("Error: No se pudo conectar al servidor.")
            messagebox.showerror("Error", "No se pudo conectar al servidor. Verifica tu conexión a Internet.")
            return

        usb_path = detectar_usb()
        if not usb_path:
            self.log_message("Error: No se detectó ningún USB.")
            messagebox.showerror("Error", "No se detectó ningún USB conectado.")
            return

        self.log_message(f"USB detectado en: {usb_path}")
        self.log_message("Iniciando descarga de archivos...")
        self.progress.set(0.5)
        self.update_idletasks()

        try:
            descargar_actualizaciones(usb_path)
            self.log_message("Actualización completada.")
            self.progress.set(1.0)
            messagebox.showinfo("Éxito", "Actualización completada exitosamente.")
        except Exception as e:
            self.log_message(f"Error al descargar: {e}")
            messagebox.showerror("Error", f"Ocurrió un problema durante la descarga.\n{e}")
        self.progress.set(0)

if __name__ == "__main__":
    app = ClamAVUpdaterApp()
    app.mainloop()
