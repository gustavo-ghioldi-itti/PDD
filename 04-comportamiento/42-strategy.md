# 🧠 Strategy – Detalle completo

### 📖 Concepto
- Define una **familia de algoritmos**, encapsula cada uno y los hace **intercambiables**.  
- Permite que el algoritmo varíe independientemente del cliente que lo usa.  
- Evita condicionales extensos (`if/else`) para elegir comportamientos.  

---

### 🧩 Estructura
- **Contexto:** clase que usa una estrategia.  
- **Strategy (interfaz):** define el método común para todas las estrategias.  
- **ConcreteStrategy:** implementa un algoritmo específico.  
- El **Contexto** delega la ejecución a la estrategia seleccionada.  

---

### 🧑‍💻 Ejemplo en Python – Métodos de pago
👉 [Ver ejemplo completo en código](42_strategy.py)

**Salida:**
```
Pagando 100 con tarjeta
Pagando 200 con PayPal
```

---

### 🎯 Ventajas
- **Flexibilidad:** cambiar algoritmos en tiempo de ejecución.  
- **Desacoplamiento:** el contexto no necesita conocer los detalles de cada estrategia.  
- **Reutilización:** cada estrategia se puede usar en distintos contextos.  

---

### ⚠️ Consideraciones
- Puede aumentar el número de clases (una por estrategia).  
- Conviene usarlo cuando los algoritmos son **suficientemente distintos** y se espera intercambiarlos.  

---

👉 Este patrón es clave en sistemas donde se necesita **variar comportamientos dinámicamente**, como motores de reglas, validaciones, cálculos o métodos de pago.
