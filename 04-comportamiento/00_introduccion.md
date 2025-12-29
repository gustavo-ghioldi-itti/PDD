# Patrones de Comportamiento

## ¿Qué son los Patrones de Comportamiento?

Los patrones de comportamiento se centran en los algoritmos y la asignación de responsabilidades entre objetos. No solo describen patrones de objetos o clases, sino también los patrones de comunicación entre ellos. Estos patrones caracterizan flujos de control complejos que son difíciles de seguir en tiempo de ejecución.

## Propósito

El objetivo principal de los patrones de comportamiento es identificar patrones de comunicación comunes entre objetos y realizar estos patrones de manera flexible. Se enfocan en cómo los objetos interactúan y distribuyen responsabilidades, mejorando la comunicación entre objetos dispares en un sistema.

## Problemas que Resuelven

Los patrones de comportamiento ayudan a resolver problemas como:

- **Comunicación compleja**: Cuando los objetos necesitan comunicarse de manera flexible
- **Responsabilidades**: Cuando necesitas distribuir responsabilidades entre objetos
- **Algoritmos intercambiables**: Cuando necesitas cambiar algoritmos en tiempo de ejecución
- **Notificaciones**: Cuando múltiples objetos necesitan ser notificados de cambios
- **Secuencias de operaciones**: Cuando necesitas ejecutar operaciones en un orden específico

## Ventajas Principales

1. **Flexibilidad**: Facilitan cambios en el comportamiento sin modificar el código cliente
2. **Desacoplamiento**: Reducen las dependencias entre objetos que interactúan
3. **Reutilización**: Promueven la reutilización de algoritmos y comportamientos
4. **Mantenibilidad**: Facilitan la comprensión y el mantenimiento de la lógica de negocio


## Cuándo Usar Patrones de Comportamiento

Considera usar patrones de comportamiento cuando:

- Necesitas desacoplar el emisor de una solicitud de su receptor
- Quieres cambiar algoritmos dinámicamente
- Múltiples objetos deben ser notificados de cambios en otro objeto
- Necesitas ejecutar operaciones de forma reversible (deshacer/rehacer)
- Quieres encapsular variaciones en el comportamiento
