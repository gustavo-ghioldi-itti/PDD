import requests

# Subsistema complejo: autenticación + llamadas HTTP
class SistemaHTTP:
    def __init__(self, token):
        self.token = token

    def get(self, url):
        headers = {"Authorization": f"Bearer {self.token}"}
        return requests.get(url, headers=headers)

    def post(self, url, data):
        headers = {"Authorization": f"Bearer {self.token}"}
        return requests.post(url, json=data, headers=headers)

# Facade: interfaz simplificada
class APIClient:
    def __init__(self, token):
        self.http = SistemaHTTP(token)

    def obtener_usuarios(self):
        return self.http.get("https://api.ejemplo.com/users").json()

    def crear_usuario(self, datos):
        return self.http.post("https://api.ejemplo.com/users", datos).json()

# Uso
cliente = APIClient("mi_token_secreto")
print(cliente.obtener_usuarios())
