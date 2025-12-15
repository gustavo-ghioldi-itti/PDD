# 🧩 Principios SOLID – Resumen

### 1. **S – Single Responsibility Principle (SRP)**
- **Idea:** Cada clase debe tener **una única responsabilidad**.  
- **Beneficio:** Código más claro, fácil de mantener y probar.  
- **Ejemplo:** Una clase `Factura` solo calcula totales; otra clase `FacturaPrinter` se encarga de imprimir.

---

### 2. **O – Open/Closed Principle (OCP)**
- **Idea:** El código debe estar **abierto a extensión, pero cerrado a modificación**.  
- **Beneficio:** Se pueden agregar nuevas funcionalidades sin romper lo existente.  
- **Ejemplo:** Usar herencia o composición para añadir nuevos tipos de validación sin tocar la clase base.

---

### 3. **L – Liskov Substitution Principle (LSP)**
- **Idea:** Los objetos de una subclase deben poder **reemplazar a los de la superclase** sin alterar el comportamiento esperado.  
- **Beneficio:** Garantiza coherencia en jerarquías de clases.  
- **Ejemplo:** Si `Ave` tiene un método `volar()`, una subclase `Pato` debe implementarlo correctamente; una clase `Pingüino` no debería heredar de `Ave` si no puede volar.

---

### 4. **I – Interface Segregation Principle (ISP)**
- **Idea:** Las interfaces deben ser **específicas y pequeñas**, no obligar a implementar métodos innecesarios.  
- **Beneficio:** Evita clases con métodos vacíos o irrelevantes.  
- **Ejemplo:** En vez de una interfaz `Animal` con `volar()`, `nadar()`, `correr()`, se crean interfaces más específicas (`Volador`, `Nadador`, `Corredor`).

---

### 5. **D – Dependency Inversion Principle (DIP)**
- **Idea:** Los módulos de alto nivel no deben depender de módulos de bajo nivel, sino de **abstracciones**.  
- **Beneficio:** Facilita el desacoplamiento y la inyección de dependencias.  
- **Ejemplo:** Una clase `ControladorPago` depende de la interfaz `MetodoPago`, no de la implementación concreta (`Tarjeta`, `Paypal`).

---

## 🎯 Idea clave
- **SOLID** es un conjunto de principios para lograr **código limpio, mantenible y escalable**.  
- Se aplican naturalmente junto con patrones de diseño en Python gracias a su **tipado dinámico, duck typing y decoradores**.  

---