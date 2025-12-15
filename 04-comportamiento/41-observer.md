# 👀 Observer – Detalle completo

### 📖 Concepto
- Define una relación **uno-a-muchos** entre objetos: cuando el **Subject** cambia de estado, **notifica automáticamente** a todos sus **Observers**.  
- Se usa para implementar **eventos, suscripciones y notificaciones**.  
- Desacopla el emisor (Subject) de los receptores (Observers).  

---

### 🧩 Estructura
- **Subject (Observable):** mantiene una lista de observadores y tiene métodos para añadir/quitar y notificar.  
- **Observer:** define la interfaz para recibir actualizaciones.  
- **ConcreteSubject:** almacena el estado y dispara notificaciones.  
- **ConcreteObserver:** implementa la reacción al cambio.  

---

### 🧑‍💻 Ejemplo en Python – Sistema de notificaciones
👉 [Ver ejemplo completo en código](41_observer.py)

**Salida:**
```
[EMAIL] Notificación: Nuevo usuario registrado
[SMS] Notificación: Nuevo usuario registrado
```

---

### 🎯 Ventajas
- **Desacoplamiento:** el Subject no necesita saber qué hacen los Observers.  
- **Flexibilidad:** se pueden añadir o quitar observadores en tiempo de ejecución.  
- **Escalabilidad:** múltiples receptores reaccionan al mismo evento.  

---

### ⚠️ Consideraciones
- Puede generar **muchas notificaciones** si no se controla bien.  
- En sistemas grandes conviene usar **event buses** o librerías de pub/sub para optimizar.  
- En Python, el patrón se implementa fácilmente con **listas de callbacks** o incluso con `asyncio` y señales.  

---

👉 Este patrón es clave para entender cómo funcionan **eventos en GUIs, sistemas de mensajería, frameworks web** y hasta **patrones de arquitectura como MVC**.  
