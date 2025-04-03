# Parte 1. Reunir requisitos técnicos

Trabajas como analista de vídeos publicitarios en la agencia de publicidad Sterling & Draper. Dedicas mucho tiempo a analizar tendencias de vídeos en YouTube para determinar qué contenido merece atención para la mercadotecnia.

Cada video tiene una categoría específica (entretenimiento, música, noticias y política, etc.), una región y una fecha en que se hace tendencia.

Un video puede estar en la sección de tendencias durante varios días seguidos.

Cada semana, las nuevas empleadas Melanie y Ashok te preguntan esto:

1. ¿Qué categorías estaban en las tendencias de la semana pasada?
2. ¿Cómo se distribuyeron en diversas regiones?
3. ¿Qué categorías fueron particularmente populares en los Estados Unidos?

En tu sexta semana en el trabajo, decides que ya es momento de que el proceso sea automático. Vas a crear un dashboard para Melanie y Ashok.

- ¿Qué pasos deben tomarse para diseñar y crear el dashboard?
Necesitas hablar con Melanie y Ashok sobre los contenidos de los dashboards, su diseño y los datos que se deben presentar. Luego, habla con los administradores de la base de datos y los ingenieros para saber de dónde y cómo se recolectan los datos necesarios y cómo se pueden transformar. No olvides preguntarles dónde almacenar las tablas de agregación. Por último, crea el pipeline y el dashboard.

Después de hablar con los administradores de la base de datos, reuniste unos requisitos técnicos:

- Objetivo de negocios: analizar el historial de tendencias de videos en YouTube
- Con qué frecuencia se usará el dashboard: al menos una vez al día
- Usuario objetivo del dashboard: gerentes de planificación de videos publicitarios
- Contenido de los datos del dashboard:
    - Tendencias pasadas de videos, ordenadas por día y categoría
    - Tendencias de videos, ordenadas por país
    - Una tabla de correspondencia entre categorías y países
- Parámetros para agrupar los datos:
    - Fecha y hora de tendencia
    - Categoría de video
    - País
- Los datos:
    - Historial de tendencias — valores absolutos ordenados por día (dos gráficos: números absolutos y proporción de porcentaje)
    - Eventos, ordenados por país — valores relativos (% de eventos)
    - La correspondencia entre las categorías y los países — valores absolutos (una tabla)
- Importancia: todaos los gráficos son igualmente importantes
- Fuentes de datos para el dashboard: los ingenieros prometieron crear una tabla de agregación llamada trending_by_time. Esta es la estructura:
    - record_id: la clave primaria
    - region: país/región geográfica
    - trending_date fecha y hora
    - category_title categoría del video
    - videos_count número de videos en la sección de tendencias
- La tabla está en la base de datos youtube, que se creó especialmente para tus necesidades.
- Intervalo de actualización de los datos: una vez cada 24 horas, a la media noche UTC
- Gráficos, controles de dashboard y su orden:

# Parte 2. Crear el dashboard

El filtro de fecha y hora y el de país debería modificar todos los gráficos del dashboard. Fíjate que los gráficos de historial de interacción "Historial de tendencias" e "Historial de tendencias, %" deben tener fecha y hora en el eje X.
"Historial de tendencias" debería tener el número de videos en la sección de tendencias (el campo videos_count) en el eje Y y el otro gráfico debería tener el porcentaje ahí.

Para crear el dashboard, sigue los siguientes pasos:

1. En Tableau Public, usa trending_by_time.csv (ve al final de esta página para descargarlo) para crear un dashboard modelado en el borrador.
2. Publica el dashboard en el servidor de Tableau Public. Asegúrate de que todos puedan acceder a él; intenta abrirlo en varios navegadores. Si no se puede, el revisor no podrá hacer la revisión.
3. Usa tu dashboard para responder a las preguntas que te hicieron:
    - ¿Qué categorías de videos estuvieron en tendencia más frecuentemente?
    - ¿Cómo se distribuyeron en las regiones?
    - ¿Qué categorías fueron particularmente populares en los Estados Unidos? ¿Hubo diferencias entre las categorías populares en Estados Unidos y en otros lugares?

Prepara una presentación breve con un informe (las respuestas a estas preguntas y gráficos).