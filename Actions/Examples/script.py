import json
from pathlib import Path

datos = {
    "nombre": "Edwin",
    "edad": 22,
    "lenguajes": ["Python", "JavaScript"]
}

archivo = Path(__file__).parent / "datos.json"

with open(archivo, "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=2, ensure_ascii=False)

print(f"JSON creado en: {archivo}")