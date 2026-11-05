# Complementos de Telemática – Seminario 1

**Autor:** Miguel López Madrid

## Qué hace el script
`Seminario_MiguelLopez.py` cifra o descifra un texto con el cifrado César: desplaza cada letra un número de posiciones en el alfabeto. Respeta mayúsculas y minúsculas y deja igual los espacios, números y signos de puntuación.

## Cómo se ejecuta
Necesita Python 3. No usa librerías externas.

```
python Seminario_MiguelLopez.py
```

Ejemplo:

```
Introduce el texto: Hola mundo
Introduce el desplazamiento: 3
¿Cifrar (c) o descifrar (d)? c
Texto cifrado: Krod pxqgr
```

## Cómo lo hice con Copilot
Usé el chat de GitHub Copilot en VS Code, en modo Ask, con este prompt:

> Crea un script sencillo en Python que cifre y descifre un texto con el cifrado César. Debe pedir por teclado el texto y el desplazamiento, y mostrar el texto cifrado y después el descifrado. Sin librerías externas y con comentarios en español.

Después le pregunté lo que no entendía:
- Qué hacen `ord()` y `chr()` y por qué se resta `base`.
- Para qué sirve el `% 26`.

**Cambio realizado:** la versión de Copilot siempre cifraba y descifraba a la vez. Añadí un menú para que el usuario elija entre cifrar (`c`) o descifrar (`d`). Para descifrar se llama a `cesar()` con `-desplazamiento`, que mueve las letras hacia atrás y deshace el cifrado.
