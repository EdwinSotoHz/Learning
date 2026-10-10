### Primer Ejemplo Workflow (Consumir actions ya creadas)
Suponiendo que hay un script python que genera un json, se pueden hacer ejecuciones de actions.

> Para casos concretos se puede usar actions ya hechas, pero para este caso se planea hacer un workflow desde cero

- Primero dar click en Actions
- Después hacemos una por nosotros mismos
- Se creará un archivo .ylm en /.github/workflows/
- Principales características de un workflow:

Notas: Algunos niveles de yml pueden llevar nombres de claves propios, p.ej: el primer nivel dentro de `jobs`, `env`, `outputs`, pueden ser claves propias y no palabras reservadas de yaml.

```yaml
name: NAME # nombre del workflow

on: # indica el evento (trigger) por el cual se ejecuta un workflow
  push:
    branches:
      - main
      # cada que se haga push en la rama main

jobs: # aquí van todos los jobs
  job_1:  # nombre del job 1 (build)
    runs-on: ubuntu-latest # runer (cada job tiene su runner, se recomienda ubuntu-latest)

    permissions:   # Requerido para la action de autocommit
      contents: write

    steps: # lista de steps
      - name: STEP_1 # nombre del step
        uses: actions/checkout@v7  # Invocación tipo Action (es la action que clona en el runner)

      # Implementacion la action python (requiere checkout y run segun la documentacion oficial)
      - name: STEP_2 
        uses: actions/setup-python@v7 # Invocación tipo Action 
        with:  # (with: = parámetros)
          python-version: 3.13

      - name: STEP_2.5 
        run: python ./Actions/Examples/script.py # requerido para ejecutar el script

      - name: STEP_3 Comitear y pushear archivo generado
        uses: stefanzweifel/git-auto-commit-action@v7
        with:
          commit_message: Autocommit desde action
          commit_user_name: Git Actions
          commit_user_email: edwinsotohz@gmail.com 
          commit_author: EdwinSotoSHz

```

- Los archivos generados Solo se generan en el runner, pero se pueden commitear desde el runner.
- LOS COMANDOS `run` se ejecutan desde la raíz del repositorio `$GITHUB_WORKSPACE`, no desde la carpeta del workflow.
- Los `run` y `uses` no pueden estar en el mismo ITEM, un step usa cualquiera, pero no ambos.
- En jobs `name` (si lleva), `uses` y `with` deben ser items hermanos (tambien `run` independientes).
- `runs-on`, `permissions` y `steps` estan al mismo nivel para configurar el job.
- Se puede crear desde actions o en local el archivo YAML, y una vez esta en el repo ahora si correrá el action (triggerado por un push/pull o lo que sea).

Una vez el workflow es disparado, en la seccion de actions del repo, se podra ver el proceso en ejecucion, con sus respectivos jobs y pasos.
También tiene mas opciones como re-run, ver el workflow, el uso de la vm.

#### `run` multilinea
```yaml
- name: STEP_X
  run: |
    npm install
    npm run build
```


El ejemplo anterior era para crear un workflow que consume ciertas actions.
Pero las actions se pueden crear y pueden ser tipo js, docker o composite.