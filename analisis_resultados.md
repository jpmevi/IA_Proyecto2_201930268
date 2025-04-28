# Análisis de Resultados

**Proyecto: Clasificación de Cáncer de Mama con Perceptrón Simple**
**Curso: Inteligencia Artificial 1**
**Autor: Juan Pablo Meza Vielman**
**Docente: Ing. Daniel González**
**Centro Universitario de Occidente, 2025**

---

## 1. Objetivo del Análisis

En esta sección presento el análisis detallado de los resultados obtenidos durante la experimentación del proyecto, cuyo propósito fue implementar y evaluar un modelo de Perceptrón Simple para la clasificación de tumores de mama en dos categorías: benignos o malignos.

El objetivo de las pruebas fue comprender cómo influyen los distintos parámetros del algoritmo en el desempeño del modelo, particularmente en la calidad del aprendizaje, la velocidad de convergencia y la precisión final. Para lograr esto, decidí variar de manera controlada los siguientes hiperparámetros:

- La tasa de aprendizaje (η)
- El número de épocas o iteraciones de entrenamiento
- El porcentaje de datos que se destinan al entrenamiento frente a los que se dejan para prueba

Cada uno de estos parámetros fue modificado de manera independiente para observar claramente su impacto, manteniendo los demás fijos durante cada experimento. Esto me permitió analizar de forma puntual cómo cada uno de estos elementos afecta el proceso de aprendizaje y la capacidad de generalización del modelo.

---

## 2. Análisis de la Tasa de Aprendizaje (η)

### Parámetros utilizados:

- Número de épocas: 50
- Porcentaje de entrenamiento: 30%
- Tasa de aprendizaje: 1, 0.5, 0.1, 0.05, 0.01

Durante esta serie de pruebas, lo que buscaba era observar cómo diferentes valores de la tasa de aprendizaje afectan la manera en que el modelo ajusta los pesos y, por consecuencia, cómo cambia el comportamiento del error y la precisión final alcanzada.

<img width="1005" alt="image" src="https://github.com/user-attachments/assets/c1366824-2131-4c79-985a-5981581d8704" />

<img width="1028" alt="image" src="https://github.com/user-attachments/assets/ca5d63ff-a37b-4b54-96e6-69999aa6ecfe" />

<img width="993" alt="image" src="https://github.com/user-attachments/assets/63217dad-44c4-4a13-a033-ad64dff23bea" />

<img width="987" alt="image" src="https://github.com/user-attachments/assets/96af78d6-696c-4f04-9000-4b9e24c3f948" />

<img width="1034" alt="image" src="https://github.com/user-attachments/assets/9c022fc1-9096-4e20-a4f5-d697a11ad4f7" />

<img width="1024" alt="image" src="https://github.com/user-attachments/assets/496c5ab2-7176-472f-84c4-4b2aa8806340" />

<img width="1027" alt="image" src="https://github.com/user-attachments/assets/b3f145a5-9bb8-4f38-b17b-001b057c013a" />

<img width="1009" alt="image" src="https://github.com/user-attachments/assets/54a7d5bc-d02d-4816-9771-251dab4182e2" />

<img width="1005" alt="image" src="https://github.com/user-attachments/assets/7202f179-f38b-4e9b-b3d3-3ae116074e87" />


A continuación muestro una tabla resumen con los resultados aproximados obtenidos en términos de accuracy y algunas observaciones generales sobre cada caso:

| Tasa de Aprendizaje | Accuracy Aproximada | Observación General                                                                                                                                            |
| ------------------- | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1                   | 81.87%              | Las actualizaciones son muy rápidas, pero la frontera de decisión no siempre es la mejor. Se observa que la precisión no es la más alta.                       |
| 0.5                 | 85.38%              | Se obtiene un ajuste más fino que con η = 1. La reducción de errores es más estable y la frontera mejora notablemente.                                         |
| 0.1                 | 91.23%              | Aquí se alcanza uno de los mejores resultados. La precisión aumenta y el modelo logra una buena estabilidad.                                                   |
| 0.05                | 90.64%              | Muy similar a la anterior. El comportamiento es estable y el rendimiento es alto, aunque ya no hay una mejora tan significativa respecto a η = 0.1.            |
| 0.01                | 89.47%              | El aprendizaje se vuelve muy lento. Aunque sigue siendo un resultado aceptable, la baja tasa puede llevar a un estancamiento si no se usan suficientes épocas. |

### Reflexión personal sobre estos resultados:

Algo que pude confirmar en esta parte del análisis es que la tasa de aprendizaje es un parámetro sumamente sensible. Cuando es demasiado alta, el modelo ajusta los pesos de manera muy agresiva, lo que puede provocar que la frontera de decisión "salte" de un lado a otro y no se logre una buena convergencia. En cambio, cuando es demasiado baja, el proceso se vuelve muy lento y el modelo necesita muchas más iteraciones para poder aprender correctamente.

