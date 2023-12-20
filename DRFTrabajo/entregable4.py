from datetime import date
import numpy as np
from scipy.optimize import newton
from datetime import date
from typing import List

class FixedCoupon:
    def __init__(self, residual: float, amortizacion: float, interes: float, start: date, end: date):
        self.residual = residual
        self.amortization = amortizacion
        self.interes = interes
        self.flujo = amortizacion + interes
        self.start = start
        self.end = end


class CLBond:
    def __init__(self, fixed_coupons: List[FixedCoupon], tera: float = None):
        self.fixed_coupons = fixed_coupons
        self.tera = tera if tera is not None else self.set_Tera()

    def set_Tera(self):
        f = self.get_first_start_date()
        inicial_guess = 0.1

        def objetivo(TERA):
            return self.fixed_coupons[0].residual - self.Valor_presente(TERA, f)

        tera = newton(objetivo, x=inicial_guess, tol=0.000001, maxiter=50)
        return tera

    def Valor_presente(self, Tasa, fecha):
        for coupon in self.fixed_coupons:
            if coupon.start <= fecha <= coupon.end:
                d = self.ContarDias(coupon.start, coupon.end)
                coupon.VP = coupon.flujo / (1 + Tasa) ** (d / 365)
        VP = sum(coupon.VP for coupon in self.fixed_coupons)
        return VP

    def get_value(self, notional: float, tasa: float, fecha: date) -> float:
        VP = self.Valor_presente(tasa, fecha)
        VPAR = self.calculate_valor_par(self.tera, fecha)
        precio = round((notional * VP) / VPAR, 4)
        Valor = VPAR * precio / 10000
        return Valor

    def get_first_start_date(self):
        if self.fixed_coupons:
            return self.fixed_coupons[0].start
        else:
            return None

    def calculate_valor_par(self, TERA, fecha):
        d = self.ContarDias(self.fixed_coupons[0].start, fecha)
        return round(100 * (1 + TERA) ** (d / 365), 8)

    def ContarDias(self, start, end):
        return (360 * (end.year - start.year) + 30 * (end.month - start.month) + (end.day - start.day))

    def dv01(self, notional, tasa, fecha):
        tasa2 = tasa + 0.001 / 100
        Aux = self.get_value(notional, tasa, fecha)
        Aux2 = self.get_value(notional, tasa2, fecha)
        dV01 = Aux - Aux2
        return dV01