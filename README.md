# Data Analytics

Descripción General del Portafolio
Bienvenido a mi portafolio de proyectos de análisis de datos con Python. Aquí encontrarás una colección de trabajos que reflejan mi trayectoria en el campo, desde mis primeros pasos hasta los proyectos más avanzados que he desarrollado recientemente. Cada proyecto incluye un análisis detallado del problema, el proceso completo de manipulación y visualización de datos, y las soluciones implementadas.

Los proyectos están organizados de forma cronológica inversa, mostrando primero los más recientes para resaltar mi evolución y mis habilidades actuales. Mi objetivo con este portafolio es compartir no solo los resultados, sino también el aprendizaje y las herramientas que he integrado a lo largo del tiempo, incluyendo bibliotecas como pandas, NumPy, matplotlib, seaborn, y técnicas avanzadas como el modelado predictivo y el aprendizaje automático.

Este portafolio está diseñado para demostrar mi capacidad de transformar datos en información valiosa que impulsa decisiones estratégicas. Espero que disfrutes explorando mi trabajo tanto como yo disfruté creándolo.

---
# Proyecto 8 SQL  

## Descripción del proyecto
El proyecto consiste en analizar datos de viajes en taxi en Chicago para entender patrones de comportamiento y probar hipótesis relacionadas con la duración de los viajes en función de las condiciones climáticas. El análisis se basa en tres archivos CSV obtenidos mediante consultas SQL:

project_sql_result_01.csv – Datos sobre el número de viajes por compañía de taxis el 15 y 16 de noviembre de 2017.
project_sql_result_04.csv – Datos sobre el promedio de viajes que terminaron en cada barrio de Chicago en noviembre de 2017.
project_sql_result_07.csv – Datos sobre viajes desde el Loop hasta el Aeropuerto Internacional O'Hare, incluyendo fecha y hora, condiciones climáticas y duración del viaje.

El proyecto incluye los siguientes objetivos:
- ✅ Importar y limpiar los datos.
- ✅ Realizar análisis exploratorio para identificar patrones y tendencias.
- ✅ Identificar las 10 principales compañías de taxis y barrios por número de viajes.
- ✅ Visualizar los resultados mediante gráficos.
- ✅ Probar la hipótesis sobre la relación entre la duración de los viajes y las condiciones climáticas en sábados lluviosos.

## Proceso de preprocesamiento
El preprocesamiento de datos incluyó las siguientes tareas:
1. Carga de datos: Se usaron las librerías pandas, numpy, seaborn, matplotlib y scipy para importar y manipular los datos.
2. Revisión de datos: Se verificó que los datos no tuvieran valores nulos o duplicados.
3. Corrección de tipos de datos: Se convirtió el campo de fecha y hora (start_ts) al formato datetime.
4. Eliminación de duplicados: Se eliminaron 197 registros duplicados en el archivo de viajes.
5. Tratamiento de valores atípicos: Se usó el rango intercuartil (IQR) para eliminar valores extremos en la duración de los viajes.
6. Agrupación y ordenación: Se agruparon los datos por compañía de taxis y barrios para identificar los 10 principales en cada caso.

## Hipótesis general
Hipótesis nula (H₀): La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare NO cambia significativamente los sábados lluviosos en comparación con los sábados no lluviosos.

Hipótesis alternativa (H₁): La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare cambia significativamente los sábados lluviosos en comparación con los sábados no lluviosos.

Para comprobar la hipótesis:

- ➡️ Se realizó una prueba de Levene para verificar si las varianzas de las duraciones son iguales.
- ➡️ Se aplicó una prueba t-test para determinar si hay diferencias significativas entre las medias.
- ➡️ Se estableció un nivel de significancia de 0.05 para la prueba.

---
# Proyecto 7 Aplicacion Web

## Descripción de los datos del proyecto
El proyecto se centra en crear una aplicación web utilizando Streamlit para visualizar datos de anuncios de coches. El conjunto de datos (vehicles_us.csv) contiene información detallada sobre vehículos en venta en Estados Unidos. El objetivo es desarrollar habilidades prácticas en:

Configuración de entornos virtuales en Python.
Análisis exploratorio de datos (EDA) mediante pandas y plotly-express.
Creación de una aplicación web interactiva con Streamlit para presentar los resultados.
Despliegue de la aplicación en un servicio en la nube (Render).

Los datos incluyen información sobre:

- Precio del vehículo.
- Año de fabricación.
- Marca y modelo.
- Estado (nuevo o usado).
- Tipo de combustible.
- Kilometraje.
- Ubicación geográfica, entre otros.
- Pasos del Preprocesamiento de Datos
- Carga de datos
- Leer el archivo CSV (vehicles_us.csv) usando pandas y cargarlo en un DataFrame.
- Inspeccionar el conjunto de datos con info() y head() para verificar la estructura y tipos de datos.
- Limpieza de datos
- Eliminar valores duplicados y filas con valores nulos si es necesario.
- Convertir columnas de fechas a formato datetime.
- Corregir errores tipográficos o de formato en las columnas de texto (por ejemplo, marcas o modelos).
- Transformación de datos
- Crear columnas adicionales si es necesario (por ejemplo, calcular el precio promedio por año o por tipo de vehículo).
- Redondear valores numéricos si es necesario.
- Agregación de datos
- Agrupar los datos por categoría (por ejemplo, por marca o tipo de combustible) para facilitar el análisis.
- Calcular estadísticas descriptivas (promedio, mediana, desviación estándar).
- Validación de datos
- Comprobar que las transformaciones y la limpieza se realizaron correctamente.
- Asegurarse de que no haya valores nulos o datos inconsistentes.


