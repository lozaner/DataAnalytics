# Data Analytics

Descripción General del Portafolio
Bienvenido a mi portafolio de proyectos de análisis de datos con Python. Aquí encontrarás una colección de trabajos que reflejan mi trayectoria en el campo, desde mis primeros pasos hasta los proyectos más avanzados que he desarrollado recientemente. Cada proyecto incluye un análisis detallado del problema, el proceso completo de manipulación y visualización de datos, y las soluciones implementadas.

Los proyectos están organizados de forma cronológica inversa, mostrando primero los más recientes para resaltar mi evolución y mis habilidades actuales. Mi objetivo con este portafolio es compartir no solo los resultados, sino también el aprendizaje y las herramientas que he integrado a lo largo del tiempo, incluyendo bibliotecas como pandas, NumPy, matplotlib, seaborn, y técnicas avanzadas como el modelado predictivo y el aprendizaje automático.

Este portafolio está diseñado para demostrar mi capacidad de transformar datos en información valiosa que impulsa decisiones estratégicas. Espero que disfrutes explorando mi trabajo tanto como yo disfruté creándolo.


# Proyecto 7 Aplicacion Web



---

# Proyecto 6 Análisis de Ventas de Juegos de Consola 🎮📊

## Descripción de datos
Descripción general: El conjunto de datos contiene información relacionada con videojuegos. Cada fila representa un juego con características como título, género, plataforma, año de lanzamiento, y ventas globales.
Principales columnas del conjunto de datos:

Name: Nombre del videojuego.
Platform: Plataforma en la que el juego fue lanzado (e.g., PS4, Xbox).
Year_of_Release: Año de lanzamiento del juego.
Genre: Género del videojuego (e.g., Acción, Deporte).
Global_Sales: Ventas globales del juego en millones de unidades.
NA_Sales, EU_Sales, JP_Sales: Ventas por región (Norteamérica, Europa, Japón).
Estas variables nos permitirán identificar tendencias, patrones de ventas y popularidad según región o género.

## Preprocesamiento de datos
**Revisión de datos faltantes o inconsistentes:
Año de lanzamiento: Hay valores faltantes en Year_of_Release que deben manejarse.
Ventas globales y regionales: Valores nulos o vacíos podrían indicar datos no registrados.

**Conversión de tipos de datos:
Year_of_Release puede necesitar conversión a un formato numérico o de fecha.
Las columnas de ventas (NA_Sales, etc.) podrían necesitar conversión a tipo numérico para realizar cálculos correctamente.

**Creación de nuevas variables:
Años desde el lanzamiento: Crear una columna calculada para saber cuántos años han pasado desde que el juego fue lanzado.
Ventas totales: Verificar que Global_Sales sea la suma de las ventas regionales; si no, calcularla.

**Eliminación de outliers:
Revisar las ventas extremadamente altas o bajas para evitar distorsiones en el análisis.

**Normalización o estandarización:
Para análisis comparativos, podría ser necesario escalar las ventas por región.

## Hipótesis
Al trabajar con datos relacionados con videojuegos, podríamos plantear las siguientes hipótesis:

1.- Hipótesis de ventas por región:
"Los videojuegos tienen mayores ventas en Norteamérica que en otras regiones, debido a la alta penetración de consolas en este mercado."


2.- Hipótesis sobre géneros:
"Los géneros de acción y deportes generan mayores ventas globales que otros géneros debido a su popularidad masiva."

3.- Hipótesis sobre plataformas:
"Los juegos lanzados en plataformas de última generación (e.g., PS4, Xbox One) tienen mayores ventas globales que los lanzados en plataformas antiguas."

4.-Hipótesis sobre lanzamientos recientes:
"Los videojuegos lanzados después de 2015 tienen un mayor promedio de ventas globales debido a la creciente demanda de videojuegos."

