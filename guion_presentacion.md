# Guion de Presentación: Calculadora Criptográfica

> **Consejo para el presentador:** Inicia la presentación mostrando la interfaz interactiva. Utiliza este guion como referencia (puedes leerlo o parafrasearlo) al momento de ir abriendo cada uno de los 6 menús desplegables.

---

## INTRODUCCIÓN (Rompiendo el hielo)
"Hola a todos. Hoy les presento esta Terminal Criptográfica interactiva. El objetivo de este proyecto no es solo resolver problemas matemáticos, sino **exponer los procedimientos y las 'cajas negras'** que componen la criptografía moderna e histórica. Hemos dividido las principales herramientas del ámbito criptográfico en **6 módulos principales** que voy a detallar a continuación."

---

## MÓDULO 1: Fundamentos de Matemática Modular
*Abre el menú "Modular" en la calculadora.*

"Todo algoritmo de encriptación moderno basa su fuerza en matemáticas del reloj, o aritmética modular. Aquí tenemos las operaciones primitivas:"

1. **Operación Módulo:** "Es la base. Calcula el residuo de una división entera. Limita todos nuestros números a un espectro controlado."
2. **Inverso Aditivo:** "Es encontrar el 'número que falta' para que la suma dentro de un módulo llegue a cero redondo."
3. **Inversos Multiplicativos (Tradicional y AEE):** "Son fundamentales para RSA. El tradicional busca por fuerza bruta, pero el **Algoritmo Extendido de Euclides (AEE)** hace divisiones sucesivas para encontrar este inverso de forma increíblemente rápida."
4. **XOR Binario:** "El corazón físico de la criptografía de sistemas informáticos; si los bits son iguales da 0, si son diferentes da 1."
5. **MCD:** "El máximo común divisor clásico que nos permite comprobar si dos números son 'Coprimos', la regla sagrada para crear claves."

---

## MÓDULO 2: Criptografía Clásica (Histórica)
*Abre el menú "Clásica".*

"Antes de los computadores, la criptografía se basaba en sustitución y transposición de letras usando un alfabeto (A-Z + Ñ = 27 letras). Aquí simulamos cómo funcionaban las comunicaciones en las grandes guerras:"

1. **Mapeo Mód 27:** "Antes de hacer matemática pura, le asignamos a cada letra un número fijo del 0 al 26."
2. **Cifrado César:** "El más antiguo. Simplemente desplaza todas las letras a la derecha por un factor determininista."
3. **Cifrado Vernam:** "El único cifrado matemáticamente inquebrantable puro (si la clave no se repite). Suma los valores de la letra del mensaje con la letra de la llave."
4. **Afín y Sustitución:** "El *Afín* aplica una fórmula lineal (`A*x + B`), mientras que la *Sustitución Pura* es agresiva, te obliga a generar un abecedario de 27 letras totalmente nuevo y mezclado."
5. **Transposición Columnar && Atbash:** "En vez de cambiar letras, la transposición las reordena metiéndolas en una cuadrícula. Mientras que Atbash simplemente voltea el alfabeto (La A es la Z)."

---

## MÓDULO 3: Criptografía Moderna (Public-Key)
*Abre el menú "Moderna".*

"Aquí entramos en las grandes ligas. Estas son las matemáticas que usamos actualmente en nuestros bancos y cuando navegamos por internet."

1. **Simulación Sistema RSA:** "La joya de la corona asimétrica. Entregas dos números Primos (`P` y `Q`) junto con un exponente `E`. La calculadora es capaz de derivar las mallas públicas y privadas para ocultar el mensaje de forma unidireccional."
2. **Intercambio Diffie-Hellman:** "El problema de cómo acordar una contraseña cuando un espía nos está escuchando. Muestra cómo dos partes elevan un secreto al cuadrado con un módulo base para sacar un valor público compartido que los atacantes no pueden revertir (Logaritmo Discreto)."
3. **Exp. Modular Rápida:** "La calculadora no puede multiplicar un número a la potencia un millón directamente. Usa conversión binaria para multiplicar eficientemente; esto es lo que hacen los servidores de VISA."

---

## MÓDULO 4: Funciones de Resumen (HASH)
*Abre el menú "Hash".*

"En Criptografía no todo es encriptar y desencriptar; también debemos verificar que un archivo no ha sido manipulado. Para eso usamos Hashes."

1. **MD5:** "Genera una huella hexadecimal de 128 bits. Hoy en día se considera vulnerable a colisiones, pero sigue siendo excelente para comprobar que un archivo no se descargó corrupto."
2. **SHA-256:** "Es el estándar del Gobierno y el que le da vida a Bitcoin. Devuelve 64 letras/números irrompibles."
3. **SHA-512:** "Nivel paranoico de la NSA. Duplica la resistencia con una monstruosa salida en red que hace imposible derivar el texto original."

---

## MÓDULO 5: Capa de Tratamiento (Codificación)
*Abre el menú "Codificación".*

"Para que las computadoras puedan aplicarle sus matemáticas o mandar los mensajes por la antena Wifi, el texto base se tiene que estructurar como datos de máquina crudos."

1. **ASCII / Binario / Hexadecimal:** "Aquí se le muestra al estudiante en tiempo real cómo su mensaje se traduce primero al número oficial en la computadora (ASCII), y cómo ese número literalmente se dibuja como un pulso eléctrico (Ej: `01001000` en Binario) o se condensa para lectura en memesticos (Hexadecimal)."
2. **BASE64:** "Típico del desarrollo web. Agarra cualquier dato oscuro de la web y lo convierte en 64 caracteres amigables que puedes adjuntar en un email."

---

## MÓDULO 6: Blindaje Térmico (SALT)
*Abre el menú "SALT" en la aplicación.*

"Cuando las bases de datos guardan contraseñas usando Hashes, los hackers pueden usar unas tablas masivas ('Rainbow Tables') para adivinar contraseñas comunes muy rápido (Ej: averiguan el hash de '123456'). Para matarlo de raíz nació el SALT."

* **Cómo lo mostramos:** "Aquí el usuario provee un *Salt Vector* (ruido). Internamente, la calculadora concatena el texto sucio y el mensaje puro antes de disparar las funciones MD5 o SHA256. Esto vuelve inútiles todos los diccionarios mundiales de Hackers, pues el Hash ya no es de '123456', sino de algo como 'empresaXY123456'."

---

## CONCLUSIÓN FINAL
"Como pueden notar en el panel inferior, cada vez que se ejecuta una operación la aplicación no se limita a entregar un resultado seco. Revela el algoritmo, mostrando los bucles, conversiones binarias o matrices por donde los datos pasaron, siendo una herramienta formidable para validar proyectos o enseñar criptografía desde cero."
