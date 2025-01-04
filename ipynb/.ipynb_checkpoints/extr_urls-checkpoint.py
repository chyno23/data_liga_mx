import pandas as pd
import numpy as np

def extr_url_primer(urlpath):

    data = pd.read_html('https://fbref.com/es/comps/9/2019-2020/horario/Marcadores-y-partidos-de-2019-2020-Premier-League')
    data = data[0]
    for i in range(0, 2):
        urlname = '20' + str(i) + '-' + '20' + str(i + 1) + '/horario/Marcadores-y-partidos-de-202' + str(i) + '-202' + str(i + 1) + '-Premier-League'
        url = urlpath + urlname
    
    
        seasons_data = pd.read_html(url)
        seadons_data = seasons_data[0]
        data = pd.concat([data, seasons_data], axis=0)
        time.sleep(5)  # Esperar 5 segundos entre solicitudes
    
    data.head()


