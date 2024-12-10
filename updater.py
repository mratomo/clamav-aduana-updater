import subprocess
import os

URL_BASE = "https://database.clamav.net"
ARCHIVOS_CVD = ["main.cvd", "daily.cvd", "bytecode.cvd"]

def verificar_conexion():
    """Verifica si el servidor está accesible utilizando ping."""
    try:
        result = subprocess.run(
            ["ping", "-n", "1", "database.clamav.net"],  # "-n" es para Windows
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return result.returncode == 0
    except Exception as e:
        print(f"Error al verificar la conexión: {e}")
        return False

def verificar_o_crear_directorio(usb_path):
    """Verifica si el directorio 'antivirus' existe en el USB. Si no, lo crea."""
    directorio_antivirus = os.path.join(usb_path, "antivirus")
    if not os.path.exists(directorio_antivirus):
        print(f"Creando directorio: {directorio_antivirus}")
        os.makedirs(directorio_antivirus)
    return directorio_antivirus

def descargar_actualizaciones(usb_path):
    """Descarga los archivos .cvd utilizando curl."""
    directorio_antivirus = verificar_o_crear_directorio(usb_path)

    for archivo in ARCHIVOS_CVD:
        url = f"{URL_BASE}/{archivo}"
        destino = os.path.join(directorio_antivirus, archivo)

        print(f"Descargando {archivo} desde {url}...")
        try:
            # Construir y ejecutar el comando curl
            comando = [
                "curl",
                "-o", destino,  # Especifica el archivo de salida
                "-L",           # Sigue redirecciones
                "-H", "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                url,
            ]
            resultado = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            if resultado.returncode == 0:
                print(f"Archivo {archivo} descargado correctamente en {destino}")
            else:
                print(f"Error al descargar {archivo}: {resultado.stderr}")
                raise Exception(f"Error al descargar {archivo}: {resultado.stderr}")

        except Exception as e:
            print(f"Excepción al descargar {archivo}: {e}")
            raise
