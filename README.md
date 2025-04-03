# Data Analytics

Descripción General del Portafolio
Bienvenido a mi portafolio de proyectos de análisis de datos con Python. Aquí encontrarás una colección de trabajos que reflejan mi trayectoria en el campo, desde mis primeros pasos hasta los proyectos más avanzados que he desarrollado recientemente. Cada proyecto incluye un análisis detallado del problema, el proceso completo de manipulación y visualización de datos, y las soluciones implementadas.

Los proyectos están organizados de forma cronológica inversa, mostrando primero los más recientes para resaltar mi evolución y mis habilidades actuales. Mi objetivo con este portafolio es compartir no solo los resultados, sino también el aprendizaje y las herramientas que he integrado a lo largo del tiempo, incluyendo bibliotecas como pandas, NumPy, matplotlib, seaborn, y técnicas avanzadas como el modelado predictivo y el aprendizaje automático.

Este portafolio está diseñado para demostrar mi capacidad de transformar datos en información valiosa que impulsa decisiones estratégicas. Espero que disfrutes explorando mi trabajo tanto como yo disfruté creándolo.

---
# Proyecto 12 Uso de Tableau Dash y Pipeline
## Descripción del proyecto 📊🎥

El proyecto se centra en el análisis de tendencias de videos en YouTube con el objetivo de identificar patrones de popularidad en distintas regiones y categorías. La agencia de publicidad Sterling & Draper busca optimizar su estrategia de marketing mediante un dashboard interactivo que automatice la consulta de datos de tendencias, permitiendo que los gerentes de planificación de videos publicitarios accedan a información clave de manera eficiente.

El dashboard proporciona información sobre:
- Las categorías de videos más populares en tendencia.
- La distribución de tendencias en distintas regiones.
- La identificación de categorías particularmente populares en Estados Unidos.
- La comparación de tendencias entre EE.UU. y otros países.
- Para lograr esto, se ha creado una base de datos llamada "youtube", que almacena la tabla "trending_by_time", actualizada diariamente con información sobre la región, fecha de tendencia, categoría del video y cantidad de videos en tendencia.

## Preprocesamiento de Datos ⚙️🧹
  
Para garantizar la precisión del análisis, se realizaron los siguientes pasos de limpieza y transformación de datos:
1. Revisión y filtrado de datos:
    - Se verificó la existencia de valores nulos o inconsistentes en los campos de fecha, categoría y región.
    - Se descartaron registros duplicados para evitar conteos erróneos en los gráficos.
2. Conversión de tipos de datos:
    - Se transformaron las fechas en un formato adecuado para facilitar el análisis cronológico.
    - Se aseguraron los valores numéricos en la columna "videos_count" para permitir cálculos precisos.
3. Creación de estructuras agregadas:
    - Se agruparon los datos por fecha y categoría para identificar tendencias temporales.
    - Se agregaron métricas de conteo por región y categoría para permitir comparaciones entre países.
4. Visualización y validación:
    - Se diseñaron gráficos en Tableau para representar los datos de forma intuitiva.
    - Se realizaron pruebas de acceso y validación en distintos navegadores para garantizar la disponibilidad del dashboard.

## Hipótesis general 📌
"Las categorías Entertainment, Music y Howto & Style son las más frecuentes en tendencias a nivel global."
    - Según los análisis, estas categorías presentan el mayor número de videos en tendencia.

"Las tendencias de videos varían significativamente entre regiones."
    - Se observa que Rusia tiene la mayor proporción de videos en tendencia, seguida de EE.UU., Francia e India.

"Las categorías populares en EE.UU. difieren de las de otros países."
    - Mientras que en EE.UU. destacan Autos & Vehicles, Comedy y Education, en otras regiones las categorías pueden ser distintas.

"El análisis automatizado mediante dashboards facilita la toma de decisiones en estrategias de marketing."
    - La implementación del dashboard optimiza el acceso a la información y reduce el tiempo necesario para responder a preguntas clave sobre tendencias en YouTube.


