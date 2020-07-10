from __future__ import absolute_import
from __future__ import unicode_literals
import os
# Put Standard Library Imports Here:
import json
import traceback

# Put Third Party/Django Imports Here:
# from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_POST
from .s3_utils import S3Utils

@require_GET
def getInfo(httpRequest):
	response = """
	<html><body> 
</br></br>
S3_BUCKET_DEMO=   {0}
</br></br>
S3_FILE_DEMO={1}
</br></br> 
</br>
<a href="http://127.0.0.1:8000/getInfo"> URI: getInfo </a>
</br></br>
<a href="http://127.0.0.1:8000/getS3FileList">URI:  getS3FileList </a>
</br></br>
<a href="http://127.0.0.1:8000/getS3Info">URI:  getS3Info</a>
</br></br>
<a href="http://127.0.0.1:8000/getS3FileListWithBucket?s3_bucket=duploservices-default-demoservice">URI:  getS3FileListWithBucket?s3_bucket=duploservices-default-demoservice </a>
</br></br>
<a href="http://127.0.0.1:8000/getS3InfoFromFile?s3_bucket=duploservices-default-demoservice&s3_file=duplo-text.txt"> URI: getS3InfoFromFile?s3_bucket=duploservices-default-demoservice&s3_file=duplo-text.txt </a>
</body></html> 
	"""
	response = response.format( os.environ.get('S3_BUCKET_DEMO'),  os.environ.get('S3_FILE_DEMO'))
	return HttpResponse(response, content_type="text/html")


############ s3 file list #######
#default read bucket from env
@require_GET
def getS3FileList(httpRequest):
	s3_utils = S3Utils()
	response = s3_utils.get_s3_list_default()
	return HttpResponse(",".join(response), content_type="text/html")

#read bucket from qs
@require_GET
def getS3FileListWithBucket(httpRequest):
	s3_utils = S3Utils()
	s3_bucket = httpRequest.GET.get('s3_bucket')
	if s3_bucket is None or s3_bucket == "":
		response = ["ERROR: parameter s3_bucket is required."]
	else:
		response = s3_utils.get_s3_list(s3_bucket)
	return HttpResponse(",".join(response), content_type="text/html")


############ s3 file #######
#default bucket & s3_file  from env
@require_GET
def getS3Info(httpRequest):
	s3_utils = S3Utils()
	response = s3_utils.get_s3_file_default()
	return HttpResponse(response, content_type="text/html")

#read bucket & s3_file from qs
@require_GET
def getS3InfoFromFile(httpRequest ):
	s3_utils = S3Utils()
	s3_file = httpRequest.GET.get('s3_file')
	s3_bucket = httpRequest.GET.get('s3_bucket')
	print("===== ", s3_bucket, "/", s3_file)
	if s3_bucket is None or s3_bucket == "" or s3_file is None or s3_file == "":
		response = "ERROR: parameter s3_bucket and s3_file are required."
	else:
		response = s3_utils.get_s3_file(s3_file, s3_bucket)
	return HttpResponse(response, content_type="text/html")



