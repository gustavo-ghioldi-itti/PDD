# Librería externa
class APIExterna:
    def obtener_datos(self):
        return {"status": "ok", "data": [1, 2, 3]}


# Tu API espera un método 'get_data'
class Adapter:
    def __init__(self, api_externa):
        self.api_externa = api_externa

    def get_data(self):
        # Traduce la interfaz externa a la interna
        return self.api_externa.obtener_datos()


# Uso
api = APIExterna()
adaptador = Adapter(api)
print(adaptador.get_data())
# → {'status': 'ok', 'data': [1, 2, 3]}