[Ver Proyecto](https://github.com/lozaner/DataAnalytics/blob/main/portfolio-DA/S6-gamestore/game-6.ipynb)

---
# Proyecto 11 Comparacion de Grupos A/B
## Descripción del proyecto
El proyecto tiene como objetivo analizar y comparar el comportamiento de usuarios en diferentes experimentos (identificados por exp_id: 246, 247 y 248) a partir de un conjunto de eventos registrados en la aplicación. La idea principal es evaluar cómo varían las tasas de conversión y la progresión en el embudo (desde la aparición de la pantalla principal hasta la finalización de un pago) entre los distintos grupos. Para ello, se exploran aspectos como:

Volumen de Eventos y Usuarios: Se examina el número total de eventos, la cantidad de usuarios únicos y el promedio de eventos por usuario.

Embudo de Conversión: Se estudia la secuencia de eventos (por ejemplo: MainScreenAppear → OffersScreenAppear → CartScreenAppear → PaymentScreenSuccessful) para determinar en qué etapa se pierde mayor cantidad de usuarios y cuál es la proporción que completa el viaje de compra.

Comparación de Grupos Experimentales: Se realizan pruebas de diferencia de proporciones entre los grupos de control (246 y 247) y el grupo con fuentes alteradas (248) para determinar si existen diferencias estadísticamente significativas en la ejecución de cada evento del embudo.

El análisis se apoya en técnicas de limpieza y exploración de datos, visualizaciones (histogramas, gráficos de barras, líneas y scatter plots) y pruebas estadísticas (pruebas de diferencia de proporciones y cálculo del estadístico Z).

## Proceso de preprocesamiento
El preprocesamiento se llevó a cabo siguiendo estos pasos:

1. Carga e Iniciación:

- Se importaron las librerías necesarias (Pandas, NumPy, matplotlib, seaborn, SciPy, datetime y sidetable).
- Se cargó el archivo “logs_exp_us.csv” utilizando el separador adecuado, generando un DataFrame con información de eventos, identificadores de usuario, timestamp y el identificador del experimento (exp_id).

2. Exploración y Limpieza Inicial:

- Se aplicó la función info_gral() para visualizar las primeras filas, conocer la estructura de los datos, revisar la presencia de valores nulos y detectar duplicados.
- Se renombraron las columnas para facilitar el análisis (por ejemplo, 'event', 'user', 'timestamp' y 'exp_id').
- Se eliminaron duplicados y se realizó la conversión de la columna de timestamp a formato datetime, creando además una columna “date” que agrupa los eventos por día.

3. Filtrado y Validación de la Muestra:

- Se identificó el período en el que los datos son más completos (a partir del 1 de agosto de 2019), descartando un pequeño porcentaje de eventos y usuarios iniciales para evitar sesgos.
- Se verificó la distribución de usuarios por grupo experimental y se calcularon indicadores como el número total de eventos, el promedio de eventos por usuario y la proporción de usuarios que participan en cada evento.

4. Construcción del Embudo y Cálculo de Métricas:

- Se determinó el orden de los eventos clave del embudo (por ejemplo: MainScreenAppear, OffersScreenAppear, CartScreenAppear y PaymentScreenSuccessful).
- Se calcularon las transiciones entre eventos para conocer la frecuencia con la que los usuarios pasan de una etapa a la siguiente y se estimaron las proporciones de conversión en cada paso.
- Se analizaron las pérdidas en cada etapa (por ejemplo, se identificó que la mayor pérdida ocurre desde la pantalla principal, con un abandono aproximado del 38%).

5. Comparación de Grupos y Pruebas Estadísticas:

-Se evaluaron las tasas de conversión en cada grupo experimental (control 246, control 247 y el grupo 248 con fuentes alteradas).
-Se realizaron pruebas de diferencia de proporciones (usando el estadístico Z y el p-valor) tanto entre los grupos de control como comparando estos con el grupo alterado.
- Además, se desarrolló una función para automatizar las comparaciones por cada tipo de evento, verificando que la asignación de los usuarios entre grupos sea homogénea.

## Hipótesis general
El análisis busca confirmar si los grupos de control (246 y 247) se dividen de forma equitativa y si el grupo con fuentes alteradas (248) presenta diferencias en la conversión o en la ejecución de eventos. Entre los hallazgos destacan:

1. Embudo de Conversión:
- Se observa que la etapa “MainScreenAppear” es la que presenta la mayor pérdida de usuarios (38.09%).
- Solo el 47.81% de los usuarios que comienzan el embudo (MainScreenAppear) llegan a completar el proceso de pago.

2. Comparación de Grupos de Control:
- Las pruebas de diferencia de proporciones entre los grupos 246 y 247 no muestran diferencias estadísticamente significativas, lo que indica una asignación homogénea de usuarios entre ellos.
- Comparación con Grupo Alterado (248):
- Al comparar el grupo 248 contra cada uno de los grupos de control y contra el grupo combinado, no se encontraron diferencias significativas en las proporciones de usuarios que realizan cada uno de los eventos (incluyendo MainScreenAppear, OffersScreenAppear, CartScreenAppear y PaymentScreenSuccessful).

3. Nivel de Significancia:
- Se estableció un nivel de significancia de 0.05 y se realizaron 15 pruebas en total, lo que respalda la robustez de las conclusiones ante el riesgo de falsos positivos.

4. Conclusión General:
- El análisis demuestra que las muestras de los grupos de control están bien divididas y que, en comparación, el grupo con fuentes alteradas (248) no presenta diferencias significativas en términos de conversión ni en el embudo de eventos. Se concluye que las estrategias o fuentes aplicadas en el grupo 248 no afectan de manera significativa el comportamiento de los usuarios en comparación con los grupos de control.

5. Recomendaciones:
- Prestar especial atención a la alta pérdida de usuarios en la etapa de “MainScreenAppear” para mejorar el embudo de conversión.
- Considerar la realización de nuevas pruebas A/B con cambios más drásticos o modificaciones en la interfaz para ver si se pueden generar mejoras en la conversión global.
- Mantener el nivel de significancia en 0.05 o, de ser necesario, evaluarlo con un umbral más estricto (por ejemplo, 0.01) para minimizar los falsos positivos, aunque en este caso los resultados se mantienen sin diferencias significativas.


[Ver Proyecto](https://github.com/lozaner/DataAnalytics/blob/main/portfolio-DA/S6-gamestore/game-6.ipynb)

---
# Proyecto 10 Prueba A/B

## Descripción del proyecto
El objetivo principal del proyecto es analizar los resultados de un test A/B aplicado sobre un conjunto de datos provenientes de órdenes y visitas. Se busca evaluar la efectividad de dos estrategias diferentes –identificadas como Grupo A y Grupo B– mediante el estudio de indicadores clave como:

- Tasa de Conversión: Relación entre el número de pedidos y las visitas diarias.
- Tamaño Promedio de Pedido: Valor promedio de las transacciones.
- Ganancia Acumulada: Ingresos totales generados a lo largo del tiempo por cada grupo.

La meta es determinar si existe una diferencia estadísticamente significativa entre ambos grupos y, en caso afirmativo, recomendar la implementación de la estrategia que demuestre mejores resultados en términos de conversión y rentabilidad.

## Proceso de preprocesamiento
1. Importación de Librerías y Carga de Datos:

Se importaron librerías fundamentales como Pandas, NumPy, matplotlib, seaborn, SciPy (stats) y datetime.
Se cargaron tres conjuntos de datos:

- hipotesis: Contiene las propuestas y sus indicadores (Reach, Impact, Confidence, Effort) para priorizar ideas mediante los frameworks ICE y RICE.
- ordenes: Registra las transacciones con información sobre ID, fecha, revenue y asignación a grupo (A o B).
- visitantes: Contiene el número de visitas diarias por grupo.

2. Exploración y Limpieza Inicial:

- Se definió una función de revisión (info_gral) que permitió visualizar las primeras filas, tipos de datos, presencia de valores nulos y duplicados en cada dataset.
- Se convirtieron las columnas de fecha a formato datetime para garantizar la correcta manipulación temporal de los datos.

Depuración e Integración:

- Se identificaron y eliminaron usuarios que aparecían en ambos grupos, asegurando que cada usuario fuese asignado a un único grupo de prueba para evitar sesgos en el análisis.
- Se calcularon indicadores ICE y RICE para priorizar las hipótesis y establecer un orden de importancia en función de impacto, alcance, confianza y esfuerzo.

3. Generación de Variables Derivadas y Métricas:

- Se calcularon métricas acumuladas: número de transacciones, visitas acumuladas y revenue acumulado para cada grupo, generando tablas pivot y series temporales.
- Se derivaron variables como la tasa de conversión diaria (pedidos/visitas) y el tamaño promedio de pedido, así como medidas para identificar anomalías (utilizando percentiles 95 y 99).

4. Visualización y Análisis Exploratorio:

- Se generaron gráficos para visualizar y comparar:
- La rentabilidad acumulada de los grupos A y B.
- El número de transacciones acumuladas y su evolución.
- La diferencia relativa en el tamaño de pedido promedio entre los grupos.
- La tasa de conversión diaria para identificar tendencias y diferencias significativas.
- Además, se realizó un análisis de dispersión y se calcularon percentiles para detectar comportamientos atípicos.

## Hipótesis general
El análisis se centró en determinar si las diferencias observadas entre los grupos A y B eran estadísticamente significativas. Entre los hallazgos clave se destacan:

1. Conversión:

- La prueba de Mann-Whitney aplicada a los datos (después de filtrar usuarios anómalos) arrojó un p-valor menor a 0.05 (p ≈ 0.00879), lo que indica que el Grupo B presenta una tasa de conversión significativamente mayor que el Grupo A.
- La diferencia relativa en conversión se estimó en aproximadamente un 18.3%, lo que sugiere que la estrategia implementada en el Grupo B es más efectiva para convertir visitas en transacciones.

2. Tamaño Promedio de Pedido:

- Aunque el Grupo B mostró un tamaño promedio de pedido ligeramente inferior (alrededor de un 4.2% menor) en comparación con el Grupo A, la diferencia no fue estadísticamente significativa (p ≈ 0.71053).

3. Ganancia Total:

- El Grupo B generó una ganancia acumulada superior a lo largo del período analizado, lo que respalda la superioridad de su estrategia en términos de ingresos totales.
- Decisión y Recomendación:
Con base en los resultados, se recomienda detener el test A/B y considerar al Grupo B como la estrategia líder. La evidencia sugiere que la mejora significativa en la conversión (y, por ende, en la ganancia acumulada) es el factor determinante, a pesar de que el tamaño promedio de pedido no muestra diferencias significativas.

Esta decisión se justifica por:

- Mayor eficacia en conversión: El Grupo B convierte un mayor porcentaje de visitas en transacciones.
- Rentabilidad acumulada: La ganancia total del Grupo B supera a la del Grupo A.
- Estabilidad de resultados: Los análisis gráficos y estadísticos confirman la consistencia del desempeño superior del Grupo B.

[Ver Proyecto](https://github.com/lozaner/DataAnalytics/blob/main/portfolio-DA/S6-gamestore/game-6.ipynb)

---
# Proyecto 9 Analisis de Negocio 

## Descripción del proyecto
El proyecto se enfoca en el análisis de datos de una empresa dedicada a la venta de entradas para eventos. El objetivo principal es optimizar los gastos de marketing, identificando cuáles son las fuentes de adquisición y estrategias que permiten maximizar el retorno de la inversión (ROI) y el valor del cliente a lo largo del tiempo (LTV). Para ello, se utilizan distintos conjuntos de datos:

Datos de visitas: Información sobre las sesiones de usuarios en la página web, con detalles como dispositivo utilizado, tiempo de inicio y fin de sesión, y fuente de adquisición.

Datos de órdenes: Registro de las compras realizadas, que incluye la fecha de compra, el revenue generado y el identificador único del usuario.

Datos de costos: Información sobre el gasto en marketing, segmentada por fuente de adquisición y distribuida a lo largo del tiempo.

El análisis se realiza a través de un notebook que guía al usuario en el proceso de transformación, exploración y análisis de estos datos, permitiendo obtener insights clave para mejorar la eficiencia de las inversiones en marketing.

## Proceso de preprocesamiento
El preprocesamiento de los datos fue fundamental para asegurar la calidad del análisis y se llevó a cabo siguiendo estos pasos:

Carga y revisión inicial:
- Se importaron los datasets (visitas, órdenes y costos) en formato CSV.
- Se visualizó una muestra de los datos y se revisó la información general para identificar posibles valores faltantes o inconsistencias.
- Limpieza y transformación:
- Se estandarizaron los nombres de las columnas a formato snake_case para facilitar el manejo de la información.
- Se convirtieron las columnas de fechas a formato datetime para poder realizar operaciones temporales.
- Se verificaron y eliminaron posibles duplicidades o registros erróneos, asegurando la integridad de la información.
- Generación de variables adicionales:
- Se crearon nuevas columnas para facilitar el análisis, como la duración de la sesión (calculada como la diferencia entre el inicio y fin de la sesión) y agrupaciones temporales (por día, semana y mes).
- Se realizó una segmentación mediante cohortes para analizar la retención de usuarios y el comportamiento a lo largo del tiempo.
- Se combinó la información de visitas, órdenes y costos para obtener una visión integral de la relación entre gasto en marketing, adquisición de clientes y su posterior comportamiento (como el revenue generado).

Visualización y análisis exploratorio:
- Se generaron gráficos para visualizar la distribución de visitas (DAU, WAU, MAU), la duración de las sesiones y la retención de usuarios a lo largo del tiempo.
- Se analizaron los patrones de compra, identificando la temporalidad y frecuencia con la que los usuarios realizaban órdenes, así como el revenue por cohorte.

## Hipótesis general
Con base en el análisis realizado se plantea la siguiente hipótesis general:

Hipótesis:

Optimizar los gastos de marketing focalizándose en las fuentes de adquisición que generan mayor conversión y presentan un menor costo de adquisición de clientes (CAC) permitirá aumentar significativamente el retorno de inversión (ROI) y el valor a largo plazo del cliente (LTV).
Fundamentación:
- Comportamiento de usuarios: Los análisis muestran que la mayoría de las visitas provienen de dispositivos desktop, lo que sugiere una mayor intención de compra en este segmento. 
- Retención y conversión: Se evidencia que los clientes que realizan la primera compra en un periodo corto tras su primera visita tienden a generar un mayor revenue acumulado, lo que se traduce en mejores indicadores de retención.
- Optimización de inversión: Al identificar las fuentes de adquisición que, a pesar de generar un mayor gasto en marketing, convierten a un mayor número de clientes con menor CAC, se puede reorientar la inversión para maximizar el retorno y la eficiencia de los recursos asignados a campañas publicitarias.

[Ver Proyecto](https://github.com/lozaner/DataAnalytics/blob/main/portfolio-DA/S6-gamestore/game-6.ipynb)

---
# Proyecto 8 SQL  

## Descripción del proyecto
El proyecto consiste en analizar datos de viajes en taxi en Chicago para entender patrones de comportamiento y probar hipótesis relacionadas con la duración de los viajes en función de las condiciones climáticas. El análisis se basa en tres archivos CSV obtenidos mediante consultas SQL:

project_sql_result_01.csv – Datos sobre el número de viajes por compañía de taxis el 15 y 16 de noviembre de 2017.
project_sql_result_04.csv – Datos sobre el promedio de viajes que terminaron en cada barrio de Chicago en noviembre de 2017.
project_sql_result_07.csv – Datos sobre viajes desde el Loop hasta el Aeropuerto Internacional O'Hare, incluyendo fecha y hora, condiciones climáticas y duración del viaje.

El proyecto incluye los siguientes objetivos:
-  Importar y limpiar los datos.
-  Realizar análisis exploratorio para identificar patrones y tendencias.
-  Identificar las 10 principales compañías de taxis y barrios por número de viajes.
-  Visualizar los resultados mediante gráficos.
-  Probar la hipótesis sobre la relación entre la duración de los viajes y las condiciones climáticas en sábados lluviosos.

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

-  Se realizó una prueba de Levene para verificar si las varianzas de las duraciones son iguales.
-  Se aplicó una prueba t-test para determinar si hay diferencias significativas entre las medias.
-  Se estableció un nivel de significancia de 0.05 para la prueba.

[Ver Proyecto](https://github.com/lozaner/DataAnalytics/blob/main/portfolio-DA/S6-gamestore/game-6.ipynb)

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

[Ver Proyecto](https://github.com/lozaner/DataAnalytics/blob/main/portfolio-DA/S6-gamestore/game-6.ipynb)

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
