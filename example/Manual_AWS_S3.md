# AWS_S3
  
Module to connect to AWS S3 Bucket  

*Read this in other languages: [English](Manual_AWS_S3.md), [Português](Manual_AWS_S3.pr.md), [Español](Manual_AWS_S3.es.md)*
  
![banner](imgs/Banner_AWS_S3.jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Connection to Aws
  
This command allows you to connect to Aws
|Parameters|Description|example|
| --- | --- | --- |
|Access Key Id|AWS account identifier|IKAMLSURT6HYUHRY48EF|
|Secret Access Key|AWS account secret key|JYFifnrufd2pGHJ2illrZMVnhwxQnHSY5JK6JdhCtu|
|Assign result to a Variable|Variable where the state of the connection will be stored, returns True if it is successful or False otherwise|Variable|

### Get list of Buckets
  
This command allows you to get a list of buckets in your AWS account
|Parameters|Description|example|
| --- | --- | --- |
|Assign result to a Variable|Variable where the list will be stored|Variable|

### Get list of objects in a bucket
  
This command allows you to get a list of objects in a bucket from your AWS account
|Parameters|Description|example|
| --- | --- | --- |
|Bucket name|Bucket name where the objects will be searched|name_bucket|
|Assign result to a Variable|Variable where the list of objects will be stored|Variable|

### Upload File
  
This command allows you to upload a file to a bucket
|Parameters|Description|example|
| --- | --- | --- |
|File|Select the file to upload||
|Name with which the file will be uploaded|Name with which the file will be uploaded to the bucket|new_name|
|Bucket name|Name of the bucket where the file will be uploaded|name_bucket|
|Assign result to a Variable|Variable where the result will be stored|Variable|

### Donwload File
  
This command allows you to download a file from a Bucket to a local folder
|Parameters|Description|example|
| --- | --- | --- |
|Object Name|Name of the object to be downloaded|name_object|
|Bucket Name|Name of the bucket where the object is located|name_bucket|
|File Path|Path where the file will be downloaded|file_path|
|Assign result to a Variable|Variable where the result will be stored|Variable|
