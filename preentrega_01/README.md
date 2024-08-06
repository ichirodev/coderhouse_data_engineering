## Pasos para ejecutar
1. Instala las dependencias del proyecto con:
```bash
pip install -r requirements.txt
```

2. Rellena el archivo `.env` con los siguientes campos
```yml
NEWS_API_KEY=$YOUR_NEWS_API_KEY
REDSHIFT_USER=$YOUR_REDSHIFT_USER
REDSHIFT_PASSWORD=$YOUR_REDSHIFT_PASSWORD
REDSHIFT_DATABASE=$YOUR_REDSHIFT_DATABASE
REDSHIFT_PORT=$YOUR_REDSHIFT_PORT
```

3. Crea la tabla `news` en redshift usando la siguiente [query](sql/01_create_table_news.sql).

4. Ejecuta el script de Python que llena la tabla `news` con datos.
```bash
python main.py --clean-results-table --date=YYYY-MM-DD
```
__[!]__ La bandera `clean-results-table` hace que la tabla `news` se trunque antes de ingresar datos, resultando en una tabla que unicamente contiene los datos recíen extraidos con cada ejecución. Se recomienda eliminar esta bandera si el script escribe en una tabla final (utilizable desde otro lado).

__[!]__ La bandera `date` es necesaria para ejecutar el script, de esta forma podemos controlar los datos que leemos e ingresamos a la tabla `news`. El formato utilizado es ISO 8601 y solo acepta `date`, no `datetime`.