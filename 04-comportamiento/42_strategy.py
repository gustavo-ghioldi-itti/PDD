from abc import ABC, abstractmethod

# Interfaz Strategy
class PagoStrategy(ABC):
    @abstractmethod
    def pagar(self, monto): pass

# Estrategias concretas
class PagoTarjeta(PagoStrategy):
    def pagar(self, monto): print(f"Pagando {monto} con tarjeta")

class PagoPaypal(PagoStrategy):
    def pagar(self, monto): print(f"Pagando {monto} con PayPal")

class PagoCripto(PagoStrategy):
    def pagar(self, monto): print(f"Pagando {monto} con Criptomoneda")

# Contexto
class ProcesadorPago:
    def __init__(self, strategy: PagoStrategy):
        self.strategy = strategy

    def procesar(self, monto):
        self.strategy.pagar(monto)

# Uso
procesador = ProcesadorPago(PagoTarjeta())
procesador.procesar(100)

procesador.strategy = PagoPaypal()
procesador.procesar(200)
