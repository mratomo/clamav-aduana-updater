import psutil

def detectar_usb():
    """Detecta dispositivos USB conectados."""
    dispositivos = [p.device for p in psutil.disk_partitions() if 'removable' in p.opts]
    return dispositivos[0] if dispositivos else None