[Ver Proyecto](https://github.com/lozaner/DataAnalytics/blob/main/portfolio-DA/gamestore/Games_6.ipynb)

---
# Proyecto 5 Megaline Telecom 📱

Trabajamos como analista para el operador de telecomunicaciones Megaline. La empresa ofrece a sus clientes dos tarifas de prepago, Surf y Ultimate. El departamento comercial quiere saber cuál de los planes genera más ingresos para ajustar el presupuesto de publicidad.

Vamos a realizar un análisis preliminar de las tarifas basado en una selección de clientes relativamente pequeña. Tendrás los datos de 500 clientes de Megaline: quiénes son los clientes, de dónde son, qué tarifa usan y la cantidad de llamadas que hicieron y los mensajes de texto que enviaron en 2018. Tu trabajo es analizar el comportamiento de los clientes y determinar qué tarifa de prepago genera más ingresos.

HIPÓTESIS

El ingreso promedio de los usuarios de las tarifas Ultimate y Surf difiere.
El ingreso promedio de los usuarios en el área de estados Nueva York-Nueva Jersey es diferente al de los usuarios de otras regiones. Decidiremos qué valor alfa usar.

Explicaremos:
Cómo formulamos las hipótesis nula y alternativa.
Qué criterio utilizamos para probar las hipótesis y por qué.

[Ver Proyecto](https://github.com/lozaner/DataAnalytics/blob/main/portfolio-DA/megaline-cellphone/compañia%20telefonica.ipynb)


---
# Proyecto 4 Data Wrangling Instacart Grosery 🛒
## Descripción de los datos
El dataset contiene información transaccional de un supermercado en línea (Instacart). Los datos incluyen:

Órdenes: Información sobre las compras realizadas por los clientes (ID de cliente, número de pedido, etc.).
Productos: Listado de productos disponibles (nombres, categorías, etc.).
Departamentos: Clasificación de los productos según categorías o departamentos.
Datos temporales: Información sobre horarios y días en los que se realizan las compras.
Los datos son ricos en variables relacionadas con los hábitos de compra de los clientes, lo que facilita el análisis de comportamiento del consumidor.

## Preprocesamiento de los datos
1.- Carga de datos: Lectura de archivos CSV (u otro formato) en estructuras de datos como DataFrames de Pandas.

2.-Limpieza de datos:
Eliminación de valores nulos o duplicados.
Conversión de tipos de datos según necesidad.

3.-Transformaciones:
Creación de variables nuevas, como el tiempo entre órdenes consecutivas o la frecuencia de compra de ciertos productos.
Unión de tablas utilizando claves comunes (por ejemplo, product_id o order_id).

4.-Normalización: Cambio en los nombres de columnas para uniformidad y mejor comprensión.

## Hipótesis
1.-Patrones de recompra: Los clientes tienden a comprar productos de ciertas categorías con mayor frecuencia durante los fines de semana.

2.-Preferencias por departamento: Los productos de ciertos departamentos (como frutas y verduras) tienen un mayor porcentaje de repetición en comparación con otros.

3.-Relación entre el tiempo y las compras: Los clientes con intervalos más cortos entre pedidos probablemente sean clientes regulares con patrones de recompra estables.

4.-Ofertas y promociones: Los descuentos o promociones impactan significativamente en el volumen de compras.

[Ver Proyecto](https://github.com/lozaner/DataAnalytics/blob/main/portfolio-DA/data-wrangling-instacart/instacart-grocery.ipynb)
---
# Proyecto 3 Data Wrangling Spotify  🎤🔊
## Descripción de los datos
El archivo contiene datos relacionados con la reproducción de música en diferentes ciudades. Las columnas son las siguientes:

City: Nombre de la ciudad.
Day: Día de la semana en que se registraron las reproducciones.
Genre: Género musical reproducido.
Plays: Número de reproducciones.

## Preprocesamiento de datos
Valores ausentes: Se debe verificar si hay celdas vacías en las columnas clave.
Duplicados: Se identifican filas duplicadas en los datos.
Revisión de formatos: Asegurarse de que las columnas tienen los tipos correctos (por ejemplo, números en Plays).
Voy a realizar estos pasos a continuación. ​​

** Resultados del preprocesamiento:

Valores ausentes: No hay valores ausentes en ninguna de las columnas.
Duplicados: No hay filas duplicadas en los datos.
Tipos de datos:

City, Day, Genre: Tipo object (texto), correcto para estas variables.
Plays: Tipo int64, adecuado para el número de reproducciones.
Los datos están limpios y no requieren modificaciones en estas áreas.

## Prueba de hipótesis
Para el análisis, plantearemos la siguiente hipótesis:

Hipótesis: La cantidad promedio de reproducciones de música en "City A" es diferente de la cantidad promedio en "City B".
Voy a calcular las medias y realizar una prueba estadística (t-test) para comparar. ​​

Parece que no puedo realizar análisis de datos más avanzados en este momento. Por favor, inténtalo de nuevo más tarde o proporciona más detalles si necesitas asistencia adicional con los resultados o análisis.

[Ver Proyecto](https://github.com/lozaner/DataAnalytics/blob/main/portfolio-DA/data-wrangling-spotify/data-wrangling-spotify.ipynb)
---
# Proyecto 2 Analisis de Store Basico

## Descripción de datos
Es el análisis exploratorio y estadístico inicial que se realiza sobre un conjunto de datos. Este proceso incluye:

Verificar las dimensiones del dataset (número de filas y columnas).
Identificar los tipos de datos de cada variable (numérica, categórica, etc.).
Examinar las estadísticas descriptivas (media, mediana, moda, desviación estándar, valores mínimos y máximos).
Detectar datos faltantes o valores atípicos (outliers).
Visualizar distribuciones y relaciones entre variables.

## Preprocesamiento de datos
Es el conjunto de técnicas aplicadas para limpiar, transformar y preparar los datos para un análisis o modelo. Incluye:

Manejo de datos faltantes (imputación o eliminación).
Normalización o escalamiento de variables.
Codificación de variables categóricas (como one-hot encoding).
Eliminación de duplicados.
Transformaciones de datos (logaritmos, escalamiento, etc.).
Reducción de dimensionalidad o selección de variables relevantes.

## Prueba de hipótesis
Este proyecto se hizo limpieza general de toda la informacion asi como se creo funciones para simplicar nuestro trabajo de limpieza.




[Ver Proyecto](https://github.com/lozaner/DataAnalytics/blob/main/portfolio-DA/analisis-venta-basico-2/analis-venta-basico-2.ipynb)
---
# Proyecto 1 Analisis de Store Basico

## Descripción de los datos
El conjunto de datos incluye una lista de usuarios con los siguientes atributos:

ID del usuario (user_id): Identificador único (cadena).
Nombre del usuario (user_name): Nombre del cliente (cadena, incluye espacios y posibles inconsistencias como guiones bajos).
Edad (user_age): Edad del usuario (número flotante).
Categorías favoritas (fav_categories): Lista de categorías de productos que el usuario prefiere.
Gastos por categoría: Lista de montos gastados en cada categoría favorita (números enteros).

Ejemplo de registro:

['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]]

## Preprocesamiento de datos
Se identificaron acciones necesarias:

1. Limpieza de nombres:
Eliminar espacios en blanco al inicio y al final.
Sustituir caracteres como guiones bajos (_) por espacios para mejorar la legibilidad.
Capitalizar los nombres para mantener un formato consistente (por ejemplo, "JOHN DOE" → "John Doe").

Validación de categorías y gastos:
Verificar que cada usuario tenga el mismo número de categorías favoritas y montos de gasto asociados. Si no coinciden, se eliminarían esos registros.
Ejemplo transformado:

Antes: ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]]
Después: ['32415', 'Mike Reed', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]]

2. Exploración de datos
Una vez limpios, habría revisado los datos para comprender mejor las tendencias:

Distribución de edades: Analizar la media, mediana y rango de las edades de los usuarios.
Categorías favoritas más comunes: Identificar cuáles categorías son más populares.
Relación entre edad y categorías favoritas: Explorar si hay correlación entre la edad y las preferencias.

## Hipótesis
En este proyecto fue iniciandome en el mundo de analisis de datos siendo la parte de limpieza asi como ordenar, trasformar a minusculas o mayusculas, cambiar a enteros, etc... fue solo limpieza y procesamiento de datos buen inicio para el mundo de analista de datos.



[Ver Proyecto](https://github.com/lozaner/DataAnalytics/blob/main/portfolio-DA/analisis-venta-basico/store_1.ipynb)
---

## 👨‍💻 Autor
Creado por [Elpidio Lozano](https://github.com/lozaner).  
Para dudas o sugerencias, ¡contáctame! 😊

---
