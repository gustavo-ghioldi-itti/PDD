# 🔄 Patrones de Comportamiento – Summary con ejemplos en Python

### 👀 Observer
**Qué hace:** Define una relación de dependencia uno-a-muchos, donde cuando un objeto cambia su estado, notifica automáticamente a sus dependientes.  
```python
class Subject:
    def __init__(self): self.observers = []
    def attach(self, obs): self.observers.append(obs)
    def notify(self, msg):
        for obs in self.observers: obs.update(msg)

class Observer:
    def update(self, msg): print(f"Notificado: {msg}")

s = Subject(); o = Observer()
s.attach(o); s.notify("Cambio de estado")
```

---

### 🧠 Strategy
**Qué hace:** Permite definir una familia de algoritmos y elegir cuál usar en tiempo de ejecución.  
```python
class Pago:
    def pagar(self): pass

class PagoTarjeta(Pago):
    def pagar(self): print("Pago con tarjeta")

class PagoPaypal(Pago):
    def pagar(self): print("Pago con PayPal")

def procesar(pago: Pago): pago.pagar()

procesar(PagoTarjeta())
procesar(PagoPaypal())
```

---

### 📦 Command
**Qué hace:** Encapsula una acción como un objeto, permitiendo parametrizar clientes con operaciones, deshacer acciones y encolar tareas.  
```python
class Command:
    def execute(self): pass

class PrintCommand(Command):
    def __init__(self, msg): self.msg = msg
    def execute(self): print(self.msg)

cmd = PrintCommand("Hola mundo")
cmd.execute()
```

---

### 🧑‍🤝‍🧑 Mediator
**Qué hace:** Centraliza la comunicación entre objetos, evitando dependencias directas.  
```python
class ChatMediator:
    def __init__(self): self.users = []
    def register(self, user): self.users.append(user)
    def send(self, msg, sender):
        for u in self.users:
            if u != sender: u.receive(msg)

class User:
    def __init__(self, name, mediator):
        self.name, self.mediator = name, mediator
        mediator.register(self)
    def send(self, msg): self.mediator.send(msg, self)
    def receive(self, msg): print(f"{self.name} recibió: {msg}")

m = ChatMediator()
u1, u2 = User("Ana", m), User("Luis", m)
u1.send("Hola a todos")
```

---

### 🔍 Chain of Responsibility
**Qué hace:** Permite pasar una petición a través de una cadena de manejadores hasta que uno la procese.  
```python
class Handler:
    def __init__(self, next=None): self.next = next
    def handle(self, req):
        if self.next: return self.next.handle(req)

class AuthHandler(Handler):
    def handle(self, req):
        if req.get("auth"): print("Autenticado")
        else: super().handle(req)

class LogHandler(Handler):
    def handle(self, req):
        print("Log:", req); super().handle(req)

chain = LogHandler(AuthHandler())
chain.handle({"auth": True})
```

---

### 🧾 Memento
**Qué hace:** Captura y restaura el estado interno de un objeto sin violar su encapsulación.  
```python
class Editor:
    def __init__(self): self.text = ""
    def write(self, txt): self.text += txt
    def save(self): return self.text
    def restore(self, memento): self.text = memento

editor = Editor()
editor.write("Hola ")
memento = editor.save()
editor.write("Mundo")
editor.restore(memento)
print(editor.text)  # → "Hola "
```

---

### 🎯 Template Method
**Qué hace:** Define el esqueleto de un algoritmo en una clase base, dejando que las subclases implementen pasos específicos.  
```python
from abc import ABC, abstractmethod

class Report(ABC):
    def generar(self):
        self.header()
        self.body()
        self.footer()

    @abstractmethod
    def header(self): pass
    @abstractmethod
    def body(self): pass
    @abstractmethod
    def footer(self): pass

class PDFReport(Report):
    def header(self): print("Encabezado PDF")
    def body(self): print("Contenido PDF")
    def footer(self): print("Pie PDF")

PDFReport().generar()
```

---

## 🎯 Idea clave del grupo
- Los **patrones de comportamiento** se enfocan en **cómo los objetos interactúan y se comunican**.  
- Diferencias principales:  
  - **Observer / Mediator / Chain of Responsibility** → gestión de comunicación y flujo.  
  - **Strategy / Command / Template Method** → encapsulación de algoritmos y acciones.  
  - **Memento** → manejo de estados y restauración.  

---
