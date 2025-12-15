# 🏭 Factory Method – Creación flexible de objetos

### 📖 Concepto
- Define una **interfaz para crear objetos**, pero permite que las **subclases decidan qué clase instanciar**.  
- Desacopla la lógica de creación del uso del objeto.  
- Facilita la **extensibilidad**: se pueden agregar nuevos tipos sin modificar el código cliente.  

---

### 🧩 Estructura
- **Producto (abstracto):** define la interfaz común para todos los objetos creados.  
- **Producto Concreto:** implementaciones específicas del producto.  
- **Creador (abstracto):** declara el método fábrica que devuelve un Producto.  
- **Creador Concreto:** sobrescribe el método fábrica para devolver una instancia específica.  

---

### 🧑‍💻 Ejemplo práctico en Python – Usuarios
👉 [Ver ejemplo completo en código](21_factory.py)

---

### 🎯 Ventajas
- **Desacoplamiento:** el código cliente no depende de clases concretas, solo de interfaces.  
- **Extensibilidad:** se pueden agregar nuevos tipos de productos sin modificar el código existente (Open/Closed Principle).  
- **Reutilización:** la lógica de creación está centralizada en las fábricas.  
- **Flexibilidad:** permite cambiar qué tipo de objeto se crea en tiempo de ejecución.  

---

### ⚠️ Consideraciones
- Puede aumentar la complejidad del código al requerir múltiples clases (una fábrica por tipo).  
- Conviene usarlo cuando se espera que el sistema crezca con nuevos tipos de productos.  
- En Python, a veces basta con usar **funciones simples** o **diccionarios de clases** en lugar de jerarquías completas.  

---
