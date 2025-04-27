import tkinter as tk
from tkinter import ttk
from perceptron import Perceptron
from utils import load_data
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from sklearn.datasets import load_breast_cancer
from matplotlib.lines import Line2D

class PerceptronApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clasificación de Cáncer de Mama con Perceptrón Simple")
        self.root.geometry("900x700")

        data = load_breast_cancer()
        self.feature_names = list(data.feature_names)

        # Frame de controles
        control_frame = ttk.Frame(self.root, padding="10")
        control_frame.pack(side="top", fill="x")

        self.learning_rate = tk.DoubleVar(value=0.01)
        self.epochs = tk.IntVar(value=50)
        self.test_size = tk.DoubleVar(value=0.3)

        self.feature1 = tk.StringVar(value=self.feature_names[0])
        self.feature2 = tk.StringVar(value=self.feature_names[1])
        self.index1 = tk.StringVar()
        self.index2 = tk.StringVar()

        # Configuración de parámetros
        ttk.Label(control_frame, text="Tasa de aprendizaje (η):").grid(row=0, column=0)
        ttk.Entry(control_frame, textvariable=self.learning_rate).grid(row=0, column=1)

        ttk.Label(control_frame, text="Número de épocas:").grid(row=1, column=0)
        ttk.Entry(control_frame, textvariable=self.epochs).grid(row=1, column=1)

        ttk.Label(control_frame, text="Porcentaje de entrenamiento:").grid(row=2, column=0)
        ttk.Entry(control_frame, textvariable=self.test_size).grid(row=2, column=1)

        # Selección por nombre
        ttk.Label(control_frame, text="Seleccionar característica 1 (x):").grid(row=3, column=0)
        ttk.Combobox(control_frame, textvariable=self.feature1, values=self.feature_names, state="readonly").grid(row=3, column=1)

        ttk.Label(control_frame, text="Seleccionar característica 2 (y):").grid(row=4, column=0)
        ttk.Combobox(control_frame, textvariable=self.feature2, values=self.feature_names, state="readonly").grid(row=4, column=1)

        # Selección por índice
        ttk.Label(control_frame, text="(Opcional) Índice de característica 1 (x):").grid(row=5, column=0)
        ttk.Entry(control_frame, textvariable=self.index1).grid(row=5, column=1)

        ttk.Label(control_frame, text="(Opcional) Índice de característica 2 (y):").grid(row=6, column=0)
        ttk.Entry(control_frame, textvariable=self.index2).grid(row=6, column=1)

        ttk.Button(control_frame, text="Entrenar modelo", command=self.train_model).grid(row=7, column=0, columnspan=2, pady=10)

        # Frame de gráficos con scroll
        self.canvas = tk.Canvas(self.root)
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def train_model(self):
        # Limpiar gráficos anteriores
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Determinar si usar índice o nombre
        try:
            idx1 = int(self.index1.get()) if self.index1.get() else list(self.feature_names).index(self.feature1.get())
            idx2 = int(self.index2.get()) if self.index2.get() else list(self.feature_names).index(self.feature2.get())
        except ValueError:
            label_error = ttk.Label(self.scrollable_frame, text="Error: Índice inválido o característica no encontrada.")
            label_error.pack(pady=10)
            return

        X_train, X_test, y_train, y_test, feature_names = load_data(idx1, idx2, self.test_size.get())

        perceptron = Perceptron(input_size=2, learning_rate=self.learning_rate.get())
        print("Tasa de aprendizaje enviada al Perceptron:", self.learning_rate.get())
        errors = perceptron.train(X_train, y_train, self.epochs.get())

        # Gráfico de errores
        fig1, ax1 = plt.subplots()
        ax1.plot(range(1, self.epochs.get() + 1), errors)
        ax1.set_xlabel("Épocas")
        ax1.set_ylabel("Errores")
        ax1.set_title("Errores por época durante el entrenamiento")

        canvas1 = FigureCanvasTkAgg(fig1, master=self.scrollable_frame)
        canvas1.draw()
        canvas1.get_tk_widget().pack(pady=10)

        correct = sum(perceptron.predict(xi) == yi for xi, yi in zip(X_test, y_test))
        accuracy = correct / len(y_test)

        fig2, ax2 = plt.subplots()
        plot_decision_boundary(perceptron, X_train, y_train, feature_names, ax2, accuracy)

        canvas2 = FigureCanvasTkAgg(fig2, master=self.scrollable_frame)
        canvas2.draw()
        canvas2.get_tk_widget().pack(pady=10)

        label_accuracy = ttk.Label(self.scrollable_frame, text=f"Exactitud en test: {accuracy * 100:.2f}%")
        label_accuracy.pack(pady=10)

def plot_decision_boundary(perceptron, X, y, feature_names, ax, accuracy):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                         np.linspace(y_min, y_max, 200))
    Z = np.array([perceptron.predict([x, y]) for x, y in zip(xx.ravel(), yy.ravel())])
    Z = Z.reshape(xx.shape)

    ax.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.Paired)
    colors = ['red' if label == -1 else 'blue' for label in y]
    ax.scatter(X[:, 0], X[:, 1], c=colors, edgecolor='k')

    ax.set_xlabel(feature_names[0])
    ax.set_ylabel(feature_names[1])
    ax.set_title(f'Frontera de decisión y datos (Accuracy: {accuracy * 100:.2f}%)')


    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='Maligno (-1)', markerfacecolor='red', markersize=8, markeredgecolor='k'),
        Line2D([0], [0], marker='o', color='w', label='Benigno (1)', markerfacecolor='blue', markersize=8, markeredgecolor='k')
    ]
    ax.legend(handles=legend_elements, loc='best')

if __name__ == "__main__":
    root = tk.Tk()
    app = PerceptronApp(root)
    root.mainloop()
