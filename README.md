# globant_etl
Repositorio para ejercicio etl

Debo decir que lamentablemente el ejercicio no funcionó como esperaba que lo hiciera.

La idea básica era:
-- Leer un archivo csv de la red, limpiarlo y filtrarlo un poco con rutinas de python y luego pasarlo a una tabla de BigQuery.
-- Se habpian seleccionado dos archivos referidos a choques en la ciudad de Nueva York, y si bein la lectura y limpieza funcionaban bien, cuando se transferían a tablas de bigQuery, la información no pasaba correctamente
-- Luego de varias pruebas no pude lograr el cometido.
-- Adicionalmente, fue atrde cuando me percaté que esa información no era actualzada a diario, por lo que tampoco se hubiese podido ver diferencia en la data
-- Si se logró crear la función en GoogleCloud, y el cron-job respectivo, de hecho la data si se "actauliza", pero las tablas SQL no están correctas
-- Al no tener las tablas correctas, es imposible crear queries que tengan sentido

Admito que no le dediqué el tiempo mínimo necesario, también advierto que mi conocimiento previode Google Cloud es nulo, por lo que debpi pasar parte del poco tiempo dedicado a investigar

Agradezco la oportunidad
