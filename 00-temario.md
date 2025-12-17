**temario estructurado para una masterclass de 45–60 minutos sobre patrones de diseño en Python**, pensado para mantener el ritmo dinámico y claro:

---

# 🎓 Masterclass: Patrones de Diseño en Python  
**Duración:** 45–60 min

---

## 1. Introducción (5 min)
- Qué son los patrones de diseño y por qué importan.  
- Breve historia (Gang of Four).  
- Ventajas en Python: legibilidad, reutilización, mantenibilidad.  

---

## 2. Patrones Creacionales (10–15 min)
- **[Factory Method](02-creacionales/21-factory.md)** → creación flexible de objetos.  
  - Ejemplo práctico: instanciación de diferentes tipos de usuarios.  
- **[Singleton](02-creacionales/22-sigleton.md)** → una sola instancia global.  
  - Ejemplo: configuración de aplicación.  
- **[Builder](02-creacionales/23-builder.md)** → construcción paso a paso de objetos complejos.  
  - Ejemplo: armado de queries SQL o JSON.  

👉 **[Resumen Patrones Creacionales](02-creacionales/24-summary.md)**  

---

## 3. Patrones Estructurales (10–15 min)
- **[Adapter](03-estructurales/31-adapter.md)** → compatibilizar interfaces distintas.  
  - Ejemplo: integrar librerías externas con tu API.  
- **[Decorator](03-estructurales/32-decorador.md)** → añadir funcionalidades sin modificar la clase.  
  - Ejemplo: logging o validación en funciones.  
- **[Facade](03-estructurales/33-facade.md)** → simplificar acceso a subsistemas complejos.  
  - Ejemplo: wrapper sobre librerías de requests + autenticación.  

👉 **[Resumen Patrones Estructurales](03-estructurales/34-summary.md)**  

---

## 4. Patrones de Comportamiento (10–15 min)
- **[Observer](04-comportamiento/41-observer.md)** → notificación automática de cambios.  
  - Ejemplo: sistema de eventos en Django/Flask.  
- **[Strategy](04-comportamiento/42-strategy.md)** → intercambiar algoritmos en tiempo de ejecución.  
  - Ejemplo: distintos métodos de pago.  
- **[Command](04-comportamiento/43-command.md)** → encapsular acciones como objetos.  
  - Ejemplo: sistema de tareas encoladas.  

👉 **[Resumen Patrones de Comportamiento](04-comportamiento/44-summary.md)**  

---

## 5. Casos prácticos(5–10 min)
- Implementar un mini ejemplo integrando varios patrones.  
- Mostrar cómo Python simplifica la implementación (decoradores, metaclases, duck typing).  

---

## 6. Cierre y Q&A (5 min)

---


