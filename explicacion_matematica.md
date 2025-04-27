# Explicación Matemática

**Proyecto: Clasificación de Cáncer de Mama con Perceptrón Simple**

**Curso: Inteligencia Artificial 1**
**Autor: Juan Pablo Meza Vielman**
**Docente: Ing. Daniel González**
**Centro Universitario de Occidente, 2025**

---

## 1. Introducción

El presente documento tiene como objetivo explicar de manera formal el funcionamiento matemático del modelo de clasificación utilizado en el proyecto. Este modelo corresponde a un **Perceptrón Simple**, una red neuronal de una sola neurona, cuyo propósito es resolver problemas de clasificación binaria en los casos en que las clases pueden ser separadas mediante una frontera lineal.

En este proyecto, el perceptrón se utiliza para clasificar tumores mamarios como **benignos** o **malignos** a partir del análisis de dos características extraídas del conjunto de datos Breast Cancer Wisconsin. La elección de este modelo responde a los requerimientos del proyecto de implementar una red neuronal desde cero, sin el uso de librerías especializadas en aprendizaje profundo.

---

## 2. El Perceptrón Simple

El perceptrón simple fue propuesto por Frank Rosenblatt en 1958 como un modelo de red neuronal capaz de aprender reglas de decisión lineales mediante el ajuste automático de los pesos asociados a las entradas.

Matemáticamente, el perceptrón calcula una combinación lineal de las entradas y luego aplica una función de activación para determinar la clase de salida.

Dado un vector de entrada \( x = (x_1, x_2, \dots, x_n) \) y un vector de pesos \( w = (w_1, w_2, \dots, w_n) \), junto con un sesgo \( w_0 \), la salida del perceptrón se calcula de la siguiente forma:

\[
z = w*0 + \sum*{i=1}^{n} w_i x_i
\]

La salida \( y \) se obtiene aplicando la función de activación tipo escalón o signo:

\[
y =
\begin{cases}
1, & \text{si } z \geq 0 \\
-1, & \text{si } z < 0
\end{cases}
\]

Donde:

- \( x_i \) representa cada una de las entradas del modelo.
- \( w_i \) es el peso asociado a cada entrada.
- \( w_0 \) es el sesgo o bias, que permite desplazar la frontera de decisión.
- \( y \) es la salida predicha por el modelo, que puede ser 1 o -1.

---

## 3. Función de Activación

La función de activación utilizada es la función signo o escalón, que es una función no continua, definida como:

\[
\text{sign}(z) =
\begin{cases}
1, & \text{si } z \geq 0 \\
-1, & \text{si } z < 0
\end{cases}
\]

Esta función permite tomar una decisión binaria sobre la clase a la que pertenece una muestra, basándose en el valor de la combinación lineal de las entradas.

---

## 4. Regla de Aprendizaje del Perceptrón

El aprendizaje del perceptrón consiste en ajustar los pesos de manera que el modelo pueda clasificar correctamente las muestras del conjunto de entrenamiento.

Dado un conjunto de datos con entradas \( x^{(j)} \) y salidas deseadas \( d^{(j)} \), el modelo calcula la salida \( y^{(j)} \). Si la salida es incorrecta, es decir, si \( y^{(j)} \neq d^{(j)} \), los pesos se actualizan de acuerdo con la siguiente regla:

\[
w_i = w_i + \eta (d^{(j)} - y^{(j)}) x_i
\]

\[
w_0 = w_0 + \eta (d^{(j)} - y^{(j)})
\]

Donde:

- \( \eta \) es la **tasa de aprendizaje**, un número positivo que controla la magnitud de los cambios en los pesos.
- \( d^{(j)} \) es la salida deseada para la muestra \( j \).
- \( y^{(j)} \) es la salida calculada por el modelo para la muestra \( j \).
- \( w_i \) es el peso de la entrada \( i \).
- \( x_i \) es la entrada correspondiente.

La actualización de los pesos tiene como propósito reducir el error cometido por el modelo, de manera que, con el paso de las iteraciones, el perceptrón logre clasificar correctamente la mayor cantidad de muestras posible.

