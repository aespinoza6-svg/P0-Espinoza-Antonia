"""system_info.py: obtiene informacion basica del computador y la guarda en data/system_info.json."""
import ctypes
import json
import os
import platform
import sys
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATA_FILE = DATA_DIR / "system_info.json"


def obtener_ram_total_gb():
    """Devuelve la memoria RAM total en GB o None si no se puede obtener."""
    try:

        class MEMORYSTATUSEX(ctypes.Structure):
            _fields_ = [
                ("dwLength", ctypes.c_ulong),
                ("dwMemoryLoad", ctypes.c_ulong),
                ("ullTotalPhys", ctypes.c_ulonglong),
                ("ullAvailPhys", ctypes.c_ulonglong),
                ("ullTotalPageFile", ctypes.c_ulonglong),
                ("ullAvailPageFile", ctypes.c_ulonglong),
                ("ullTotalVirtual", ctypes.c_ulonglong),
                ("ullAvailVirtual", ctypes.c_ulonglong),
                ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
            ]

        stat = MEMORYSTATUSEX()
        stat.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
        if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat)):
            return round(stat.ullTotalPhys / (1024 ** 3), 2)
    except Exception:
        pass
    return None


def obtener_procesador():
    """Devuelve el modelo del procesador."""
    proc = platform.processor()
    if proc:
        return proc
    return platform.machine()


def obtener_info():
    """Reune la informacion basica del computador."""
    return {
        "sistema_operativo": platform.system(),
        "version_sistema": platform.release(),
        "arquitectura": platform.machine(),
        "version_python": sys.version.split()[0],
        "procesador": obtener_procesador(),
        "procesadores_logicos": os.cpu_count(),
        "memoria_ram_total_gb": obtener_ram_total_gb(),
    }


def main():
    info = obtener_info()
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(info, f, indent=2, ensure_ascii=False)
    print(json.dumps(info, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
