import requests
import pprint
from os import environ
import time
import sys
from logger import logging
from datetime import datetime, timedelta

logger = None

# duplo_engine =  'http://internal-masterelbduplo-1713775494.us-west-2.elb.amazonaws.com/subscriptions/' + environ.get('TENANT_ID')
# duplo_engine =  environ.get('DISCOVERY_EP') + '/subscriptions/' + environ.get('TENANT_ID')
duplo_engine =  environ.get('DUPLO_EP') + '/subscriptions/' + environ.get('TENANT_ID')

def deploy_new_service(g_serviceName, aInImage, aInHeaders):
    serviceUrl = duplo_engine + '/GetWebAppSiteConfig/' + g_serviceName
    response = requests.get(serviceUrl, headers=aInHeaders)
    serviceDetails = response.json()
    
    if not serviceDetails:
        raise Exception("Web App Site config details not found")

    serviceDetails["properties.linuxFxVersion"] = "DOCKER|" + aInImage
    webAppConfigUpdateUrl = duplo_engine + '/UpdateWebAppSiteConfig/' + g_serviceName
    print("going to update web app site config with new docker image name - " + aInImage)
    response = requests.post(webAppConfigUpdateUrl, headers=aInHeaders, json= serviceDetails)
    if response.status_code == 200:
        print("deployment success..")
    else:
        raise Exception("Failed to update web app")

def setup_custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    return logger

def remove_empty_from_dict(d):
    """recursively remove empty lists, empty dicts, or None elements from a dictionary"""
    if type(d) is dict:
        return dict((k, remove_empty_from_dict(v)) for k, v in d.iteritems() if v and remove_empty_from_dict(v))
    elif type(d) is list:
        return [remove_empty_from_dict(v) for v in d if v and remove_empty_from_dict(v)]
    else:
        return d

if __name__ == '__main__':
    logger = setup_custom_logger('CustomDeploy')
    jheaders = {"Content-type": "application/json", "Authorization": "Bearer " + environ.get('DUPLO_SSO_TOKEN')}
    #jheaders = {"Content-type": "application/json"}
    deploy_new_service(environ.get('WEB_APP_NAME'), sys.argv[1], jheaders)