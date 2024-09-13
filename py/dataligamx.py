import pandas as pd

class DataLigamx:
    
    def __init__(self,url):
        self.url=url
        
    def import_data(self):
        #Traemos la data de la url indicada
        data = pd.read_html(self.url, encoding='UTF-8')
        
        #obtenemos la data ya que esta en un arregla de una componente
        data = data[0]
        
        #Creamos las columnas Goles Local y Goles Visitante de la columna Marcador
        data[['Goles Local', 'Goles Visitante']] = data['Marcador'].str.split('–', expand=True)
        
        #Eliminamos la columna Marcador
        data = data.drop('Marcador', axis=1)
        
        import re
        def extraer_numero(cadena):
            numeros = re.findall(r'\b\d+\b', str(cadena))
            if numeros:
                return int(numeros[0])
            else:
                return None
            
        data['Goles Local'] = data['Goles Local'].apply(extraer_numero).fillna(0).astype(int)
        data['Goles Visitante'] = data['Goles Visitante'].apply(extraer_numero).fillna(0).astype(int)
        indices_a_eliminar = [indice for indice, valor in data['Ronda'].iteritems() if pd.isna(valor)]
        data = data.drop(indices_a_eliminar)
        df = data.reset_index(drop=True)
        return df