import pandas as pd
import matplotlib.pyplot as plt

class GraficasFutbol:
    def __init__(self, data, equipo, estado):
        self.data = data.copy()
        self.equipo = equipo
        self.estado = estado

    def sub_data_para_graficar(self):
        if self.estado == 'Visitante':
            sub_dataframe_visitante = self.data[self.data['Visitante'] == self.equipo].reset_index()
            return sub_dataframe_visitante
        elif self.estado == 'Local':
            sub_dataframe_local = self.data[self.data['Local'] == self.equipo].reset_index()
            return sub_dataframe_local
        else:
            raise ValueError("El estado debe ser 'Visitante' o 'Local'.")

    def configurar_y_mostrar_grafico(self, ax, xlabel, ylabel, title):
        # Configurar etiquetas y título
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        
        #Mostrar La leyenda
        ax.legend()
        
        # Mostrar el gráfico
        plt.show()

    def grafica_total_goles(self, ax=None):
        if ax is None:
            fig, ax = plt.subplots(figsize=(20,6))
            
        data = self.sub_data_para_graficar()

        # Calcular los goles totales por partido
        data['Goles Totales'] = data['Goles Local'] + data['Goles Visitante']

        # Crear un gráfico de barras con los goles totales por encuentro
        ax.bar(data.index, data['Goles Totales'], color='purple', alpha=0.7)

        self.configurar_y_mostrar_grafico(ax, 'Encuentro', 'Goles Totales por Encuentro',
                                          'Goles Totales por Encuentro de la Liga')

    def grafica_local_visita(self, ax=None, figsize=(20, 6)):
        if ax is None:
            fig, ax = plt.subplots(figsize=figsize)
        
        data = self.sub_data_para_graficar()
        
        # Barra para los goles del equipo local
        ax.bar(data.index, data['Goles Local'], label='Local', color='red', alpha=0.7)

        # Barra para los goles del equipo visitante
        ax.bar(data.index, data['Goles Visitante'], label='Visitante', color='green', alpha=0.7)

        self.configurar_y_mostrar_grafico(ax, 'Encuentro', 'Goles',self.equipo)
