# Clasificación de Cáncer de Mama con Perceptrón Simple

## 1. Descripción General

Este proyecto tiene como objetivo desarrollar un sistema de clasificación de tumores mamarios en benignos o malignos, utilizando un Perceptrón Simple implementado desde cero en el lenguaje de programación Python. El desarrollo del sistema cumple con las restricciones del curso de Inteligencia Artificial 1, las cuales prohíben el uso de librerías de redes neuronales y exigen la construcción propia del modelo.

La clasificación se realiza a partir del análisis de dos características extraídas del conjunto de datos Breast Cancer Wisconsin, que contiene mediciones físicas de núcleos celulares obtenidas por imágenes médicas. A través de una interfaz gráfica, el usuario puede seleccionar las características que desea utilizar, ajustar los parámetros del modelo, entrenar el perceptrón y visualizar los resultados obtenidos en el proceso.

El sistema permite observar el comportamiento de aprendizaje del perceptrón en tiempo real, mostrando la frontera de decisión aprendida, la evolución de los errores durante el entrenamiento y la exactitud final alcanzada. Esto facilita la comprensión del funcionamiento del modelo y sus limitaciones, en especial cuando se aplican a problemas de clasificación binaria con fronteras lineales.

## 2. Estructura del Proyecto

El proyecto está organizado en los siguientes archivos:

```
perceptron_cancer/
│
├── main.py               Control principal de la aplicación, manejo de la interfaz gráfica y del flujo de ejecución.
├── perceptron.py         Implementación de la clase Perceptron con los métodos de entrenamiento y predicción.
├── utils.py              Funciones auxiliares para la carga del conjunto de datos y la preparación del mismo.
├── requirements.txt      Archivo que define las librerías necesarias para la ejecución del proyecto.
```

## 3. Detalles Técnicos del Perceptron Simple

El perceptrón es una red neuronal de una sola neurona que permite resolver problemas de clasificación cuando las clases son linealmente separables. Su funcionamiento se basa en combinar de manera ponderada las entradas mediante pesos ajustables, y aplicar una función de activación que determina la salida final del modelo.

### Función de activación del perceptrón

El perceptrón calcula la salida mediante la siguiente ecuación:

<img width="245" alt="image" src="https://github.com/user-attachments/assets/0b2d5713-e7e2-4def-9363-eff986d8db2a" />


donde:

- w0 es el término independiente o sesgo
- wi son los pesos asociados a cada entrada xi
- y es la salida generada por el perceptrón, la cual toma los valores de 1 o -1

La función de activación utilizada es la función signo, que retorna 1 si el resultado es positivo y -1 si es negativo.

### Regla de actualización de pesos

Durante el entrenamiento, el perceptrón ajusta sus pesos utilizando la siguiente regla de aprendizaje:

<img width="203" alt="image" src="https://github.com/user-attachments/assets/b87968b1-31a8-4288-8520-4b39605c16be" />


donde:

- η es la tasa de aprendizaje, un valor positivo configurado por el usuario
- d es la etiqueta deseada o valor real de la muestra
- y es la salida calculada por el perceptrón
- xj es el valor de la entrada correspondiente

El proceso de ajuste se repite durante varias iteraciones o épocas, hasta completar el número máximo de épocas definido por el usuario.

## 4. Carga y Preparación del Dataset

El conjunto de datos utilizado es el Breast Cancer Wisconsin Diagnostic Dataset, disponible en la librería scikit-learn. Este dataset contiene 569 muestras, cada una con 30 características numéricas que describen aspectos físicos del núcleo celular, como tamaño, textura, perímetro y área.

El proyecto realiza la carga de los datos mediante la función load_breast_cancer y transforma las etiquetas originales, que son cero para maligno y uno para benigno, a los valores -1 para maligno y 1 para benigno, los cuales son los valores requeridos por la implementación del perceptrón.

El usuario puede seleccionar dos características del dataset para el entrenamiento y la evaluación. La selección se realiza ya sea por índice numérico o por nombre, y si el usuario ingresa ambos, el sistema prioriza los índices. Los datos se dividen en dos conjuntos: uno para entrenamiento y otro para prueba. El porcentaje de esta división es configurable desde la interfaz.

## 5. Entrenamiento y Evaluación del Modelo

El entrenamiento consiste en ajustar los pesos del perceptrón a lo largo de las épocas configuradas. En cada época, se recorren todas las muestras del conjunto de entrenamiento, y si la predicción del modelo es incorrecta, se actualizan los pesos siguiendo la regla de aprendizaje descrita anteriormente.

