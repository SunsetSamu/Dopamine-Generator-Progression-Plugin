---
tags:
  - Python
---
# DGPP: Dopamine Generator Progression Plugin

Disclaimer: Por defecto, este plugin puede resultar molesto e irritante para personas con sensibilidad auditiva, personas asustadizas, y personas en estado de irritabilidad. Para la accesibilidad de todos he incluido opciones de deshabilitado para varias de estas funciones, de modo que pueda seguir disfrutando de ganar EXP como mini motivante. 

Plugin experimental creado por SunsetSamu

## Overview 

En una lluvia de ideas para mejorar mi hábito de dibujo diario caí en cuenta en que podría crear un plugin con python para ayudarme en el programa de manera directa, tras algunas ideas inadecuadas pensé sobre la adictiva necesidad de subir niveles en juegos competitivos.

DGPP, o "Dopamine Generator Progression Plugin (for Krita)" es una nueva manera de conseguir tu atención para que sigas dibujando a diario ¡Con Insignias y un sistema de progreso basado en experiencia que se gana con cada acción registrada por el historial! *(ninguna información de absolutamente nada es enviada a ninguna parte de ninguna manera)*

La progresión de este plugin es fácilmente engañable, le recuerdo que el objetivo de este es retener su atención de una forma creativa basada un deseo de continuar el progreso de manera honesta, si la cantidad de progreso es modificada para mayor obtención de puntos su disfrute propio también se verá afectado.

## Features

- 🎖️ **Insignias y barras de progreso animadas** que se muestran en la parte superior de su programa (esto es personalizable, junto con el tamaño de estas, versiones no intrusivas en la UI, y la capacidad de inhabilitarlas), puede configurarlas para aparecer cada que sube de nivel, cada de guarda cambios y cada que exporta su documento.

- 📟 **Docker de progresión en tiempo real** dónde se muestra su experiencia actual y la restante para su siguiente nivel!

- 🔔 **Sonidos personalizados** para activar su dopamina! Puede deshabilitar estos sonidos si le parecen molestos, así como puede cambiarlos por los suyos propios como guste.

- 📂 **Fácil de cambiar los assets** de insignias, barras de progreso y prácticamente todo lo visual por sus propias versiones!

- 🖥️ **Ligero y Compatible desde Krita 5** para aquellos quienes permanecen en sistemas operativos anteriores. Also, está en desarrollo desde una laptop i3 de 2da generación y 4gb de RAM, por lo que su funcionamiento debe estar garantizado para cualquier equipo similar o superior

- 📇 **Ranking de progresión por medio de whitelist** usando protocolos p2p para comparar tus niveles con amigos de confianza. 

