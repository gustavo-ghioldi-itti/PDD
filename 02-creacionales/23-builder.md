# 🏗️ Builder – Construcción paso a paso de objetos complejos

### 📖 Concepto
- Permite **crear objetos complejos** separando la construcción de su representación final.  
- Se construye el objeto **paso a paso**, con métodos encadenados.  
- Útil cuando un objeto tiene muchas opciones o configuraciones.  

---

### 🧩 Estructura
- **Builder:** clase que construye el objeto paso a paso.  
- **Métodos encadenados:** cada método retorna `self` para permitir encadenamiento (fluent interface).  
- **Método `build()`:** finaliza la construcción y devuelve el objeto completo.  
- **Producto:** el objeto complejo que se está construyendo.  

---

### 🧑‍💻 Ejemplo práctico en Python – Armado de queries SQL
👉 [Ver ejemplo completo en código](23_builder.py)

---

### 🎯 Ventajas
- **Legibilidad:** el código de construcción es claro y autodocumentado.  
- **Flexibilidad:** permite construir diferentes representaciones del mismo objeto.  
- **Evita constructores complejos:** no necesitas constructores con muchos parámetros opcionales.  
- **Inmutabilidad:** se puede diseñar para crear objetos inmutables después de la construcción.  

---

### ⚠️ Consideraciones
- Puede agregar complejidad innecesaria para objetos simples.  
- Conviene usarlo cuando el objeto tiene **muchas configuraciones opcionales** o pasos de construcción.  
- En Python, también se puede lograr flexibilidad con **kwargs** y valores por defecto, pero Builder es más explícito.  

---
