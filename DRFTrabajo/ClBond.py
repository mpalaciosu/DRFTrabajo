class CLBond:
    def _init_(self, fixed_coupons: list[FixedCoupon], tera: float = None):
        self.fixed_coupons = fixed_coupons
        self.tera = tera

    def get_value(self, notional: float, tasa: float, fecha: date) -> float:
        value = 0.0
        for coupon in self.fixed_coupons:
            if fecha >= coupon.Start and fecha <= coupon.End:
                value += coupon.Df * (coupon.flujo * tasa + notional * coupon.tasa)
        return value

    def set_tera(self):
        total_value = 0.0
        total_weight = 0.0
        for coupon in self.fixed_coupons:
            total_value += coupon.Df * coupon.inicial * coupon.tasa
            total_weight += coupon.Df * coupon.inicial
        self.tera = total_value / total_weight

    def get_dv01(self, notional: float) -> float:
        dv01 = 0.0
        for coupon in self.fixed_coupons:
            dv01 += coupon.Df * notional * coupon.tasa
        return dv01
           