def log(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Ejecutando {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def saludar(nombre):
    print(f"Hola, {nombre}!")

# Uso
saludar("Gustavo")
# → [LOG] Ejecutando saludar
# → Hola, Gustavo!
