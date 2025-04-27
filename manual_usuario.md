# Manual de Usuario

**Proyecto: Clasificación de Cáncer de Mama con Perceptrón Simple**

**Curso: Inteligencia Artificial 1**
**Autor: Juan Pablo Meza Vielman**
**Docente: Ing. Daniel González**
**Centro Universitario de Occidente, 2025**

---

## 1. Introducción

Este manual tiene como objetivo ayudarte a utilizar correctamente la aplicación desarrollada para clasificar tumores mamarios como benignos o malignos. Esta aplicación fue creada como parte del proyecto del curso de Inteligencia Artificial 1 y está diseñada para que cualquier persona pueda usarla de manera sencilla, sin necesidad de conocimientos profundos de programación o inteligencia artificial.

El sistema permite configurar algunos parámetros para que puedas entrenar el modelo y observar cómo aprende a clasificar los datos. Además, incluye gráficos que muestran los resultados de forma visual y fácil de entender.

---

## 2. ¿Qué hace la aplicación?

Esta aplicación utiliza un modelo muy sencillo llamado Perceptrón Simple para aprender a identificar si un tumor es benigno o maligno. Para esto, utiliza información sobre ciertas características del tumor, como el tamaño y la textura de las células.

El sistema permite que tú decidas qué características usar, cuánto tiempo quieres que el modelo aprenda, y qué porcentaje de los datos se utilizará para el aprendizaje. Una vez configurado, el sistema realiza el entrenamiento y te muestra los resultados mediante gráficos que explican cómo se comportó el modelo.

---

## 3. Requisitos para usar la aplicación

Para poder utilizar la aplicación necesitas lo siguiente:

- Una computadora con sistema operativo Windows, Linux o macOS.
- Tener instalado Python versión 3.8 o superior.
- Tener las siguientes librerías instaladas en Python: numpy, matplotlib, scikit-learn y tkinter.

Si no tienes estas librerías, puedes instalarlas de forma rápida con el siguiente comando en la terminal o consola:

```
pip install -r requirements.txt
```

---

## 4. Cómo iniciar la aplicación

1. Abre una terminal o consola de comandos.
2. Colócate dentro de la carpeta donde descargaste el proyecto.
3. Ejecuta uno de los siguientes comandos:

- En Windows:

  ```
  python main.py
  ```

- En Linux o macOS:

  ```
  python3 main.py
  ```

Después de esto, se abrirá la ventana principal de la aplicación.

---

## 5. Conociendo la interfaz

Cuando la aplicación se abre, verás una ventana dividida en dos partes principales:

- La parte superior es donde puedes configurar los parámetros del entrenamiento.
- La parte inferior es donde se mostrarán los gráficos con los resultados.

A continuación, te explico cómo funciona cada parte.

---

## 6. Configuración de los parámetros

Antes de entrenar el modelo, debes ingresar algunos valores para que la aplicación sepa cómo quieres que aprenda.

### Parámetros disponibles:

- **Tasa de aprendizaje:**
  Aquí defines qué tan rápido quieres que el modelo aprenda. Un número muy alto puede hacer que aprenda mal, un número muy bajo puede hacer que tarde demasiado. Se recomienda comenzar con 0.01.

- **Número de épocas:**
  Indica cuántas veces el modelo debe revisar los datos para aprender. Cada revisión completa de los datos se llama época. Puedes probar con 50 épocas.

- **Porcentaje para entrenamiento:**
  Especifica qué cantidad del total de los datos se utilizará para que el modelo aprenda. Lo que quede se usará para probar si el modelo aprendió bien. Por ejemplo, si eliges 70%, el 70% de los datos se usa para aprender y el 30% para evaluar.

-- IMAGEN

---

## 7. Selección de las características

La aplicación permite que elijas las dos características que quieres que el modelo utilice para aprender. Estas características son datos sobre el tumor, como tamaño, textura, perímetro, área, entre otros.

Puedes elegirlas de dos formas:

- **Seleccionando el nombre en las listas desplegables.**
- **Ingresando directamente el número del índice de la característica.**

Si llenas los campos de los índices, estos serán los que se utilizarán, aunque hayas elegido alguna opción en las listas. Si dejas los índices vacíos, se usarán las opciones que seleccionaste en las listas.

-- IMAGEN

---

## 8. Cómo entrenar el modelo

Una vez que hayas configurado los parámetros y elegido las características, presiona el botón **Entrenar modelo**.

La aplicación comenzará el entrenamiento y, al finalizar, mostrará los resultados de manera gráfica.

---

## 9. Entendiendo los resultados

Después de entrenar el modelo, se mostrarán dos gráficos y un texto con la exactitud del modelo.

### Gráfico de errores por época

Este gráfico te muestra cuántos errores tuvo el modelo durante cada una de las repeticiones o épocas del entrenamiento.
Si el modelo va aprendiendo bien, la cantidad de errores debería ir bajando con el tiempo.

-- IMAGEN

---

### Gráfico de frontera de decisión

En este gráfico verás los puntos que representan los datos que el modelo utilizó para aprender.

- Los puntos **rojos** representan tumores malignos.
- Los puntos **azules** representan tumores benignos.

Además, verás una línea recta que es la frontera que el modelo aprendió para separar ambas clases. Las áreas coloreadas indican cómo el modelo clasifica los datos.

En la parte superior del gráfico se muestra el porcentaje de aciertos del modelo, es decir, qué tan bien logró clasificar los datos que no había visto durante el entrenamiento.

-- IMAGEN

---

## 10. Qué hacer si aparece un mensaje de error

El sistema puede mostrar mensajes de error si se ingresan datos incorrectos. Algunos ejemplos son:

- Si escribes un índice que no existe.
- Si repites el mismo número en los dos campos de índice.
- Si dejas los campos vacíos sin seleccionar ninguna opción.

Cuando esto suceda, la aplicación te mostrará un mensaje en la parte de los resultados indicando qué debes corregir.

-- IMAGEN

---

## 11. Recomendaciones para obtener mejores resultados

- Prueba con diferentes combinaciones de características para encontrar las que mejor funcionen.
- Utiliza una tasa de aprendizaje baja como 0.01 para empezar, luego ajusta si es necesario.
- Si ves que el gráfico de errores no baja, intenta cambiar las características o aumentar el número de épocas.
- Recuerda que el modelo utilizado es muy simple y solo puede separar las clases con una línea recta. Si las clases no pueden separarse bien con una línea, es normal que el modelo no logre una exactitud perfecta.

---

## 12. Cómo cerrar la aplicación

Para cerrar la aplicación, simplemente haz clic en el botón de cerrar de la ventana o utiliza la combinación de teclas Alt + F4.

---

## 13. Contacto

Este sistema fue desarrollado como parte del proyecto del curso de Inteligencia Artificial 1.

Autor: Juan Pablo Meza Vielman
Curso: Inteligencia Artificial 1 – Proyecto 2
Docente: Ing. Daniel González
Centro Universitario de Occidente
Año: 2025
