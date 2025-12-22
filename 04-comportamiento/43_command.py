from abc import ABC, abstractmethod


# Interfaz Command
class Command(ABC):
    @abstractmethod
    def execute(self): pass


# Receiver
class Editor:
    def escribir(self, texto): print(f"Escribiendo: {texto}")
    def borrar(self): print("Texto borrado")


# ConcreteCommands
class EscribirCommand(Command):
    def __init__(self, editor, texto):
        self.editor, self.texto = editor, texto

    def execute(self): self.editor.escribir(self.texto)


class BorrarCommand(Command):
    def __init__(self, editor):
        self.editor = editor

    def execute(self): self.editor.borrar()


# Invoker
class Invoker:
    def __init__(self): self.historial = []

    def ejecutar(self, comando):
        comando.execute()
        self.historial.append(comando)


# Uso
editor = Editor()
invoker = Invoker()

invoker.ejecutar(EscribirCommand(editor, "Hola mundo"))
invoker.ejecutar(BorrarCommand(editor))
