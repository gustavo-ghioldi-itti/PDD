# 🔒 Singleton – Una sola instancia global

### 📖 Concepto
- Garantiza que una clase tenga **solo una instancia** en todo el programa.  
- Proporciona un **punto de acceso global** a esa instancia.  
- Útil para recursos compartidos: configuración, logging, conexión a base de datos.  

---

### 🧩 Estructura
- **Singleton:** clase que controla su propia instanciación.  
- **Atributo estático `_instance`:** almacena la única instancia de la clase.  
- **Método `__new__`:** sobrescrito para controlar la creación del objeto.  
- **Punto de acceso global:** todos los módulos acceden a la misma instancia.  

---

### 🧑‍💻 Ejemplo práctico en Python – Configuración de aplicación
👉 [Ver ejemplo completo en código](22_singleton.py)

---

### 🎯 Ventajas
- **Acceso controlado:** garantiza que solo exista una instancia en todo el programa.  
- **Punto de acceso global:** fácil de acceder desde cualquier parte del código.  
- **Ahorro de recursos:** evita crear múltiples instancias de objetos costosos (conexiones DB, configuraciones).  
- **Consistencia:** todos los módulos trabajan con el mismo estado compartido.  

---

### ⚠️ Consideraciones
- **Acoplamiento global:** puede dificultar el testing y crear dependencias ocultas.  
- **Thread-safety:** en aplicaciones multihilo, se debe asegurar que la creación sea thread-safe (usar locks).  
- **Alternativas en Python:** a veces es mejor usar **módulos** (que ya son singleton por naturaleza) o **inyección de dependencias**.  
- **Antipatrón:** el uso excesivo de Singleton puede indicar problemas de diseño; usar con moderación.  

---