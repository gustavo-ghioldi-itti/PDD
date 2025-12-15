# 🔌 Adapter – Compatibilizar interfaces distintas

### 📖 Concepto
- Permite que **dos interfaces incompatibles trabajen juntas**.  
- Actúa como un **traductor** entre clases o librerías que no fueron diseñadas para interactuar.  
- Útil para integrar librerías externas en tu propio sistema sin modificar su código.  

---

### 🧩 Estructura
- **Target (interfaz esperada):** la interfaz que el cliente espera usar.  
- **Adaptee (clase a adaptar):** la clase existente con interfaz incompatible.  
- **Adapter:** clase que implementa la interfaz Target y traduce las llamadas al Adaptee.  
- **Cliente:** usa la interfaz Target sin conocer al Adaptee.  

---

### 🧑‍💻 Ejemplo práctico en Python – Integrar librería externa con tu API
👉 [Ver ejemplo completo en código](31_adapter.py)

---

### 🎯 Ventajas
- **Reutilización:** permite usar código existente sin modificarlo.  
- **Desacoplamiento:** el cliente no necesita conocer la implementación del Adaptee.  
- **Integración limpia:** facilita la integración de librerías de terceros o sistemas legacy.  
- **Flexibilidad:** se pueden crear múltiples adaptadores para diferentes interfaces.  

---

### ⚠️ Consideraciones
- Agrega una capa extra de indirección, lo que puede afectar ligeramente el rendimiento.  
- Si se necesitan adaptar muchas interfaces, puede resultar en muchas clases Adapter.  
- Conviene usarlo cuando **no se puede modificar** la clase original o cuando se quiere mantener compatibilidad.  

---
