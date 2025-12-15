## 📦 Prototype – Clonar objetos existentes
- Permite crear nuevos objetos copiando instancias ya existentes.  
- Útil cuando la creación es costosa y se necesita duplicar.  

```python
import copy

class Documento:
    def __init__(self, titulo):
        self.titulo = titulo

    def clone(self):
        return copy.deepcopy(self)

doc1 = Documento("Contrato")
doc2 = doc1.clone()
print(doc2.titulo)  # → "Contrato"
```

---

## 🏢 Abstract Factory – Familias de objetos relacionados
- Proporciona una **interfaz para crear familias de objetos** sin especificar sus clases concretas.  
- Útil cuando se necesita consistencia entre objetos relacionados.  

```python
from abc import ABC, abstractmethod

# Productos
class Boton(ABC): pass
class Ventana(ABC): pass

class BotonMac(Boton): pass
class VentanaMac(Ventana): pass

class BotonWin(Boton): pass
class VentanaWin(Ventana): pass

# Fábricas abstractas
class GUIFactory(ABC):
    @abstractmethod
    def crear_boton(self): pass
    @abstractmethod
    def crear_ventana(self): pass

# Fábricas concretas
class MacFactory(GUIFactory):
    def crear_boton(self): return BotonMac()
    def crear_ventana(self): return VentanaMac()

class WinFactory(GUIFactory):
    def crear_boton(self): return BotonWin()
    def crear_ventana(self): return VentanaWin()

# Uso
factory = MacFactory()
boton = factory.crear_boton()
ventana = factory.crear_ventana()
```

---

## 🧩 Summary rápido
- **Factory Method** → delega la creación a subclases.  
- **Singleton** → asegura una sola instancia global.  
- **Builder** → construye objetos paso a paso.  
- **Prototype** → clona objetos existentes.  
- **Abstract Factory** → crea familias de objetos relacionados.  

---
