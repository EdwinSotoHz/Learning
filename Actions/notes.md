## **CI/CD** 

Significa **Integración Continua** (*Continuous Integration*) y **Entrega/Despliegue Continuo** (*Continuous Delivery / Continuous Deployment*). 
Es una metodología y conjunto de prácticas de desarrollo de software que busca automatizar el ciclo de vida del código, desde que un desarrollador escribe una línea nueva hasta que se despliega en producción.

***Alegoría: "línea de ensamblaje automatizada en una fábrica."***

---

### 1. CI - Integración Continua (*Continuous Integration*)
Práctica donde los desarrolladores fusionan (*merge*) su código en un repositorio central de manera frecuente (varias veces al día).
Cada vez que alguien sube código (*push*), un servidor automatizado (como GitHub Actions) ejecuta una serie de pasos sin intervención humana:
1. Compila el código para asegurarse de que no hay errores de sintaxis.
2. Ejecuta pruebas unitarias y de integración (*tests*).
3. Analiza la calidad del código o busca vulnerabilidades de seguridad.

**El objetivo:** Detectar errores en cuanto antes, para que corregir un fallo cueste minutos.

---

### 2. CD - Entrega Continua o Despliegue Continuo (*Continuous Delivery / Continuous Deployment*)
Una vez que el código pasa todas las pruebas de la fase de CI, la fase de CD se encarga de prepararlo o enviarlo automáticamente a los entornos correspondientes (servidores de pruebas, preproducción o producción).
- **Entrega Continua (*Delivery*):** El código se empaqueta y se deja listo para lanzarse, pero **requiere la aprobación manual** para subirlo a producción.
- **Despliegue Continuo (*Deployment*):** Todo es 100% automático. Si el código pasa las pruebas, se sube a producción **sin que nadie tenga que hacer clic en ningún botón**.

---

### ¿Por qué entra GitHub Actions aquí?
GitHub Actions es precisamente la herramienta que te permite **construir tus propios pipelines de CI/CD**.

Cuando configuras un archivo en GitHub Actions, le estás diciendo a GitHub: *"Cada vez que yo haga un `push` a la rama `main`, quiero que corras este script que compila mi proyecto, ejecute mis pruebas y, si todo sale bien, lo despliegue automáticamente a mi servidor de Azure o AWS"*.

**Pipeline (o canalización):** Serie de pasos o procesos conectados de forma secuencial y automatizada para cumplir un objetivo específico.

### Colaboracion
Grandes proveedores como **Azure** y **AWS** facilitan el proceso ofreciendo en el Marketplace sus propias *actions* oficiales (ej. autenticación y despliegue en la nube), evitando construir integraciones desde cero.

## **Conceptos Clave**
**Concepto Clave:** Es como si GitHub clonara el repo en una VM e hiciera lo que le indico en el workflow, por ende puede generar archivos, modificar archivos, hacer commits y hacer push de esos cambios.

- **Workflow** → proceso automatizado completo (archivo YAML en `.github/workflows/`).
  ***Contiene:** triggers (`on:`) + uno o varios **jobs***.
<br>

- **Job** → conjunto de pasos que corren en el mismo runner.
  ***Contiene:** `runs-on` (dónde corre) + uno o varios **steps***.
<br>

- **Step** → unidad dentro de un job.
  ***Contiene:** un comando shell (`run:`) **o** una invocación a una action (`uses:`)*.
<br>

- **Action** → componente reutilizable que se invoca dentro de un step (`uses:`).
  ***Contiene:** la lógica empaquetada — comandos agrupados (composite), código JS (JavaScript) o un contenedor con entrypoint (Docker), más su `action.yml` con inputs/outputs*.
<br>

- **Runner** → la VM donde se ejecuta el job. TEMPORAL (efímero y aislado)
  ***Contiene:** el entorno de ejecución (SO, herramientas preinstaladas) donde corren los steps*.

## Primeros pasos
- Crear una carpeta .github/workflows/
- Dentro de la carpeta, crear un archivo YAML con el nombre del workflow.
- Por ejemplo: .github/workflows/main.yaml

## YAML
> Escalar = 1 solo valor
> Mapa = objeto, diccionario, hash
> Secuencia = array, lista

- En YAML no se permiten tabs para indentar, solo espacios 2 típicamente.
- Un Mapa es un conjunto de pares `<clave>: <valor>` al mismo nivel.
- Sangria dice dentro de que nivel/clave están
- Se maneja `<clave>: <valor>`
- Una clave con valor escalar no puede tener hijos (si tiene valor delante no puede tener hijos)
- Una clave puede tener mas claves anidadas

```yaml
clave1:
  clave2: valor2
```

- Puede contener varios elementos como valores con `-`, caso solo valores (array):
```yaml
clave: 
  - valor1
  - valor2
  - valor3
```

- Puede contener varios elementos como propiedades, caso propiedades (objeto):
```yaml
clave: 
  claveProp1: valor
  claveProp2: valor
  claveProp3: valor
```

- Puede contener varios elementos como objetos con propiedades cada uno, caso objetos con propiedades (array de objetos), se usa para tener varios mapas distintos en una clave:
```yaml
clave: 
  - claveObj1:
      claveProp: valor
  - claveObj2:
      claveProp1: valor
      claveProp2: valor
  - claveObj3:
      claveProp: 
        - valor1
        - valor2
        - valor3
```

- Se puede tener una lista de mapas, donde cada mapa (ítem) tiene las mismas claves que los demás. Cada `-` abre un nuevo mapa, se usa para tener mapas "iguales" en la misma clave:
```yaml
clave: 
  - nombre: Juan
    edad: 30
  - nombre: Ana
    edad: 25
```

## Roles de action (Consumir y crear)
El uso común en Actions que es crear workflows consumiendo Actions (workflows):
- Crear un workflow en `.github/workflows/*.yml` 
- Consumir actions de repos externos: `uses: usuario-github/hello-world-action@v1`
- Comunmente usan pasos y requerimentos específicos y usan `uses` y `run`.

El otro uso es crear actions Locales que además pueden ser consumidas en otros repos (actions):
- Crear un archivo `action.yml` en `.github/actions/`.
- Dentro de este archivo, se definen `runs`, `inputs`, `outputs` y los `steps` que la componen.
- Puede tener `uses` y `run` como un workflow, pero no tiene `on` porque es una action local.
- Son tipo js, docker o composite (definido en el `runs:`)
