



# AWS_S3
  
Módulo para conectarse a AWS S3 Bucket  
  
![banner](imgs/Banner_AWS_S3.jpg)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  



## Descripción de los comandos

### Conexion a Aws
  
Ingrese los datos para la conexion
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Access Key Id|Direccion o nombre del servidor al que se conectara||
|Secret Access Key|Nombre de usuario||
|Asignar resultado a Variable|Variable donde se almacenara el estado de la conexion, devuelve True si es exitosa o False en el caso contrario|Variable|

### Obtener Lista de Buckets
  
Obtener Lista de Buckets
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar resultado a Variable|Variable donde se almacenara la lista obtenida|Variable|

### Obtener lista de objetos en un bucket
  
Obtener lista de objetos en un bucket
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre del Bucket|Nombre del bucket|name_bucket|
|Asignar resultado a Variable|Variable donde se guardará la lista de objetos|Variable|

### Subir Archivo
  
Subir un archivo a un bucket
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Archivo|Seleccione el archivo a subir||
|Nombre con el que se subira el archivo||new_name|
|Nombre del bucket||name_bucket|
|Asignar resultado a Variable|Variable donde se almacenara el resultado|Variable|

### Descargar Archivo
  
Descarga un archivo de un Bucket
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre del Objeto||name_object|
|Nombre del Bucket||name_bucket|
|Ruta del Archivo||file_path|
|Asignar resultado a Variable|Variable donde se almacenara el resultado|Variable|
