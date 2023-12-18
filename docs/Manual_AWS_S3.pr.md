# AWS_S3
  
Módulo para se conectar ao AWS S3 Bucket  

*Read this in other languages: [English](Manual_AWS_S3.md), [Português](Manual_AWS_S3.pr.md), [Español](Manual_AWS_S3.es.md)*
  
![banner](imgs/Banner_AWS_S3.jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Conexão com Aws
  
Este comando permite conectar-se ao Aws
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Access Key Id|Identificador da conta AWS|IKAMLSURT6HYUHRY48EF|
|Secret Access Key|Chave secreta da conta AWS|JYFifnrufd2pGHJ2illrZMVnhwxQnHSY5JK6JdhCtu|
|Atribuir resultado à variável|Variável onde será armazenado o estado da conexão, retorna True se for bem sucedida ou False caso contrário|Variable|

### Obter Lista de Buckets
  
Este comando permite obter uma lista de buckets em sua conta AWS
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribuir resultado à variável|Variável onde será armazenada a lista obtida|Variable|

### Obter lista de objetos em um bucket
  
Este comando permite obter uma lista de objetos em um bucket de sua conta AWS
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome do Bucket|Nome do bucket onde serão procurados os objetos|name_bucket|
|Atribuir resultado à variável|Variável onde será armazenada a lista de objetos|Variable|

### Subir um Arquivo
  
Este comando permite subir um arquivo a um bucket
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Arquivo|Selecione o arquivo a subir||
|Nome com o qual o arquivo será subido|Nome com o qual o arquivo será subido ao bucket|new_name|
|Nome do bucket|Nome do bucket onde o arquivo será subido|name_bucket|
|Atribuir resultado à variável|Variável onde o resultado será armazenado|Variable|

### Donwload Arquivo
  
Este comando permite baixar um arquivo de um Bucket
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome do Objeto|Nome do objeto que será baixado|name_object|
|Nome do Bucket|Nome do bucket onde o objeto está localizado|name_bucket|
|Caminho de Arquivo|Caminho onde o arquivo será baixado|file_path|
|Atribuir resultado à variável|Variável onde será armazenado o resultado|Variable|
