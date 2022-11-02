import requests
from os import environ
import time
import sys
from logger import logging

logger = None

# duplo_engine =  'http://internal-masterelbduplo-1713775494.us-west-2.elb.amazonaws.com/subscriptions/' + environ.get('TENANT_ID')
# duplo_engine =  environ.get('DISCOVERY_EP') + '/subscriptions/' + environ.get('TENANT_ID')
duplo_engine =  environ.get('DUPLO_HOST') + '/subscriptions/' + environ.get('DUPLO_TENANT_ID')

def deploy_new_service(g_serviceName, aInImage, aInHeaders):
    serviceUrl = duplo_engine + '/GetEcsServices'
    response = requests.get(serviceUrl, headers=aInHeaders)
    print(response.json())
    serviceDetails = None
    for svc in response.json():
        if svc['Name'] == g_serviceName:
            serviceDetails = svc
            print("Got svc details")
            break
    
    if not serviceDetails:
        raise Exception("ECS Service details not found")

    if serviceDetails:
        print("going to fetch task details" + serviceDetails['TaskDefinition'])
        taskDetailsUrl = duplo_engine + '/FindEcsTaskDefinition'
        response = requests.post(taskDetailsUrl, headers=aInHeaders, json= {"Arn": serviceDetails['TaskDefinition']})

        if response.json():
            taskDetails = response.json()
            print(taskDetails)

            containerDef = {}
            newTaskDef = {}
            if taskDetails['ContainerDefinitions']:
                containerDef = remove_empty_from_dict(taskDetails['ContainerDefinitions'][0])

                containerDef["Image"] = aInImage

                newTaskDef = {
                    "ContainerDefinitions": [containerDef],
                    "Cpu": taskDetails['Cpu'],
                    "Family": taskDetails['Family'],
                    "InferenceAccelerators": [],
                    "Memory": taskDetails['Memory'],
                    "NetworkMode": {
                        "Value": "awsvpc"
                    }
                }
                taskUpdateUrl = duplo_engine + '/UpdateEcsTaskDefinition'
                print(newTaskDef)
                response = requests.post(taskUpdateUrl, headers=aInHeaders, json= newTaskDef)
                print("updated task defils" + str(response.status_code))
                if response.status_code == 200:
                    serviceDetails['TaskDefinition'] = response.json()
                    ecsServiceUpdateUrl = duplo_engine + '/UpdateEcsService'
                    print("going to update ecs service")
                    response = requests.post(ecsServiceUpdateUrl, headers=aInHeaders, json= serviceDetails)
                    if response.status_code == 200:
                        print("deployment success")
                    else:
                        raise Exception("Failed to update service")
                else:
                    raise Exception("Failed to create new task definition version")
            else:
                raise Exception("Container details not found in task definition")

def setup_custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    return logger

def remove_empty_from_dict(d):
    """recursively remove empty lists, empty dicts, or None elements from a dictionary"""
    if type(d) is dict:
        return dict((k, remove_empty_from_dict(v)) for k, v in d.items() if v and remove_empty_from_dict(v))
    elif type(d) is list:
        return [remove_empty_from_dict(v) for v in d if v and remove_empty_from_dict(v)]
    else:
        return d

if __name__ == '__main__':
    logger = setup_custom_logger('CustomDeploy')
    jheaders = {"Content-type": "application/json", "Authorization": "Bearer " + environ.get('DUPLO_TOKEN')}
    #jheaders = {"Content-type": "application/json"}
    deploy_new_service(sys.argv[1], sys.argv[2], jheaders)

	