---

## 5. Condición de Parada

El entrenamiento del perceptrón finaliza cuando ocurre alguna de las siguientes condiciones:

- Se ha alcanzado el número máximo de épocas o iteraciones definido por el usuario.
- Se logra que el modelo no cometa errores en el conjunto de entrenamiento (en el caso ideal de separación lineal perfecta).

En este proyecto, se utilizó como criterio de parada el número máximo de épocas, configurado por el usuario a través de la interfaz gráfica.

---

## 6. Cálculo de la Exactitud del Modelo

Una vez finalizado el entrenamiento, se evalúa el desempeño del modelo mediante el cálculo de la **exactitud**. Esta métrica indica el porcentaje de muestras del conjunto de prueba que fueron clasificadas correctamente por el modelo.

La fórmula utilizada es la siguiente:

\[
\text{Exactitud} = \frac{\text{Número de predicciones correctas}}{\text{Total de muestras de prueba}} \times 100
\]

Donde:

- Las predicciones correctas son aquellas en las que la salida calculada \( y \) coincide con la salida deseada \( d \).
- El total de muestras de prueba corresponde a las muestras que no fueron utilizadas en el proceso de entrenamiento.

La exactitud es una medida global del rendimiento del modelo, pero es importante tener presente que no ofrece información detallada sobre el comportamiento en cada clase. Para análisis más completos se podrían incluir otras métricas como precisión, sensibilidad y matriz de confusión, aunque no forman parte de los alcances de este proyecto.

---

## 7. Interpretación de la Frontera de Decisión

El perceptrón simple genera una **frontera de decisión lineal** en el espacio de las características seleccionadas. Esta frontera es una línea recta definida por la ecuación:

\[
w_0 + w_1 x_1 + w_2 x_2 = 0
\]

Al despejar \( x_2 \):

\[
x_2 = -\frac{w_1}{w_2} x_1 - \frac{w_0}{w_2}
\]

Esta ecuación describe la recta que divide el espacio de las dos clases. Las muestras que se encuentren a un lado de la recta serán clasificadas como una clase, mientras que las que se encuentren al otro lado serán clasificadas como la otra.

Si el problema no es perfectamente separable mediante una línea recta, el perceptrón no podrá encontrar una frontera que separe correctamente todas las muestras, lo cual es una limitación natural de este tipo de modelo.

---

## 8. Limitaciones Matemáticas del Perceptrón Simple

El perceptrón simple presenta las siguientes limitaciones desde el punto de vista matemático:

- Solo es capaz de aprender fronteras de decisión lineales. Si las clases no son linealmente separables, el modelo no podrá encontrar una solución perfecta.
- No puede resolver problemas que requieren fronteras curvas o más complejas, como el problema del XOR.
- La convergencia del algoritmo está garantizada únicamente si el conjunto de datos es linealmente separable.

Estas limitaciones fueron aceptadas dentro del alcance del proyecto, dado que el objetivo principal es comprender el funcionamiento y el proceso de aprendizaje del perceptrón simple, no alcanzar el máximo desempeño posible.

---

## 9. Conclusión

El perceptrón simple es un modelo de red neuronal de una sola capa que permite resolver problemas de clasificación binaria siempre que las clases puedan ser separadas mediante una línea recta. Su funcionamiento se basa en la combinación lineal de las entradas, la aplicación de una función de activación binaria y el ajuste de los pesos a través de una regla de aprendizaje supervisada.

Aunque presenta limitaciones importantes en cuanto a la complejidad de las fronteras de decisión que puede aprender, su simplicidad y facilidad de interpretación lo convierten en una herramienta útil para fines educativos y para el entendimiento de los fundamentos del aprendizaje automático.

Este proyecto demuestra la aplicación del perceptrón simple a la clasificación de tumores mamarios, cumpliendo con los requisitos del curso y permitiendo visualizar de forma clara tanto el proceso de aprendizaje como los resultados obtenidos.