## Hipótesis

1. Hipótesis sobre el precio de los vehículos
2.  Hipótesis nula (H₀): El precio promedio de los vehículos no varía significativamente entre diferentes marcas.
3. Hipótesis alternativa (H₁): El precio promedio de los vehículos varía significativamente entre diferentes marcas.
4. Hipótesis sobre el año de fabricación y el precio
5. Hipótesis nula (H₀): No existe una correlación significativa entre el año de fabricación y el precio del vehículo.
6. Hipótesis alternativa (H₁): Existe una correlación significativa entre el año de fabricación y el precio del vehículo.

---

# Proyecto 6 Análisis de Ventas de Juegos de Consola 🎮📊

## Descripción de datos

Descripción General del Proyecto
El proyecto consiste en un análisis de datos de ventas de videojuegos para la tienda online Ice, que vende videojuegos a nivel mundial. El objetivo principal es identificar patrones y factores que determinan el éxito de un videojuego, con el fin de planificar campañas publicitarias efectivas y detectar proyectos prometedores para el futuro. El análisis se basa en un conjunto de datos que abarca desde 2016, y se asume que el análisis se realiza en diciembre de 2016 para planificar estrategias para el año 2017.


## Preprocesamiento de datos
1. Revisión de datos faltantes o inconsistentes:
Año de lanzamiento: Hay valores faltantes en Year_of_Release que deben manejarse.
Ventas globales y regionales: Valores nulos o vacíos podrían indicar datos no registrados.

2. Conversión de tipos de datos:
Year_of_Release puede necesitar conversión a un formato numérico o de fecha.
Las columnas de ventas (NA_Sales, etc.) podrían necesitar conversión a tipo numérico para realizar cálculos correctamente.

3. Creación de nuevas variables:
Años desde el lanzamiento: Crear una columna calculada para saber cuántos años han pasado desde que el juego fue lanzado.
Ventas totales: Verificar que Global_Sales sea la suma de las ventas regionales; si no, calcularla.

4. Eliminación de outliers:
Revisar las ventas extremadamente altas o bajas para evitar distorsiones en el análisis.

5. Normalización o estandarización:

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

[Ver Proyecto](https://github.com/lozaner/DataAnalytics/blob/main/portfolio-DA/S6-gamestore/game-6.ipynb)

---
# Proyecto 5 Megaline Telecom

Descripción General del Proyecto
El proyecto consiste en analizar los ingresos generados por dos planes tarifarios (Surf y Ultimate) ofrecidos por Megaline, una empresa de telecomunicaciones. El objetivo es determinar cuál de los dos planes genera más ingresos para poder ajustar el presupuesto de publicidad de la empresa. Para ello, se dispone de datos sobre 500 clientes, que incluyen información sobre las llamadas, mensajes y datos consumidos en 2018, así como el plan al que están suscritos.

## Preprocesamiento de los datos

1. Carga de datos
2. Cargar las cinco tablas de datos (users, calls, messages, internet, plans) en DataFrames de pandas.
3. Revisión y limpieza de datos
4. Inspeccionar los datos para identificar valores nulos y duplicados.
5. Corregir los tipos de datos (por ejemplo, convertir fechas de strings a datetime).
6. Completar o eliminar valores nulos según corresponda.
7. Redondeo de datos
8. Redondear la duración de las llamadas hacia arriba al minuto más cercano.
9. Redondear los datos de tráfico de internet al GB más cercano.
10. Creación de columnas adicionales
11. Extraer el mes de las fechas para facilitar el análisis mensual.
12. Agregación de datos por usuario y mes
13. Número total de llamadas, mensajes y datos utilizados por cada usuario al mes.
14. Crear una tabla maestra que combine todos los datos en un solo DataFrame.
15. Cálculo de ingresos mensuales
16. Restar el límite incluido en el plan al consumo real.
17. Cobrar los minutos, mensajes y datos extra.
18. Sumar la tarifa mensual del plan para obtener el ingreso mensual total.


## Descripción de la hipótesis

- Hipótesis sobre los ingresos por tarifa
- Hipótesis nula (H₀): El ingreso promedio de los usuarios de los planes Surf y Ultimate es igual.
- Hipótesis alternativa (H₁): El ingreso promedio de los usuarios de los planes Surf y Ultimate es diferente.
- Hipótesis sobre los ingresos por región
- Hipótesis nula (H₀): El ingreso promedio de los usuarios en la región de Nueva York-Nueva Jersey es igual al ingreso  promedio en otras regiones.
- Hipótesis alternativa (H₁): El ingreso promedio de los usuarios en la región de Nueva York-Nueva Jersey es diferente al   ingreso promedio en otras regiones.
- Criterio de prueba

Se utilizará una prueba t para muestras independientes para evaluar la diferencia entre los ingresos promedios.
El valor de significancia (α) se establecerá en 0.05.

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
