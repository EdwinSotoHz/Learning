# BASH

```bash
ls              # listar
ls -la          # listar con detalles y ocultos
pwd             # ruta actual

mkdir Folder    # crear carpeta
touch File.txt  # crear archivo

code / agy file # abrir en VSCode
clear           # limpiar terminal
```

# Git — Control de versiones distribuido

```bash
git -v
git -h
```

**Config global:**
```bash
git config --global user.email ""
git config --global user.name ""
```

**Config repo:**
```bash
git config user.name ""
git config user.email ""
```

**Conceptos:**
- **HEAD** → dónde está situado el proyecto actualmente.
- **Snapshot** → "foto" del repo (commit pusheado).
- **Flujo:** Área local → Área Stage → Commit → Foto (local o GitHub).
- En la rama `main` hay fotos acumuladas (estados del repo).

# Comandos Git

```bash
git init                    # crea repo local (.git)
git status                  # commits en rama, ficheros a subir, no subidos y untracked
git add file file file      # snapshot al área stage
git commit -m ""            # guarda snapshot con mensaje
git push                    # envía foto al álbum
git log                     # hash y datos de commits
git log --graph             # historial gráfico
git diff                    # líneas cambiadas vs último commit
```

**Deshacer:**
```bash
git reset    # borra commit y vacía git add (archivos intactos)
```

**Navegar / recuperar:**
```bash
git checkout <rama/hash/file>   # cambiar rama, ver commit o regresar un file
```

# .gitignore

```
**/file.txt
/Folder/
file.txt
```

# GitHub

Espejo de lo que hay en el repo local.