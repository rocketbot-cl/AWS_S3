



# AWS_S3
  
Module to connect to AWS S3 Bucket  
  
![banner](imgs/Banner_AWS_S3.jpg)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



## Description of the commands

### Connection to Aws
  
Enter the data for the connection
|Parameters|Description|example|
| --- | --- | --- |
|Host Name / Host IP|Address of the server to connect to||
|Secret Access Key|Username||
|Assign result to a Variable|Variable where the state of the connection will be stored, returns True if it is successful or False otherwise|Variable|

### Get list of Buckets
  
Get list of Buckets
|Parameters|Description|example|
| --- | --- | --- |
|Assign result to a Variable|Variable where the list will be stored|Variable|

### Get list of objects in a bucket
  
Get list of objects in a bucket
|Parameters|Description|example|
| --- | --- | --- |
|Bucket name|Bucket name|name_bucket|
|Assign result to a Variable|Variable where the list of objects will be stored|Variable|

### Upload File
  
Upload a file to a bucket
|Parameters|Description|example|
| --- | --- | --- |
|Archivo|Select the file to upload||
|Name with which the file will be uploaded||new_name|
|Bucket name||name_bucket|
|Assign result to a Variable|Variable where the result will be stored|Variable|

### Donwload File
  
Download a file from a Bucket
|Parameters|Description|example|
| --- | --- | --- |
|Object Name||name_object|
|Bucket Name||name_bucket|
|File Path||file_path|
|Assign result to a Variable|Variable where the result will be stored|Variable|
