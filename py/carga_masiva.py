import requests
import pandas as pd
import random
import string

#
USERNAME = f'gta_qas@gta.com.mx'
PASSWORD = f'wW94;6mog[hc'
BASE_URL = f'http://18.217.164.177:8001'

def get_token(usr, password):
    json_data  = {
                "username":  usr,
                "password": password
    }
    url = BASE_URL + '/api/token/'
    response = requests.post(url, data=json_data)
    if response.status_code == 200:
        response_json = response.json()
        token = response_json.get('access')
        return token

def alta_empleado(no_empleado,primer_nombre, apellido_paterno, apellido_materno, email_personal,email_empresa, rfc, curp):
    json_data =  {
            "no_empleado": no_empleado,
            "nombres": primer_nombre,
            "apellido_paterno":apellido_paterno,
            "apellido_materno": apellido_materno,
            "estado_fsm": "alta",
            "no_celular": "5551234567",
            "email_personal": email_personal,
            "email_empresa": email_empresa,
            "rfc":rfc,
            "curp": curp,
            "tipo_nomina": 1,
            "clave_internacional": "+52",
            "clabe_interbancaria": "777777777777777777",
            "no_cuenta": "7777777777777",
            "no_seguro_social": "7777777777777",
            "banco_cuenta": "3",
            "activo": True,
            "imagen": None,
            "fecha_ingreso": None,
            "fecha_baja": None,
            "fecha_creacion": "2024-11-12T13:47:38.482400-06:00",
            "fecha_modificacion": "2024-11-12T13:47:38.482422-06:00",
    }
    
    url = BASE_URL + '/api/empleados/'
    token = get_token(USERNAME,PASSWORD)
    headers = {
            'Content-Type': 'application/json',
            'Authorization':  f"Bearer {token}"
            }
    print(headers)
    response = requests.post(url, 
                             json=json_data,
                             headers=headers
                             )

    if response.status_code == 200:
        response_json = response.json()
        return response_json
    else:
        return response.json()


# 1. Vas a leer el csv
# 2. PAra cada linea vas a obtener los datos empleado
# 3. para empleado mandas a llamar la funcion alta empleado pasandole los valores que le correspoden

#df_empleados = pd.read_csv("empleados.csv")

def generar_rfc_unico(primer_nombre, apellido_paterno, apellido_materno):
    # Tomar las primeras letras del apellido paterno, materno y nombre
    rfc_base = (
        apellido_paterno[:2].upper() +  # Primeras 2 letras del apellido paterno
        apellido_materno[:1].upper() +  # Primera letra del apellido materno
        primer_nombre[:1].upper()       # Primera letra del nombre
    )
    
    # Generar un sufijo aleatorio de 6 dígitos
    sufijo = ''.join(random.choices(string.digits, k=6))
    
    # Combinar para formar el RFC completo
    rfc = (rfc_base + sufijo).ljust(13, 'X')  # Rellenar con 'X' si es necesario
    
    # Verificar que el RFC no esté duplicado
    # while rfc in rfc_existentes:
    #     sufijo = ''.join(random.choices(string.digits, k=6))
    #     rfc = (rfc_base + sufijo).ljust(13, 'X')
    
    # Agregar el RFC a la lista de existentes
    # rfc_existentes.add(rfc)
    return rfc

df_empleados = pd.read_csv("/home/emmanuel/Descargas/Estructura_Organizacional.csv")
df_empleados
df_empleados[["apellido_paterno", "apellido_materno", "nombre"]] = df_empleados["NOMBRE"].str.split(n=2, expand=True)
df_empleados.drop(columns=["NOMBRE"], inplace=True)

json_empleados = df_empleados.to_dict(orient="records")
i = 8
for empleado in json_empleados:
    print(empleado)
    print(empleado.get("nombre"))

    rfc = generar_rfc_unico(
        primer_nombre=empleado.get("nombre"),
        apellido_paterno=empleado.get("apellido_paterno"),
        apellido_materno=empleado.get("apellido_materno"),
        
    )

    respuesta = alta_empleado(
        no_empleado=i,
        primer_nombre=empleado.get("nombre"),
        apellido_materno=empleado.get("apellido_materno"),
        apellido_paterno=empleado.get("apellido_paterno"),
        email_personal=empleado.get("correo"),
        email_empresa=empleado.get("correo1"),
        rfc=rfc,
        curp=rfc,
        
    )
    i = i + 1
 
#for linea in file:
#    respuesta = alta_empleado(
#        no_empleado=,
#        primer_nombre=,
#        apellido_materno=,
#        apellido_paterno=,
#        rfc=,
#        curp=
#    )
    print(respuesta)
#
