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
- **Workflow (Flujo de trabajo):** Es un proceso automatizado que se ejecuta en respuesta a un evento. Está definido en un archivo YAML dentro del directorio `.github/workflows/`.
- **Job (Trabajo):** Es un conjunto de pasos que se ejecutan en el mismo *runner*, pueden ejecutarse en paralelo o de forma secuencial.
- **Step (Paso):** Puede ser un comando de shell, una acción o una secuencia de acciones.
- **Runner (Ejecutor):** Es una VM donde se ejecuta el *workflow*. Puede ser un *runner* de GitHub (VM compartidas) o un *runner* autohospedado.

## Primeros pasos
- Crear una carpeta .github/workflows/
- Dentro de la carpeta, crear un archivo YAML con el nombre del workflow.
- Por ejemplo: .github/workflows/main.yaml

### Ejemplo workflow
