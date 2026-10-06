## BASH

```bash
ls              ## listar
ls -la          # listar con detalles y ocultos
pwd             # ruta actual

mkdir Folder    # crear carpeta
touch File.txt  # crear archivo

code / agy file # abrir en VSCode
clear           # limpiar terminal
```

## Git: Control de versiones distribuido

**Version y help:**
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

**Iniciar en local:**
```bash
git init                    # crea repo local (.git)
git branch -m master main   # cambia el nombre de la rama master a main (solo si se necesita)
```

**Hacer commits:**
```bash
git status                  # rama, files para el siguiente commit (en stage), archivos no en stage y no trackeados
git add <file> <file> <file>      # agregar snapshots al área stage
git commit -m ""            # guarda snapshot del área stage con mensaje
git push                    # envía foto al álbum (solo si existe un repo en github)
```

**Ver historial:**
```bash
git log                     # hash y datos de commits
git log --graph             # historial gráfico
git diff                    # líneas cambiadas vs último commit
```

**.gitignore**
```
**/file.txt
/Folder/
file.txt
```

**Deshacer:**
```bash
git reset    # borra commit y vacía git add (archivos intactos)
```

**Navegar / recuperar:**
```bash
git checkout <file/hash/rama>   # cambiar rama, ver commit o regresar un file
```

**Vincula tu repositorio local con GitHub:**
```bash
git remote add origin https://github.com
git push -u origin main
```

**Regesar oficialemente a un commit:**
```bash
git reset --hard <hash>    # borra commits hasta el hash indicado y regresa los archivos a ese punto
git reflog                 # muestra el log de todos los commits
```

# GitHub

Espejo de lo que hay en el repo local.