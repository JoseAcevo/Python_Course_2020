print(input("Pulse botón StopStart para contacto."))


class Contacto:

    def __init__(self):
        self.arranque = False
        self.Pedal_Freno = False
        self.Pedal_Embrague = False
        self.airbag_light = True
        self.Abs_light = True
        self.oil_light = True
        self.battery_light = True

    def llave_electronica(self, presente):
        self.Llave_Electronica = presente

        if self.Llave_Electronica:
            return V1.inmov_1(True)

        else:
            return V1.inmov_1(False)

    def inmov_1(self, inmo):
        self.inmo_1 = inmo

        if self.inmo_1:
            return V1.arrancar(True)

        else:
            return V1.arrancar(False)

    @staticmethod
    def denegacion_servicio():
        return "Llave electrónica no reconocida o defectuosa."

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

        """Presionar el botón sin pisar pedales 
        pondrá el contacto del vehiculo"""

    def stopstart_engine(self):  # BOTON DE ARRRANQUE

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
                return "Pise pedales freno y embrague para arrancar."

    def diagnosis(self, airbag, Abs, oil, battery):

        if airbag:
            print("Sistema de retención de ocupantes <<OK>>")
        elif airbag(False):
            print("Sistema de retención defectuoso acuda al taller")  # Esto no vale....
        elif Abs:
            print("Sistema de frenos <<OK>>")
        elif Abs(False):
            print("Sistema de frenos defectuoso, acuda al taller")

    def airbag(self, conductor, acompanante, cintoA, cintoB):

        self.Aconductor = conductor
        self.Aacompanante = acompanante
        self.Pconductor = cintoA
        self.Pacompanante = cintoB

        if self.Aconductor and self.Aacompanante and self.Pconductor and self.Pacompanante:
            V1.diagnosis(True, False, False, False)
            self.airbag_light = False

        if not self.Aconductor or self.Aacompanante or self.Pacompanante or self.Pconductor:
            V1.diagnosis(False, False, False, False)

    def Abs(self, avi, avd, ari, ard, pedalfreno):

        self.avi = avi
        self.avd = avd
        self.ard = ard
        self.ari = ari
        self.Pedal_Freno = pedalfreno

        if self.avi and self.avd and self.ard and self.ari and self.Pedal_Freno:
            V1.diagnosis()
            self.airbag_light = False
            return "Sistema frenos <<OK>>"

        if not self.avi or self.avd or self.ari or self.ari or self.Pedal_Freno:
            return "Sistema frenos defectuoso, acuda al taller"

    def oil(self):
        self.oil = False
        pass

    def battery(self):
        self.battery = False
        pass

    @staticmethod
    def motor_arranque():
        return "El motor de arranque gira"


V1 = Contacto()
V1.llave_electronica(True)
V1.embrague()
V1.freno()
V1.airbag(True, True, True, True)