La evaluación del modelo se realiza utilizando el conjunto de prueba. El desempeño se mide a través de la exactitud, la cual indica el porcentaje de muestras que fueron correctamente clasificadas por el modelo.

La fórmula de la exactitud es la siguiente:

\[
\text{Accuracy} = \frac{\text{Número de predicciones correctas}}{\text{Total de muestras de prueba}} \times 100
\]

## 6. Visualización del Proceso

El sistema permite visualizar los siguientes elementos:

- Gráfico de errores por época, donde se observa la evolución del número de errores durante el entrenamiento. Esto permite analizar si el modelo está aprendiendo correctamente o si el aprendizaje se ha estancado.
- Scatter plot con la frontera de decisión, que representa las dos clases del problema. Los puntos se muestran con colores diferenciados: azul para benignos y rojo para malignos. La línea recta es la frontera de decisión aprendida por el perceptrón, y la zona de cada clase está coloreada según la predicción del modelo.
- Leyenda que indica las clases, junto con la exactitud final calculada, la cual también se muestra en el título del gráfico.

## 7. Interfaz Gráfica

La interfaz gráfica fue desarrollada utilizando Tkinter y tiene como propósito facilitar la interacción del usuario con el sistema sin necesidad de modificar el código. Los elementos principales de la interfaz son los siguientes:

- Campos para ingresar la tasa de aprendizaje, el número de épocas y el porcentaje de entrenamiento.
- Combobox para seleccionar las características por nombre.
- Entradas numéricas para seleccionar las características por índice.
- Botón que inicia el entrenamiento del modelo.
- Área para visualizar los gráficos generados, con soporte de scroll vertical para facilitar la navegación en ventanas pequeñas.

El diseño de la interfaz permite alternar entre selección por nombre o por índice, priorizando el índice si el usuario lo ingresa.

## 8. Validaciones Implementadas

El sistema cuenta con las siguientes validaciones:

- Verificación de que los índices ingresados estén dentro del rango permitido del dataset, que es de cero a veintinueve.
- Prioridad a los índices si se ingresan, incluso si también se seleccionan nombres en los combobox.
- Mensaje de error si los índices no son válidos o si hay conflictos en la selección de características.

Estas validaciones aseguran la correcta operación del sistema y previenen errores por configuraciones inadecuadas.

## 9. Requisitos del Sistema

El proyecto requiere las siguientes herramientas de software:

- Python versión 3.8 o superior
- Librerías:
  - numpy
  - matplotlib
  - scikit-learn
  - tkinter, incluido por defecto en Python

Las dependencias necesarias pueden instalarse ejecutando el siguiente comando:

```
pip install -r requirements.txt
```

## 10. Ejecución del Proyecto

Para ejecutar la aplicación, se utilizan los siguientes comandos según el sistema operativo:

En Linux o macOS:

```
python3 main.py
```

En Windows:

```
python main.py
```

El sistema también permite generar un ejecutable mediante PyInstaller, lo que facilita la ejecución sin necesidad de instalar Python.

## 11. Consideraciones Técnicas y Limitaciones

El perceptrón simple es un modelo que únicamente puede aprender fronteras lineales. Si el conjunto de datos no es linealmente separable, el modelo no podrá alcanzar una clasificación perfecta. El dataset Breast Cancer Wisconsin no es completamente linealmente separable, por lo que el modelo puede presentar errores en la clasificación, especialmente cuando las clases se traslapan.

El sistema permite experimentar con diferentes combinaciones de características, lo que puede mejorar o empeorar la exactitud dependiendo de la selección. Sin embargo, debido a la naturaleza del perceptrón, la frontera de decisión siempre será una línea recta, sin capacidad para adaptarse a fronteras curvas o más complejas.

## 12. Posibles Extensiones y Mejoras

El sistema puede ser extendido en el futuro con las siguientes mejoras:

- Implementación de perceptrón multicapa para permitir la clasificación de datos no linealmente separables.
- Inclusión de validación cruzada para obtener mediciones más robustas del rendimiento.
- Cálculo de métricas adicionales como precisión, recall y matriz de confusión.
- Exportación de los resultados del entrenamiento a formatos como CSV o PDF.
- Automatización de la búsqueda de las mejores combinaciones de características mediante algoritmos de selección de variables.

## 13. Créditos

Autor: Juan Pablo Meza Vielman
Curso: Inteligencia Artificial 1 – Proyecto 2
Docente: Ing. Daniel González
Universidad: Centro Universitario de Occidente
Año: 2025