- (==Pedido==) 💡 **Retos personales tipo [Habitica](https://www.psyciencia.com/habitica-app-productividad-convierte-vida-juego/)** que el mismo usuario pueda personalizar junto a una recompensa en EXP que se obtendrá al completar estos retos. 
> 	`Seria que permitas al usuario establecer "desafíos" donde se pueda escribir cosas como "hacer 30 minutos de practica de gestos al día" el usuario lo puede marcar como hecho y recibir alguna recompensa, no necesariamente implementar todo un cronometro u otra cosa, sino basarse en la buena fe del usuario que lo marcara como "hecho" cuando realmente termine. Lo que si tendría que estar es todo el tema del tiempo, periodicidad, un sistema de dificultad (mas difícil mayor recompensa), etc. (creo que seria mas una app separada que un plugin)`
 
 - 🔥 **Sistema de rachas por días** similar a Duolingo (basado en, basado en el "unix time" con plazo de hasta 26 horas). Los días acumulados no tienen efectos en la puntuación por EXP.

- (==Tentativo==) 🌐 **Progreso competitivo mundial!** podrá ver su posición en una tabla mundial mediante un sistema de webhooks y aplicaciones de Discord. Se permitirá habilitar esta opción y se pedirá un username que no necesariamente debe ser del Discord (a menos que se quiera ingresar al mismo y obtener los rangos personalizados por nivel), las puntuaciones y experiencia serán subidas constantemente al servidor en donde se irán rankeando cada hora. Así mismo cada hora se el plugin cliente descarga este ranking y se actualiza el apartado del docker. Se debe pensar también en un método para banear usuarios que se detecten como tramposos.
   ==Respecto al pedido de los retos personales==, integrar esa función en este modo competitivo puede llegar a ser considerado una trampa, por lo que tenemos dos opciones; 
   1. Que esos puntos solo cuenten en un modo offline.
   2. Establecer un contador de retos personales sin utilidad para el ranking 

	- (==Pedido==) 📡 **Retos semanales integrados** por medio de algún tipo de notificación + recompensa en EXP. Pueden estar conectados desde el Discord y ser organizados de manera manual para evitar abusos. 


## Experience Values

- Cualquier acción: 1 EXP
- Acción de Pincel, Borrador, o pluma vectorial: 3 EXP
	- Multiplicador X50 cada 100: 150 EXP
- Guardar / Cargar documento: 5 EXP
- Exportar documento: 20 EXP
	- Multiplicador X4 cada 5: 80 EXP
- Exportar TimeLapse (integrado de Krita): 100
	- Multiplicador X5 cada 20: 500 EXP

- EXP por tiempo (con documento abierto):
	- 10min: 2 EXP
	- 30min: 5 EXP
	- 1H: 10 EXP
	- 5H: 50 EXP + aviso de tomar un descanso (deshabilitable)

## Tier Levels

*Aquí ChatGPT me dió una mano:*
### Fórmula de experiencia por nivel

==Si queremos 500 niveles, ajustamos \( k \) para que la experiencia total para alcanzar el nivel 500 sea aproximadamente 2,929,458 EXP.==
$$
\[ \text{EXP\_requerida}(500) = k \times 500^2 \]
\[ 2,929,458 = k \times 250,000 \]
\[ k = \frac{2,929,458}{250,000} = 11.717832 \]
$$
Redondeamos \( k \) a 11.72.

### Implementación ajustada

Utilizando la fórmula ajustada:
$$
\[ \text{EXP\_requerida}(n) = 11.72 \times n^2 \]
$$
Aquí están algunos niveles y su experiencia requerida:

| Nivel | EXP Requerida |
| ----- | ------------- |
| 1     | 12            |
| 2     | 47            |
| 3     | 105           |
| 4     | 188           |
| 5     | 295           |
| ...   | ...           |
| 10    | 1172          |
| ...   | ...           |
| 100   | 117,200       |
| ...   | ...           |
| 250   | 732,500       |
| ...   | ...           |
| 500   | 2,929,000     |
```python
def exp_requerida(nivel, k=12):

    """

    Calcula la experiencia requerida para alcanzar un nivel dado.

    Args:

    nivel (int): El nivel para el cual se quiere calcular la experiencia.

    k (float): El factor de ajuste de la fórmula. Por defecto es 12.

    Returns:

    float: La experiencia requerida para alcanzar el nivel dado.

    """

    return k * nivel**2


def mostrar_exp_para_niveles(max_nivel, k=12):

    """

    Muestra la experiencia requerida para alcanzar niveles desde 1 hasta max_nivel.

    Args:

    max_nivel (int): El nivel máximo para el cual se quiere mostrar la experiencia.

    k (float): El factor de ajuste de la fórmula. Por defecto es 12.

    """

    for nivel in range(1, max_nivel + 1):

        exp = exp_requerida(nivel, k)

        print(f"Nivel {nivel}: {exp} EXP")

# Ejemplo de uso

mostrar_exp_para_niveles(700)  # Muestra la experiencia requerida para los niveles del 1 al 700

```
## ROADMAP

Al ser un proyecto de tiempo muy parcial no propondré fechas, pero si versiones funcionales

**Versión funcional 1: Base** 
1. [ ] Crear un docker funcional
2. [ ] Contador de acciones basado en el historial de acciones integrado en Krita
3. [ ] Primer panel de control funcional
4. [ ] Definir los valores de las acciones monitorizables para el contador
5. [ ] Guardado y lectura del contador (En dos archivos, uno es de variables privadas y otro público)
6. [ ] Guardado y lectura automáticas
7. [ ] Establecer los distintos niveles para el contador
8. [ ] Contar acciones como exportar imagen y grabación integrada
9. [ ] Establecer multiplicadores del contador
10. [ ] Variables visibles desde el panel de control
11. [ ] Botón de prueba de sonido
12. [ ] Sonidos funcionales para los niveles alcanzados
13. [ ] Sonidos desactivables 
14. [ ] Acceso rápido a los recursos del plugin desde el panel de control
15. [ ] Barra de progreso funcional para el contador
16. [ ] insignias en el docker
17. [ ] GIFs en el docker
18. [ ] Elementos visuales (PNGs) fuera del docker
19. [ ] GIFs fuera del docker (de no ser posible, saltar la parte de animado de insignias fuera del docker)
20. [ ] desaparecer elementos externos al docker al pasar el cursor cerca
21. [ ] Insignias fuera del docker al alcanzar un nivel nuevo
22. [ ] Barra de progreso fuera del docker al alcanzar un nivel nuevo
23. [ ] Opacidad dinámica de elementos fuera del docker
24. [ ] Insignias especiales y barra de progreso fuera del docker al obtener EXP por multiplicador
25. [ ] Elementos fuera del docker desactivables
26. [ ] Elementos fuera del docker con tamaño y posición configurables desde el panel de control
27. [ ] CONTROL DE CALIDAD
28. [ ] Primera versión a GitHub :>