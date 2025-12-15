class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Inicialización única
            cls._instance.settings = {"modo": "producción", "debug": False}
        return cls._instance

# Uso
c1 = Config()
c2 = Config()

print(c1 is c2)  # → True (misma instancia)
print(c1.settings)  # → {'modo': 'producción', 'debug': False}
