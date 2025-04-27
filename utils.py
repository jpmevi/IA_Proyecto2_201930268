from sklearn.datasets import load_breast_cancer
import numpy as np
from sklearn.model_selection import train_test_split

def load_data(feature1_index=0, feature2_index=1, test_size=0.3):
    """
    Carga el dataset de cáncer de mama y selecciona dos características.
    """
    data = load_breast_cancer()
    X = data.data[:, [feature1_index, feature2_index]]
    y = data.target

    # Cambia etiquetas de 0 (maligno) y 1 (benigno) a -1 y 1
    y = np.where(y == 0, -1, 1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    feature_names = (data.feature_names[feature1_index], data.feature_names[feature2_index])

    return X_train, X_test, y_train, y_test, feature_names
