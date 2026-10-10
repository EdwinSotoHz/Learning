### Actions
Las acciones de GitHub son scripts empaquetados para automatizar tareas en un flujo de trabajo de desarrollo de software en GitHub.

### Workflows ya existentes
Si ves un flujo de trabajo que crees que podría ser un buen punto de partida, solo selecciona el botón `Configurar` para añadir el script y editar el código fuente `yml`.

### Types of Actions
Existen tres tipos: acciones en contenedores, acciones JavaScript y acciones compuestas.

Aquí tienes el resumen de los tres tipos de actions según ese texto:

## Tipos de Actions

**1. Container actions (Docker)**
- El **entorno va incluido** en el código de la acción (dentro del contenedor).
- Solo se ejecutan en **Linux** alojado por GitHub.
- Soportan **muchos lenguajes** (porque el contenedor trae todo lo necesario).

**2. JavaScript actions**
- El **entorno NO va incluido**; debes especificarlo aparte.
- Se ejecutan en **VM en la nube o en las instalaciones**.
- Soportan **Linux, macOS y Windows** (multiplataforma).

**3. Composite actions**
- **Combinan varios steps** de workflow dentro de una sola acción.
- Sirven para **agrupar varios comandos** y ejecutarlos luego como **un solo step**.    

## Identificar tipos
**Workflow** = Usar actions
**Action** = Logica empaquetada y reutilizable

Un workflow no es "de un tipo"; es un orquestador que puede combinar múltiples jobs, steps y actions de cualquier tipo.

Para identificar los tipos de cada action en un workflow hay claves:
- `run` no es una action
- `uses` indica consumir una action

| Tipo de Action | Lo que verás en `action.yml` | ¿Cómo se ejecuta? |
| :--- | :--- | :--- |
| **JavaScript** | `runs: using: 'node20'` (`node24`) y un `main:` apuntando a un `.js`  | Directamente en el runner (rápido y multiplataforma)  |
| **Docker Container** | `runs: using: 'docker'` y un `image:` que apunta a un `Dockerfile` o una imagen  | Dentro de un contenedor (aislado, pero solo en Linux)  |
| **Composite** | `runs: using: 'composite'` y una lista `steps:` con los comandos a ejecutar  | Agrupa varios pasos y los ejecuta en el runner  |

- Si ves que la action está en un repositorio oficial de `actions/` o es muy popular, casi siempre será de tipo **JavaScript**. Las Docker Actions son menos comunes para tareas simples.

- La única regla es que cada paso de tipo `run:` debe especificar explícitamente su `shell:` (como `bash`, `pwsh` o `python`). Por eso puedes mezclar comandos de distintos lenguajes dentro de la misma acción.