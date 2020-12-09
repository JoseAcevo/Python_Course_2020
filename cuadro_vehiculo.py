class Contacto:
    def __init__(self):
        self.arranque = False
        self.Pedal_Freno = False
        self.Pedal_Embrague = False

    def llave_electronica(self, presente):
        self.Llave_Electronica = presente

        if self.Llave_Electronica:
            print(input("Pulse Stop and Start para poner contacto....."))
            return V1.inmov_1(True)

        else:
            return V1.denegacion_servicio()

    def inmov_1(self, inmo):
        self.inmo_1 = inmo

        if self.inmo_1:
            return V1.arrancar(True)

        else:
            return V1.arrancar(False)

    @staticmethod
    def denegacion_servicio():
        print("Llave electrónica no reconocida o defectuosa.")

    def arrancar(self, autorizacion):
        self.arranque = autorizacion

        if self.arranque:
            return V1.motor_arranque()
        else:
            return V1.denegacion_servicio()

    def freno(self):
        self.Pedal_Freno = True

    def embrague(self):
        self.Pedal_Embrague = True

    @property
    def stopstart_engine(self):

        if self.inmo_1 and self.Pedal_Embrague and self.Pedal_Freno:
            return V1.arrancar(True)

        else:

            if not self.inmo_1:
                return V1.denegacion_servicio()

            elif self.Pedal_Embrague:
                return "Pise el pedal del freno para arrancar."

            elif self.Pedal_Freno:
                return "Pise el pedal del embrague para arrancar."

            else:
                return "Pise pedales freno/embrague para arrancar."

    @staticmethod
    def motor_arranque():
        return "El motor de arranque gira"


# MODULO CONTROL AIRBAG.
# AIRBAGS SIGNALS

# FRONT-LEFT = OK OR NOOK
# IF OK:
# V1.AIRBAG(TRUE)
# ELSE:
# V1.AIRBAG(FALSE)

# FRONT-RIGHT = OK OR NOOK
# IF OK:
# V1.AIRBAG(TRUE)

# ELSE:
# V1.AIRBAG(FALSE)


# PRETENS SIGNALS

# FRONT-LEFT = OK OR NOOK
# IF OK:
# V1.AIRBAG(TRUE)
# ELSE:
# V1.AIRBAG(FALSE)

# FRONT-RIGHT = OK OR NOOK
# IF OK:
# V1.AIRBAG(TRUE)

# ELSE:
# V1.AIRBAG(FALSE)


# PRESENCE SENSOR

# FRONT RIGHT SEAT = OK OR NOOK
# IF OK:
# V1.AIRBAG(TRUE)
# ELSE:
# V1.AIRBAG(FALSE)


class Diagnosis(Contacto):
    def __init__(self):
        super().__init__()
        self.airbag_light = True
        self.abs_light = True
        self.battery_light = True
        self.oil_light = True

    def calculador_control_airbag(self, front_left, front_right, pre_left, pre_right, presence_sensor):
        self.Driver_Airbag = front_left
        self.Copilot_Airbag = front_right
        self.pre_left = pre_left
        self.pre_right = pre_right
        self.presence = presence_sensor

        if self.Driver_Airbag and self.Copilot_Airbag and self.pre_left and self.pre_right and presence_sensor:
            return V1.airbag(False)
        else:
            return V1.airbag(True)

    def airbag(self, diag):
        self.airbag_light = diag
        if self.airbag_light:
            print('Sistema de retención de pasajeros defectuoso, ACUDA AL TALLER.')
        else:
            print("Sistema de retención de pasajeros funciona correctamente")

    def abs(self, diag):
        self.abs_light = diag
        if self.abs_light:
            print("Sistema electrónico de control de frenado y estabilidad defectuoso, ACUDA AL TALLER.")
        else:
            print("Sistema electrónico de control de frenado y estabilidad funciona correctamente")

    def battery(self, diag):
        self.battery_light = diag
        if self.battery_light:
            print("Sistema electrónico de control de carga de la batería defectuoso, ACUDA AL TALLER.")
        else:
            print("Sistema electrónico de control de carga de la batería funciona correctamente")

    def oil(self):
        self.oil_light = False
        pass


V1 = Diagnosis()
V1.embrague()
V1.freno()
# Reconocimiento de la llave de contacto.
V1.llave_electronica(False)
V1.calculador_control_airbag(False, True, True, True, True)
print(V1.stopstart_engine)
