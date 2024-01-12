# AWS_S3
  
Modulo para conectarse a AWS S3 Bucket  

*Read this in other languages: [English](Manual_AWS_S3.md), [Português](Manual_AWS_S3.pr.md), [Español](Manual_AWS_S3.es.md)*
  
![banner](imgs/Banner_AWS_S3.jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Conexion a Aws
  
Este comando permite conectarse a Aws
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Access Key Id|Identificador de la cuenta de AWS|IKAMLSURT6HYUHRY48EF|
|Secret Access Key|Clave secreta de la cuenta de AWS|JYFifnrufd2pGHJ2illrZMVnhwxQnHSY5JK6JdhCtu|
|Asignar resultado a Variable|Variable donde se almacenara el estado de la conexion, devuelve True si es exitosa o False en el caso contrario|Variable|

### Obtener Lista de Buckets
  
Este comando permite obtener una lista de buckets en su cuenta de AWS
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar resultado a Variable|Variable donde se almacenara la lista obtenida|Variable|

### Obtener lista de objetos en un bucket
  
Este comando permite obtener una lista de objetos en un bucket de su cuenta de AWS
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre del Bucket|Nombre del bucket donde se buscarán los objetos|name_bucket|
|Asignar resultado a Variable|Variable donde se guardará la lista de objetos|Variable|

### Subir Archivo
  
Este comando permite subir un archivo a un bucket
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Archivo|Seleccione el archivo a subir||
|Nombre con el que se subira el archivo|Nombre con el que se subira el archivo al bucket|new_name|
|Nombre del bucket|Nombre del bucket donde se subira el archivo|name_bucket|
|Asignar resultado a Variable|Variable donde se almacenara el resultado|Variable|

### Descargar Archivo
  
Este comando permite descargar un archivo de un Bucket
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre del Objeto|Nombre del objeto que se descargara|name_object|
|Nombre del Bucket|Nombre del bucket donde se encuentra el objeto|name_bucket|
|Ruta del Archivo|Ruta donde se descargara el archivo|file_path|
|Asignar resultado a Variable|Variable donde se almacenara el resultado|Variable|
