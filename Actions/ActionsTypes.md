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

