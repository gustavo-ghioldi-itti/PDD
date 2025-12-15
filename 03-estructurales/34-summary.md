# 🏗️ Patrones Estructurales – Summary con ejemplos en Python

### 🔌 Adapter
**Qué hace:** Traduce una interfaz a otra compatible.  
```python
class APIExterna:
    def obtener_datos(self): return {"ok": True}

class Adapter:
    def __init__(self, api): self.api = api
    def get_data(self): return self.api.obtener_datos()

print(Adapter(APIExterna()).get_data())
```

---

### 🎨 Decorator
**Qué hace:** Añade funcionalidades sin modificar la clase original.  
```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def saludar(): print("Hola!")
saludar()
```

---

### 🏢 Facade
**Qué hace:** Simplifica acceso a subsistemas complejos.  
```python
class Sistema:
    def paso1(self): return "p1"
    def paso2(self): return "p2"

class Facade:
    def __init__(self): self.sys = Sistema()
    def operar(self): return f"{self.sys.paso1()}-{self.sys.paso2()}"

print(Facade().operar())
```

---

### 🧱 Composite
**Qué hace:** Trata objetos individuales y compuestos de forma uniforme.  
```python
class Componente:
    def mostrar(self): pass

class Archivo(Componente):
    def __init__(self, nombre): self.nombre = nombre
    def mostrar(self): print(self.nombre)

class Carpeta(Componente):
    def __init__(self): self.elementos = []
    def agregar(self, comp): self.elementos.append(comp)
    def mostrar(self):
        for e in self.elementos: e.mostrar()

carpeta = Carpeta()
carpeta.agregar(Archivo("doc.txt"))
carpeta.agregar(Archivo("foto.png"))
carpeta.mostrar()
```

---

### 🔗 Bridge
**Qué hace:** Separa abstracción de implementación.  
```python
class Dibujador:
    def dibujar(self, forma): pass

class DibujadorSVG(Dibujador):
    def dibujar(self, forma): print(f"<svg>{forma}</svg>")

class Forma:
    def __init__(self, dibujador): self.dibujador = dibujador
    def mostrar(self): self.dibujador.dibujar("círculo")

Forma(DibujadorSVG()).mostrar()
```

---

### 🪢 Proxy
**Qué hace:** Controla acceso a un objeto.  
```python
class Servicio:
    def operacion(self): print("Ejecutando operación real")

class Proxy:
    def __init__(self): self.servicio = Servicio()
    def operacion(self):
        print("Chequeo de acceso...")
        self.servicio.operacion()

Proxy().operacion()
```

---

### 🧩 Flyweight
**Qué hace:** Reutiliza objetos compartidos para optimizar memoria.  
```python
class Caracter:
    _pool = {}
    def __new__(cls, simbolo):
        if simbolo not in cls._pool:
            cls._pool[simbolo] = super().__new__(cls)
            cls._pool[simbolo].simbolo = simbolo
        return cls._pool[simbolo]

a1 = Caracter("a")
a2 = Caracter("a")
print(a1 is a2)  # → True (misma instancia)
```

---

## 🎯 Idea clave
- **Adapter / Facade / Proxy** → simplifican o controlan acceso.  
- **Decorator / Composite / Bridge** → añaden flexibilidad en composición y extensión.  
- **Flyweight** → optimiza recursos compartiendo datos.  

---

👉 Con este resumen + ejemplos en Python tenés todo el bloque de **patrones estructurales** listo para tu masterclass.  