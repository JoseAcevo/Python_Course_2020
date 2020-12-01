class cuentaCorriente:
    def __init__(self, numero_cc, titular, saldo):
        self.numero = numero_cc
        self.titular = titular
        self.saldo = saldo

    def getDatosCuenta(self):
        return "El titular de la cuenta cuyo número es: " + str(
            self.numero) + " es el Sr/a " + self.titular + " y dispone de un saldo de " + str(self.saldo) + " €"

    def Ingreso(self):
        ingreso = float(input("Inserte cantidad a ingresar, por favor: "))
        self.saldo = self.saldo + ingreso
        return c1.getDatosCuenta()

    def reintegro(self):
        reintegro = float(input("Inserte cantidad a retirar, por favor: "))
        self.saldo = self.saldo - reintegro
        return c1.getDatosCuenta()


class Cuenta_Joven(cuentaCorriente):
    def __init__(self, numero_cc, titular, saldo, bonus=0):
        super().__init__(numero_cc, titular, saldo)
        self.bonus_promocion = bonus
        self.saldo += bonus

    @property
    def getbonus(self):
        return "El importe del bonus asciende a : " + str(self.bonus_promocion)

    def getDatosCuenta(self):
        return super().getDatosCuenta() + "Bonus" + str(self.bonus_promocion)


c1 = Cuenta_Joven(12345,"Pepita", 1500, 200)
c1.Ingreso()
c1.reintegro()
print(c1.getDatosCuenta())

# Seguir desde aquí y seguir con el ejemplo del curso tutorizado (Cuenta Joven).
