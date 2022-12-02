import boto3
import os

class S3Object:
    def __init__(self, awsAccessKeyId, awsSecretAccessKey):
        self.session = boto3.Session(aws_access_key_id=awsAccessKeyId, aws_secret_access_key=awsSecretAccessKey)
        
    def listBuckets(self):
        s3 = self.session.client("s3")
        response = s3.list_buckets()
        allBucketsNames = []

        for bucket in response['Buckets']:
            allBucketsNames.append(bucket["Name"])

        return allBucketsNames

    def listObjectsInBucket(self, bucketName):
        
        objectsInBucket = self.session.resource('s3').Bucket(bucketName).objects.all()
        allObjectsNames = []

        for eachObject in objectsInBucket:
            allObjectsNames.append(eachObject.key)

        return allObjectsNames

    def uploadFileInBucket(self, fileName, bucketName, newFileName=None):
        if newFileName is None:
            newFileName = os.path.basename(fileName)
        
        s3 = self.session.client("s3")
        try:
            s3.upload_file(fileName, bucketName, newFileName)
            response = True
        except:
            response = False

        return response

    def downloadFileFromBucket(self, objectName, bucketName, filePath):
        s3 = self.session.client("s3")
        try:
            s3.download_file(bucketName, objectName, filePath)
            response = True
        except:
            response = False

        return response
