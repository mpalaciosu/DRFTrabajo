from datetime import date
import numpy as np

class  FixedCoupon:
    def _init_(self,inicial:float ,amortizacion: float, interes: float, final: float,Start: date,End: date):
        self.inicial=inicial #Monto inicial 
        self.amortization= amortizacion #Monto amortizado 
        self.interes=interes # Intereses generados 
        self.tasa=interes/inicial #"tasa de intreres"
        self.flujo=amortizacion+inicial #Flujo del periodo 
        self.Start=Start # fecha inicio
        self.End=End #fecha fin 
        self.welthfactor= (final-amortizacion)/final
        self.Df=1/self.welthfactor
