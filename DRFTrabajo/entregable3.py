import datetime as dt 
from datetime import timedelta, datetime
import calendar
from datetime import date

def get_ufs(last_uf_known_date : date, last_uf_value : float, new_ipc : float) -> dict[date, float]:
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

    return {fecha_hoy : uf_hoy}


