# 🏢 Facade – Simplificar acceso a subsistemas complejos

### 📖 Concepto
- Proporciona una **interfaz unificada y sencilla** para un conjunto de clases o librerías complejas.  
- Oculta la complejidad interna y ofrece un **punto de entrada único**.  
- Útil para crear **wrappers** sobre librerías externas o sistemas con múltiples pasos.  

---

### 🧩 Estructura
- **Subsistemas complejos:** conjunto de clases o módulos con lógica detallada.  
- **Facade:** clase que proporciona una interfaz simplificada para acceder a los subsistemas.  
- **Cliente:** usa la Facade sin conocer la complejidad interna.  
- **Encapsulación:** la Facade oculta los detalles de implementación.  

---

### 🧑‍💻 Ejemplo práctico en Python – Wrapper sobre `requests` + autenticación
👉 [Ver ejemplo completo en código](33_facade.py)

---

### 🎯 Ventajas
- **Simplicidad:** reduce la complejidad para el cliente final.  
- **Desacoplamiento:** el cliente no depende de los detalles internos de los subsistemas.  
- **Mantenibilidad:** cambios en los subsistemas no afectan al cliente si la Facade se mantiene estable.  
- **Punto de entrada único:** facilita el uso de sistemas complejos con una API clara.  

---

### ⚠️ Consideraciones
- La Facade puede convertirse en un **God Object** si acumula demasiadas responsabilidades.  
- No elimina la complejidad, solo la oculta; los subsistemas siguen siendo complejos internamente.  
- Conviene usarlo cuando se trabaja con **librerías de terceros, APIs complejas o sistemas legacy**.  
- En Python, es común crear Facades como **módulos o clases wrapper** para simplificar el uso de bibliotecas.  

---  
