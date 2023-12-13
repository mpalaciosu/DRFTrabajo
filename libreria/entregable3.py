import datetime as dt 
from datetime import timedelta, datetime
import calendar

def get_ufs(last_uf_known_date : dt.datetime, last_uf_value : float, new_ipc : float):
    """
    Funcion calcula el valor de la UF para hoy en base a inputs.

    Parameters
    ----------
    last_uf_known_date : dt.datetime
        Fecha de la ultima uf conocida para un dia 9. (este dato siempre estara
        disponible online).
    last_uf_value : float
        Valor de la UF el ultimo dia 9.
    new_ipc : float
        IPC publicado el mes anterior. Se debe utilizar el valor mensual.

    Returns
    -------
    [fecha_hoy, uf_hoy] : DICT
        Diccionario con la informacion relevante para hoy.

    """
    
    fecha_hoy = datetime.now()
    i = (fecha_hoy - last_uf_known_date).days
    
    if fecha_hoy.day > 9: 
        
        first_day_month = last_uf_known_date.replace(day=1)
        
        last_day_month = first_day_month + timedelta(
            days=calendar.monthrange(
                first_day_month.year, 
                first_day_month.month)[1] - 1)
        
        d = (last_day_month - first_day_month).days + 1
        
    else:
        
        first_day_previous_month = last_uf_known_date.replace(day=1) - timedelta(days=1)
        
        last_day_previous_month = first_day_previous_month + timedelta(
            days=calendar.monthrange(
                first_day_previous_month.year, 
                first_day_month.month)[1] - 1)
        
        d = (last_day_previous_month - first_day_previous_month).days + 1

    aux = last_uf_value*(1 + new_ipc) ** (i/d)
    
    uf_hoy = round(aux, 2)

    return [fecha_hoy, uf_hoy]

