class Tasa:
    def _init_(self, Tipo:str, Dias:str,Base:str):
        self.Tipo=Tipo
        self.Dias=Dias
        self.Base=Base
    
    def ContarDias(Tipo,fecha_hoy,fecha_final):
        if Tipo=="Actual":
            D=(fecha_final - fecha_hoy).days
        elif Tipo=="360":
            D=(360*(fecha_final.year-fecha_hoy.year)+30*(fecha_final.month-fecha_hoy.month)+(fecha_final.day-fecha_hoy.day))
        else:
            print("Ta malo :/")
        return (D)    
    
    def tipo_de_interes (Tipo,tasa,inicio,fin ):
        Dias= ContarDias(Tasa.Tipo,inicio,fin)
        YF=Dias/Tasa.Base
        if Tipo=="Lineal":
            welth= 1+tasa*YF
        elif Tipo=="Compuesto":
            welth=(1+tasa)^YF
        elif Tipo=="Exp":
            welth=np.exp(tasa*YF)
        else:
            print ("OK")
        return(welth )