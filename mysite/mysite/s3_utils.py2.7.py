import boto
import sys, os
from boto.s3.key import Key
from boto.exception import S3ResponseError
from django.conf import settings

class S3Utils:

    ############ s3 file list #######
    def get_s3_list_default(self):
        s3_bucket = settings.S3_BUCKET_DEMO
        if s3_bucket is None or s3_bucket=="":
            return ["ERROR: 'S3_BUCKET_DEMO' setting is missing"]
        return self.get_s3_list(s3_bucket)

    def get_s3_list(self, s3_bucket):
        conn = boto.connect_s3()
        bucket = conn.get_bucket(s3_bucket)
        bucket_list = bucket.list()
        results = []
        for file in bucket_list:
            key_string = str(file.key)
            results.append(key_string)
            print(file)

        return results

    ############ s3 file #######
    def get_s3_file_default(self):
        s3_bucket = settings.S3_BUCKET_DEMO
        s3_file = settings.S3_FILE_DEMO
        if s3_bucket is None or s3_bucket==""  or  s3_file is None or s3_file=="":
            return "ERROR: 'S3_BUCKET_DEMO' and 'S3_FILE_DEMO' settings are missing"
        return self.get_s3_file(s3_file, s3_bucket)

    def get_s3_file(self, s3_file, s3_bucket ):
        if s3_bucket is None or s3_bucket=="" or  s3_file is None or s3_file=="":
            return "ERROR: 's3_bucket' and 's3_file' parameter are required"
        conn = boto.connect_s3()
        bucket = conn.get_bucket(s3_bucket)
        key = bucket.get_key(s3_file)
        response = key.get_contents_as_string()
        return response

# if __name__ == "__main__":
#     s3_utils = S3Utils()
#     os.environ['S3_BUCKET_DEMO'] = "duploservices-default-demoservice"
#     os.environ['S3_FILE_DEMO'] = "duplo-text.txt"
#     files= s3_utils.get_s3_list()
#     print(files)
#     response = s3_utils.get_s3_file()
#     print(response)
