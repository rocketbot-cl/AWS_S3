"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

base_path = tmp_global_obj["basepath"] # type: ignore
cur_path = base_path + "modules" + os.sep + "AWS_S3" + os.sep + "libs" + os.sep

if cur_path not in sys.path:
    sys.path.append(cur_path)
    
import traceback
import os
import sys
from s3Object import S3Object # type: ignore

GetParams = GetParams # type: ignore
SetVar = SetVar # type: ignore
PrintException = PrintException # type: ignore

global session_aws_connect
module = GetParams("module")
try:
    if module == "connect":

        awsAccessKeyId = GetParams("acces_id")
        awsSecretAccessKey = GetParams("secret_key")
        var_ = GetParams('var_')
        try:
            session_aws_connect = S3Object(awsAccessKeyId, awsSecretAccessKey)
            # The method is called to know if the connection is established or not
            listBuckets = session_aws_connect.listBuckets()
            connect = True
        except:
            traceback.print_exc()
            connect = False
        SetVar(var_, connect)

    if module == "getListBuckets":

        var_ = GetParams('var_')
        try:
            listBuckets = session_aws_connect.listBuckets()
            SetVar(var_, listBuckets)
        except Exception as e:
            print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
            PrintException()
            raise e

    if module == "getListObjectsInBucket":
        bucketName = GetParams("bucketName")
        var_ = GetParams('var_')
        try:
            listObjectsInBucket = session_aws_connect.listObjectsInBucket(bucketName)
            SetVar(var_, listObjectsInBucket)
        except Exception as e:
            print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
            PrintException()
            raise e
    
    if module == "uploadFileInBucket":
        fileName = GetParams("fileName")
        newFileName = GetParams("newFileName")
        bucketName = GetParams("bucketName")
        var_ = GetParams('var_')
        try:
            uploadFileInBucket = session_aws_connect.uploadFileInBucket(fileName, bucketName, newFileName)
            SetVar(var_, uploadFileInBucket)
        except Exception as e:
            print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
            PrintException()
            raise e
        
    if module == "downloadFileFromBucket":
        objectName = GetParams("objectName")
        bucketName = GetParams("bucketName")
        filePath = GetParams("filePath")
        var_ = GetParams('var_')
        
        filename = objectName.replace("/", "_")
        filePath = os.path.join(filePath, filename)
        
        try:
            downloadFileFromBucket = session_aws_connect.downloadFileFromBucket(objectName, bucketName, filePath)
            SetVar(var_, downloadFileFromBucket)
        except Exception as e:
            print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
            PrintException()
            raise e

except Exception as e:
    print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
    PrintException()
    raise e