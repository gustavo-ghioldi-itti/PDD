# 🎨 Decorator – Añadir funcionalidades sin modificar la clase

### 📖 Concepto
- Permite **extender el comportamiento** de una función o clase sin alterar su código original.  
- Se aplica envolviendo la función/clase con otra que añade lógica adicional.  
- Útil para **logging, validación, control de acceso, caching**, etc.  

---

### 🧩 Estructura
- **Componente (función/clase original):** el objeto base que se va a decorar.  
- **Decorator (función wrapper):** envuelve al componente y añade funcionalidad extra.  
- **Sintaxis `@decorator`:** azúcar sintáctico de Python para aplicar decoradores.  
- **Composición:** se pueden apilar múltiples decoradores sobre la misma función.  

---

### 🧑‍💻 Ejemplo práctico en Python – Logging en funciones
👉 [Ver ejemplo completo en código](32_decorator.py)

---

### 🎯 Ventajas
- **Extensibilidad:** añade funcionalidades sin modificar el código original (Open/Closed Principle).  
- **Reutilización:** los decoradores se pueden aplicar a múltiples funciones/clases.  
- **Composición:** se pueden combinar múltiples decoradores para crear comportamientos complejos.  
- **Transparencia:** el código decorado mantiene su interfaz original.  

---

### ⚠️ Consideraciones
- Puede dificultar el debugging si se apilan muchos decoradores.  
- El orden de los decoradores importa (se aplican de abajo hacia arriba).  
- En Python, los decoradores son muy idiomáticos y ampliamente usados en frameworks (Flask, Django, FastAPI).  
- Conviene documentar bien qué hace cada decorador para mantener la claridad del código.  

---
