# 🧑‍💻 Caso práctico: Sistema de Notificaciones con Patrones

### 🎯 Objetivo
- **Observer** → notificar a múltiples canales (Email, SMS, Push).  
- **Strategy** → elegir el algoritmo de envío (rápido, seguro, en batch).  
- **Decorator** → añadir logging sin modificar las clases.  
- **Singleton** → configuración global de la aplicación.  
- Mostrar cómo Python simplifica todo con **decoradores, duck typing y metaclases**.

---

### 🧩 Código Integrado
```python
from abc import ABC, abstractmethod

# --- Singleton para configuración global ---
class Config:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.settings = {"modo": "producción", "debug": True}
        return cls._instance

# --- Decorator para logging ---
def log(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Ejecutando {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# --- Observer: Subject y Observers ---
class Subject:
    def __init__(self): self._observers = []
    def attach(self, obs): self._observers.append(obs)
    def notify(self, msg):
        for obs in self._observers: obs.update(msg)

class Observer(ABC):
    @abstractmethod
    def update(self, msg): pass

class EmailObserver(Observer):
    def update(self, msg): print(f"[EMAIL] {msg}")

class SMSObserver(Observer):
    def update(self, msg): print(f"[SMS] {msg}")

# --- Strategy: distintas formas de enviar ---
class EstrategiaEnvio(ABC):
    @abstractmethod
    def enviar(self, msg): pass

class EnvioRapido(EstrategiaEnvio):
    def enviar(self, msg): print(f"Envío rápido: {msg}")

class EnvioSeguro(EstrategiaEnvio):
    def enviar(self, msg): print(f"Envío seguro: {msg}")

# --- Contexto que integra todo ---
class Notificador:
    def __init__(self, estrategia: EstrategiaEnvio):
        self.estrategia = estrategia
        self.subject = Subject()
    @log
    def notificar(self, msg):
        self.estrategia.enviar(msg)
        self.subject.notify(msg)

# --- Uso ---
config = Config()
print("Modo:", config.settings["modo"])

notificador = Notificador(EnvioRapido())
notificador.subject.attach(EmailObserver())
notificador.subject.attach(SMSObserver())

notificador.notificar("Nuevo usuario registrado")
```

---

### 📌 Salida esperada
```
Modo: producción
[LOG] Ejecutando notificar
Envío rápido: Nuevo usuario registrado
[EMAIL] Nuevo usuario registrado
[SMS] Nuevo usuario registrado
```

---

### 🚀 Claves para mostrar en vivo
- **Duck typing:** los observers solo necesitan implementar `update`, no importa la clase.  
- **Decoradores:** logging agregado sin tocar la lógica de `Notificador`.  
- **Singleton:** configuración compartida en toda la app.  
- **Strategy + Observer:** flexibilidad para cambiar el algoritmo de envío y notificar múltiples canales.  

---