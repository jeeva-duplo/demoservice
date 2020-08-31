[	  
	  {
	        "EnvName": "default",
                "LocalFleet": "true", 
		"WorkFlow" : [  
					   {  
						  "Name":"PRE_DEPLOY_BUILD",
						  "PhaseType":4,
						  "BuildParams":"PHASE=PRE_DEPLOY_BUILD, FOO=BAR1",
						  "Order":0,
						  "Parallelism":2,
						  "ContainerImage":"duplocloud/zbuilder:v7"
					   },
					   {  
						  "Name":"DEPLOY",
						  "PhaseType":1,
						  "BuildParams":"PHASE=DEPLOY",
						  "Order":1,
						  "Parallelism":1,
						  "ContainerImage":null
					   },
			                   {  
						  "Name":"POST_DEPLOY_VERIFICATION",
						  "PhaseType":4,
						  "BuildParams":"PHASE=POST_DEPLOY_VERIFICATION, FOO=BAR",
						  "Order":2,
						  "Parallelism":1,
						  "ContainerImage":"duplocloud/zbuilder:v7"
					   } 
					]
	  },
	{
	        "EnvName": "dev",
                "LocalFleet": "true", 
		"WorkFlow" : [  
					   {  
						  "Name":"PRE_DEPLOY_BUILD",
						  "PhaseType":4,
						  "BuildParams":"PHASE=PRE_DEPLOY_BUILD, FOO=BAR",
						  "Order":0,
						  "Parallelism":2,
						  "ContainerImage":"duplocloud/zbuilder:v7"
					   },
					   {  
						  "Name":"DEPLOY",
						  "PhaseType":1,
						  "BuildParams":"PHASE=DEPLOY",
						  "Order":1,
						  "Parallelism":1,
						  "ContainerImage":null
					   } 
					]
	  },
	  {
	        "EnvName": "prod",
                "LocalFleet": "true", 
		"WorkFlow" : [  
					   {  
						  "Name":"DEPLOY",
						  "PhaseType":1,
						  "BuildParams":"PHASE=DEPLOY",
						  "Order":1,
						  "Parallelism":1,
						  "ContainerImage":null
					   },
			                   {  
						  "Name":"POST_DEPLOY_VERIFICATION",
						  "PhaseType":4,
						  "BuildParams":"PHASE=POST_DEPLOY_VERIFICATION, FOO=BAR",
						  "Order":2,
						  "Parallelism":1,
						  "ContainerImage":"duplocloud/zbuilder:v7"
					   } 
					]
	  }
]