En mis pruebas, el mejor equilibrio entre velocidad de aprendizaje y estabilidad se consiguió con tasas intermedias, especialmente entre 0.05 y 0.1. Estas tasas permiten que el modelo avance de manera gradual, pero sin caer en actualizaciones demasiado pequeñas que frenen el progreso.

---

## 3. Análisis del Número de Épocas

### Parámetros utilizados:

- Tasa de aprendizaje: 1
- Porcentaje de entrenamiento: 30%
- Épocas: 5, 10, 50, 100, 200

En esta parte del análisis me enfoqué en entender cuánto tiempo de entrenamiento necesita el modelo para lograr una buena convergencia. Cambié el número de épocas, manteniendo la tasa de aprendizaje fija, para poder observar cómo evoluciona el error a lo largo del proceso.

| Número de Épocas | Tendencia de los Errores                                                                                                                               | Comportamiento observado |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| 5                | Alta dispersión, sin reducción clara del error. Las pocas iteraciones no permiten al modelo aprender adecuadamente.                                    |
| 10               | Aún se observa mucha variación y falta de estabilidad. Todavía es insuficiente para lograr un aprendizaje efectivo.                                    |
| 50               | Empiezan a notarse tendencias hacia la reducción de errores, aunque con ciertas oscilaciones.                                                          |
| 100              | Se observa una mejora considerable, con una mayor estabilidad, aunque siguen presentes algunas pequeñas fluctuaciones.                                 |
| 200              | El comportamiento es más estable y consistente, pero las fluctuaciones continúan debido a la naturaleza del Perceptrón y la linealidad de la frontera. |

### Reflexión personal sobre estos resultados:

Una de las cosas más claras que pude observar es que no basta con pocas épocas para que el perceptrón logre una buena clasificación. Cuando se tienen menos de 50 iteraciones, los pesos no logran adaptarse de forma adecuada y el modelo no aprende bien los patrones de los datos.

Aumentar las épocas permite darle más oportunidades al perceptrón de ajustar sus pesos correctamente, aunque es importante tener presente que, debido a las limitaciones del propio algoritmo (que solo trabaja con fronteras lineales), existe un punto a partir del cual aumentar las épocas ya no mejora tanto el rendimiento. Esto fue especialmente evidente después de las 100 épocas.

---

## 4. Análisis del Porcentaje de Entrenamiento

### Parámetros utilizados:

- Tasa de aprendizaje: 0.01
- Número de épocas: 50
- Porcentaje de entrenamiento: 10%, 20%, 30%, 50%

En esta serie de experimentos lo que quise analizar fue cómo influye el tamaño del conjunto de entrenamiento en la capacidad del modelo para aprender y, al mismo tiempo, cómo afecta la cantidad de datos reservados para la validación o prueba.

| Porcentaje de Entrenamiento | Accuracy Aproximada | Observación                                                                                                                                         |
| --------------------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| 10%                         | 92.98%              | A pesar de la precisión alta, esta configuración entrena con muy pocos datos, lo que puede generar sobreajuste y baja generalización.               |
| 20%                         | 87.72%              | Se mejora la representación de los datos, aunque la variabilidad en los resultados todavía es algo alta.                                            |
| 30%                         | 89.47%              | Aquí se logra un buen equilibrio entre cantidad de datos para aprender y datos para evaluar el desempeño real del modelo.                           |
| 50%                         | 87.72%              | Aunque hay más datos para entrenar, el menor porcentaje de datos para prueba puede limitar la capacidad de evaluar correctamente la generalización. |

### Reflexión personal sobre estos resultados:

Algo interesante que descubrí es que tener más datos para entrenar no siempre garantiza mejores resultados si se descuida la proporción de datos reservados para validación. Cuando se entrena con muy pocos ejemplos, el modelo puede ajustarse demasiado a esos casos específicos, pero luego falla al enfrentarse a nuevas muestras. Por otro lado, si se reservan demasiados datos para prueba, se limita la capacidad de aprendizaje.

En mis pruebas, el balance más adecuado estuvo entre 30% y 50% de entrenamiento, donde se logró una buena estabilidad y precisión sin sacrificar la capacidad de evaluación.

---

## 5. Comportamiento de la Frontera de Decisión

Durante las pruebas, también pude observar cómo cambia la forma de la frontera de decisión dependiendo de los parámetros que configuré. Como el Perceptrón Simple solo permite crear fronteras lineales, en todos los casos la línea de separación fue recta.

Sin embargo, pude notar que:

- Cuando la tasa de aprendizaje es muy alta, la frontera tiende a ser más inestable y, en algunos casos, demasiado inclinada o mal
