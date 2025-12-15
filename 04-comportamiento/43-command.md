# 📦 Command – Detalle completo

### 📖 Concepto
- Encapsula una **solicitud o acción** dentro de un objeto.  
- Permite **parametrizar clientes con operaciones**, encolar comandos, deshacer acciones y separar el emisor del receptor.  
- El cliente no llama directamente al método, sino que ejecuta un **objeto comando**.  

---

### 🧩 Estructura
- **Command (interfaz):** declara el método `execute()`.  
- **ConcreteCommand:** implementa la acción específica.  
- **Receiver:** el objeto que realmente realiza la operación.  
- **Invoker:** invoca el comando sin conocer los detalles de la acción.  
- **Client:** configura el comando y lo asigna al invocador.  

---

### 🧑‍💻 Ejemplo en Python – Editor de texto con comandos
👉 [Ver ejemplo completo en código](43_command.py)

**Salida:**
```
Escribiendo: Hola mundo
Texto borrado
```

---

### 🎯 Ventajas
- **Desacopla** el emisor del receptor.  
- Permite **deshacer/rehacer** acciones guardando el historial.  
- Facilita la **programación de tareas** (colas, macros, batch).  
- Escalable: se pueden añadir nuevos comandos sin modificar el invocador.  

---

### ⚠️ Consideraciones
- Puede aumentar el número de clases (un comando por acción).  
- Conviene usarlo en sistemas donde se requiera **flexibilidad en la ejecución de operaciones**.  

---

👉 Este patrón es clave en **editores de texto, sistemas de transacciones, control remoto, menús de aplicaciones** y cualquier lugar donde se necesite **deshacer/rehacer o encolar acciones**.  