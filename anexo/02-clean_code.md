# 🧼 Clean Code – Principios clave

### 1. **Nombres claros y significativos**
- Usar nombres que expresen **intención** (ej: `calcular_total()` en vez de `ct()`).
- Evitar abreviaturas crípticas o genéricas (`data`, `temp`).

---

### 2. **Funciones pequeñas y enfocadas**
- Cada función debe hacer **una sola cosa** y hacerlo bien.  
- Máximo 20–30 líneas, preferir dividir en sub-funciones.

---

### 3. **Evitar duplicación (DRY – Don’t Repeat Yourself)**
- Extraer lógica repetida en funciones o clases reutilizables.  
- La duplicación genera inconsistencias y dificulta el mantenimiento.

---

### 4. **Comentarios útiles, no redundantes**
- El código debe ser **autoexplicativo**.  
- Usar comentarios solo para aclarar *por qué* se hace algo, no *qué* hace.

---

### 5. **Manejo claro de errores**
- Usar excepciones en lugar de códigos mágicos.  
- Proporcionar mensajes de error descriptivos.

---

### 6. **Consistencia en estilo**
- Seguir convenciones (PEP8 en Python).  
- Indentación, nombres, espaciado y formato homogéneo.

---

### 7. **Separación de responsabilidades**
- Aplicar SRP (Single Responsibility Principle).  
- Evitar clases o funciones “Dios” que hacen de todo.

---

### 🧑‍💻 Ejemplo en Python – Código limpio vs. sucio

```python
# ❌ Código sucio
def f(x, y):
    return x*9/5+y

# ✅ Código limpio
def convertir_celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte temperatura de Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32
```

---

## 🎯 Idea clave
- **Clean Code** no es solo estética: mejora la **legibilidad, mantenibilidad y escalabilidad** del software.  
- En Python, se potencia con **nombres expresivos, funciones pequeñas, PEP8 y duck typing**.  
