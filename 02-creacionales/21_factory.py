from abc import ABC, abstractmethod

# Producto abstracto
class Usuario(ABC):
    @abstractmethod
    def tipo(self):
        pass

# Productos concretos
class Admin(Usuario):
    def tipo(self): return "Administrador"

class Invitado(Usuario):
    def tipo(self): return "Invitado"

# Creador abstracto
class UsuarioFactory(ABC):
    @abstractmethod
    def crear_usuario(self):
        pass

# Creadores concretos
class AdminFactory(UsuarioFactory):
    def crear_usuario(self): return Admin()

class InvitadoFactory(UsuarioFactory):
    def crear_usuario(self): return Invitado()

# Uso
factory = AdminFactory()
usuario = factory.crear_usuario()
print(usuario.tipo())   # → "Administrador"
