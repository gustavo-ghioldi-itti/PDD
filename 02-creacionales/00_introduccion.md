# Patrones Creacionales

## ¿Qué son los Patrones Creacionales?

Los patrones creacionales son patrones de diseño que se enfocan en los mecanismos de creación de objetos, intentando crear objetos de una manera adecuada a la situación. El objetivo principal es abstraer el proceso de instanciación y hacer que el sistema sea independiente de cómo sus objetos son creados, compuestos y representados.

## Propósito

Estos patrones encapsulan el conocimiento sobre qué clases concretas utiliza el sistema y ocultan cómo se crean y combinan las instancias de estas clases. Esto proporciona flexibilidad en **qué** se crea, **quién** lo crea, **cómo** se crea y **cuándo** se crea.

## Problemas que Resuelven

Los patrones creacionales ayudan a resolver problemas comunes como:

- **Complejidad en la creación**: Cuando la creación de objetos requiere lógica compleja
- **Acoplamiento**: Reducir el acoplamiento entre el código cliente y las clases concretas
- **Reutilización**: Facilitar la reutilización de código de creación
- **Flexibilidad**: Permitir cambiar fácilmente qué objetos se crean sin modificar el código cliente

## Ventajas Principales

1. **Encapsulación**: Ocultan la lógica de creación de objetos
2. **Flexibilidad**: Facilitan la introducción de nuevos tipos de objetos
3. **Control**: Proporcionan mayor control sobre el proceso de instanciación
4. **Reutilización**: Promueven la reutilización de código de creación

## Cuándo Usar Patrones Creacionales

Considera usar patrones creacionales cuando:

- El sistema debe ser independiente de cómo se crean sus productos
- Necesitas controlar el número de instancias de una clase
- La construcción de objetos es compleja y requiere múltiples pasos
- Quieres evitar el acoplamiento directo con clases concretas
