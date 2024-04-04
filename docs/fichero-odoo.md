# Fichero de configuración de Odoo

## Parámetros mas usados:

- `addons_path`: Especifica la ruta donde se encuentran los módulos adicionales de Odoo que deben ser cargados por el servidor.

- `data_dir`: Especifica la ruta donde Odoo almacenará los datos de la base de datos y otros archivos relacionados.

- `admin_passwd`: Contraseña del usuario administrador de la base de datos de Odoo. Si está comentado (`;`), Odoo intentará leer la contraseña del entorno.

- `csv_internal_sep`: Separador utilizado en archivos CSV importados o exportados por Odoo.

- `db_maxconn`: Número máximo de conexiones simultáneas permitidas a la base de datos.

- `db_name`: Nombre de la base de datos de Odoo que se utilizará. Si se establece como `False`, se utilizará el nombre de la base de datos que se proporciona en la URL.

- `db_template`: Nombre de la plantilla de base de datos que se utilizará para crear nuevas bases de datos. Por defecto, se utiliza `template1`.

- `dbfilter`: Expresión regular para filtrar los nombres de las bases de datos a las que un usuario tiene acceso.

- `debug_mode`: Indica si el modo de depuración está habilitado (`True`) o deshabilitado (`False`).

- `email_from`: Dirección de correo electrónico que se utilizará como remitente para los correos electrónicos generados por el sistema.

- `limit_memory_hard`: Límite máximo de memoria (en bytes) que un proceso de Odoo puede utilizar antes de ser terminado.

- `limit_memory_soft`: Límite suave de memoria (en bytes) que un proceso de Odoo puede utilizar antes de ser advertido.

- `limit_request`: Número máximo de solicitudes HTTP simultáneas que Odoo puede manejar.

- `limit_time_cpu`: Límite de tiempo de CPU (en segundos) que un proceso de Odoo puede utilizar antes de ser terminado.

- `limit_time_real`: Límite de tiempo real (en segundos) que un proceso de Odoo puede utilizar antes de ser terminado.

- `list_db`: Indica si la lista de bases de datos debe ser accesible desde el navegador web (`True`) o no (`False`).

- `log_db`, `log_handler`, `log_level`, `logfile`: Parámetros relacionados con la configuración de registro y los archivos de registro.

- `longpolling_port`: Puerto utilizado para la comunicación de largo tiempo de espera (long polling) entre el cliente y el servidor.

- `max_cron_threads`: Número máximo de hilos de proceso que pueden ejecutar tareas programadas (cron) simultáneamente.

- `osv_memory_age_limit`: Límite de edad (en horas) de los registros en caché en la memoria.

- `osv_memory_count_limit`: Número máximo de registros en caché en la memoria.

- `smtp_password`, `smtp_port`, `smtp_server`, `smtp_ssl`, `smtp_user`: Configuración para el servidor SMTP utilizado para enviar correos electrónicos desde Odoo.

- `workers`: Número de trabajadores del proceso que se utilizarán para manejar las solicitudes de Odoo. Si se establece en `0`, se utilizará el número de núcleos de CPU disponibles.

- `xmlrpc`, `xmlrpc_interface`, `xmlrpc_port`, `xmlrpcs`, `xmlrpcs_interface`, `xmlrpcs_port`: Parámetros relacionados con la configuración de los protocolos XML-RPC utilizados por Odoo para la comunicación remota.
