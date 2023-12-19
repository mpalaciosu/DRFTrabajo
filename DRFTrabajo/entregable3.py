import datetime as dt 
from datetime import timedelta, datetime
import calendar
from datetime import date

def calcular_uf(last_uf_known_date : date, last_uf_value : float, new_ipc : float) -> dict[date: float]:
    """
    Funcion calcula el valor de la UF para hoy en base a inputs.

    Parameters
    ----------
    last_uf_known_date : date
        Fecha de la ultima uf conocida (previo al dia el cual se quiere calcular).
    last_uf_value : float
        Valor de la UF del ultimo dia conocido.
    new_ipc : float
        ultimo ipc mensual publicado en formato de numero, es decir 0.7% se debe
        ingresar como 0.007 en le input.

    Returns
    -------
    [fecha_hoy, uf_hoy] : dict
        Diccionario con la informacion relevante para hoy.

    """
    
    fecha_hoy = last_uf_known_date + timedelta(days=1)
    i = (fecha_hoy - last_uf_known_date).days
    
    if fecha_hoy.day > 9: 
        
        first_day_month = last_uf_known_date.replace(day=1)
        
        last_day_month = first_day_month + timedelta(
            days=calendar.monthrange(
                first_day_month.year, 
                first_day_month.month)[1] - 1)
        
        d = (last_day_month - first_day_month).days + 1
        
    else:
        
        last_day_previous_month = last_uf_known_date.replace(day=1) - timedelta(days=1)
        
        first_day_previous_month = last_day_previous_month.replace(day=1)
        
        d = (last_day_previous_month - first_day_previous_month).days + 1

    aux = last_uf_value * (1 + new_ipc) ** (i/d)
    
    uf_hoy = round(aux, 2)

    return uf_hoy

from datetime import timedelta

def get_ufs(last_uf_known_date : date, last_uf_value : float, new_ipc : float) -> dict[date:float]:
    
    uf_dict = {}  # Diccionario para almacenar las fechas y valores de la UF
    uf_dict[last_uf_known_date] = last_uf_value

    # calculamos numero de dias del mes : 
    first_day_month = last_uf_known_date.replace(day=1)
    last_day_month = first_day_month + timedelta(
            days=calendar.monthrange(
                first_day_month.year, 
                first_day_month.month)[1] - 1)
    d = (last_day_month - first_day_month).days + 1


    for i in range(1, d):
        # Calcula la nueva fecha sumando i días a la última fecha conocida
        new_date = last_uf_known_date + timedelta(days=1)

        # Calcula el nuevo valor de la UF utilizando la función existente
        new_uf_value = calcular_uf(last_uf_known_date, last_uf_value, new_ipc)

        # Almacena la fecha y valor de la UF en el diccionario
        uf_dict[new_date] = new_uf_value

        # Actualiza la última fecha conocida y valor de la UF para la siguiente iteración
        last_uf_known_date = new_date
        last_uf_value = new_uf_value

    return uf_dict




