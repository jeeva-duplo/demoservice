# demoservice
A hello world python service

# run (python 2.7)
* pip install -r requirements.txt
* cd mysite
* export S3_BUCKET_DEMO=duploservices-default-demoservice
* export S3_FILE_DEMO=duplo-text.txt
* python manage.py runserver

# urls
* http://127.0.0.1:8000/
* http://127.0.0.1:8000/getS3FileList
* http://127.0.0.1:8000/getS3FileListWithBucket?s3_bucket=duploservices-default-demoservice
* http://127.0.0.1:8000/getS3Info
* http://127.0.0.1:8000/getS3InfoFromFile?s3_bucket=duploservices-default-demoservice&s3_file=duplo-text.txt
*
*
* The api uses env variables like = S3_BUCKET_DEMO/S3_FILE_DEMO  ( e.g. api = getS3FileList , getS3Info)
*
* or you may use query string for setting bucket/file parameters ( e.g. api = getS3FileListWithBucket , getS3InfoFromFile)
* NOTAE: the file contents are not tested for binary files.

