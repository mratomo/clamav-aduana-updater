# ✨ ClamAV Updater ✨

Esta herramienta facilita la descarga de las bases de datos de detección de **ClamAV** (archivos `.cvd`) en un equipo con conexión a Internet y su posterior transferencia a sistemas que funcionan **offline** (aislados de la red). De esta forma, se pueden mantener las definiciones de virus **actualizadas** en entornos donde no es posible conectarse directamente a los servidores de ClamAV.

## 🌟 Características

- 🚀 **Descarga automática** de las bases de datos de ClamAV: `main.cvd`, `daily.cvd`, `bytecode.cvd`.
- 🌐 **Verificación de conexión a Internet** antes de iniciar la descarga.
- 💻 **Detección automática de dispositivos USB** (unidades removibles) para almacenar las definiciones.
- 🖥️ **Interfaz gráfica** sencilla (GUI) usando `customtkinter`.
- 📜 **Log de eventos** y una barra de progreso para informar al usuario.

## ⚠️ Importante

Dada la función para la que está destinada esta herramienta (descarga y transferencia de definiciones de antivirus a sistemas aislados), **es altamente recomendable revisar y auditar el código fuente antes de su uso en entornos críticos**, más allá de verificar solamente las URLs de descarga. Es esencial comprender a fondo las operaciones que el programa realiza, en particular:

- 🌐 Acceso a la red y descarga de archivos.
- 🏗️ Ejecución de comandos externos (como `curl` y `ping`).
- 💾 Manipulación de datos en unidades USB.

Una revisión exhaustiva del código ayudará a garantizar la **seguridad** y la **confiabilidad** en ambientes sensibles.

## 📦 Requisitos

- 🐍 **Python 3.8+**
- 🗃️ **Librerías de Python:**  
  - `customtkinter`
  - `tkinter` (incluida en la instalación estándar de Python)
  - `psutil`
- 🔧 **Herramientas externas:**  
  - `curl`: necesaria para descargar las definiciones de virus.
  - `ping`: para verificar conectividad.

Asegúrate de tener `curl` instalado:  
- **En Windows:** [curl.se](https://curl.se/download.html) o instala Git for Windows (que incluye `curl`).
- **En Linux:** `sudo apt-get install curl` o `sudo yum install curl`.

## 🔧 Instalación de Dependencias

```bash
# Instalación de dependencias en Linux
sudo apt-get update
sudo apt-get install python3-pip curl
pip3 install customtkinter psutil

# Instalación en Windows (asumiendo que Python y pip están en PATH)
pip install customtkinter psutil
```

## 🏃 Uso

1. Clona el repositorio o descarga los archivos:
   ```bash
   git clone https://github.com/usuario/clamav-updater.git
   cd clamav-updater
   ```
   
2. Ejecuta la aplicación:
   ```bash
   python main.py
   ```
   
3. En la interfaz gráfica, presiona el botón **"Iniciar Actualización"**:
   - 🌐 Verificará la conexión con `database.clamav.net`.
   - 🔌 Detectará una memoria USB conectada.
   - 📂 Creará el directorio `antivirus` en el USB, si no existe.
   - ⬇️ Descargará las definiciones `.cvd` al USB.
   - 🎉 Si todo va bien, mostrará un mensaje de éxito.

4. Lleva la memoria USB al sistema offline y copia/actualiza las definiciones en el directorio de ClamAV del sistema aislado.

## 📦 Empaquetado

Para distribuir la herramienta sin requerir la instalación previa de Python y sus dependencias, puedes empaquetarla en un ejecutable usando **PyInstaller**.

### 🪟 Empaquetado en Windows

**Requisitos previos:**

- Python instalado.
- PyInstaller instalado:
  ```bash
  pip install pyinstaller
  ```

**Pasos:**

1. En el directorio del proyecto:
   ```bash
   cd clamav-updater
   ```

2. Ejecuta PyInstaller:
   ```bash
   pyinstaller --onefile --noconsole main.py
   ```
   - `--onefile`: genera un solo ejecutable.
   - `--noconsole`: sin ventana de consola.

3. El ejecutable estará en `dist/main.exe`.

4. Copia `main.exe` y otros archivos necesarios al destino.

**Nota:**  
Asegúrate de que `curl` esté disponible en el sistema destino. Si no, inclúyelo junto con el ejecutable o instálalo en el PATH del equipo final.

### 🐧 Empaquetado en Linux

**Requisitos previos:**

- Python 3 y pip.
- PyInstaller instalado:
  ```bash
  pip3 install pyinstaller
  ```

**Pasos:**

1. En el directorio del proyecto:
   ```bash
   cd clamav-updater
   pyinstaller --onefile main.py
   ```

2. El ejecutable estará en `dist/main`.

3. Asegúrate de que tenga permisos de ejecución:
   ```bash
   chmod +x dist/main
   ```

**Nota:**  
- En Linux, `curl` suele estar en los repositorios oficiales. Instálalo si no está presente.
- Si quieres un binario totalmente estático, puede ser más complejo por las dependencias dinámicas.

## 🗂️ Estructura del Proyecto

```
clamav-updater/
├─ main.py          # Script principal con la interfaz gráfica
├─ updater.py       # Funciones para verificar conexión y descargar definiciones
├─ usb_detector.py  # Función para detectar unidades USB
├─ requirements.txt # (Opcional) Lista de dependencias
└─ README.md        # Este archivo
```

## 🛠️ Troubleshooting

- **No se detecta USB:**  
  Asegúrate de que la memoria USB esté montada y aparezca como unidad extraíble.  
  - En Windows, debe tener una letra de unidad (E:, F:, etc.).  
  - En Linux, `psutil.disk_partitions()` debe mostrarla con la opción `removable`.

- **No se encuentra `curl`:**  
  Instala `curl` en el sistema anfitrión.  
  - En Windows, puedes incluir `curl.exe` junto con `main.exe`.  
  - En Linux, `sudo apt-get install curl`.

- **Error con PyInstaller y `customtkinter`:**  
  Asegúrate de tener la última versión de `customtkinter`. Si la GUI falla, prueba sin `--noconsole` para ver mensajes de error detallados.

## 📜 Licencia

Este proyecto se distribuye bajo la [Licencia MIT](LICENSE), una de las más permisivas disponibles. Puedes hacer uso del código según los términos descritos en dicha licencia.  
Se recomienda auditar el código antes de implementarlo en entornos críticos.

---
