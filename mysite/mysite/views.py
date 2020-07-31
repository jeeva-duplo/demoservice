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

from django.conf import settings

@require_GET
def getInfo(httpRequest):
	response = """
		<html><body>
		</br></br>
		ENV S3_BUCKET_DEMO =   {0}
		</br></br>
		ENV S3_FILE_DEMO = {1}
		</br></br>
		</br>
		<a href="/getInfo"> URI: getInfo</a>
		</br></br>
		<a href="/getS3Files">URI: getS3Files (file list)</a>
		</br></br>
		<a href="/getS3File">URI:  getS3File (file content)</a>
		</br></br>
		<a href="/getS3BucketFiles?s3_bucket={0}">URI:  getS3BucketFiles?s3_bucket={0} (file list with qs-params)</a>
		</br></br>
		<a href="/getS3BucketFile?s3_bucket={0}&s3_file={1}"> URI: getS3BucketFile?s3_bucket={0}&s3_file={1}  (file content with qs-params)</a>
		</body></html>
	"""

	response = response.format(settings.S3_BUCKET_DEMO, settings.S3_FILE_DEMO )
	return HttpResponse(response, content_type="text/html")


############ s3 file list #######
#default read bucket from env
@require_GET
def getS3FileList(httpRequest):
	s3_utils = S3Utils()
	response = s3_utils.get_s3_list_default()
	response_text = "<BR><BR>  &nbsp; &nbsp; , &nbsp;".join(response)
	return HttpResponse( "<html><body>[<BR> &nbsp; &nbsp;   {0} <BR> ]</body></html>".format(response_text) , content_type="text/html")

#read bucket from qs
@require_GET
def getS3FileListWithBucket(httpRequest):
	s3_utils = S3Utils()
	s3_bucket = httpRequest.GET.get('s3_bucket')
	if s3_bucket is None or s3_bucket == "":
		response = ["ERROR: parameter s3_bucket is required."]
	else:
		response = s3_utils.get_s3_list(s3_bucket)
	response_text = "<BR><BR> &nbsp; &nbsp; , &nbsp;".join(response)
	return HttpResponse( "<html><body>[<BR> &nbsp; &nbsp; {0} <BR> ]</body></html>".format(response_text) , content_type="text/html")


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
		response = "ERROR: parameter1 s3_bucket and s3_file are required."
	else:
		response = s3_utils.get_s3_file(s3_file, s3_bucket)
	return HttpResponse(response, content_type="text/html")
