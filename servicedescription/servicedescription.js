{
	"Roles": [{
	"Name": "byohwebsite",
	"DockerImage": "duplocloud/anyservice:<hubtag>",
	"Replicas": 1,
	"Cloud":4,
	"NetworkId": "default",
	"AgentPlatform": 0,
	"ExtraConfig": "\"FOO=BAR2\"",
	"AllocationTags": "",
	"Tags": [],
	"ApplicationUrl": "",
	"IsInfraDeployment": false,
	"SecondaryTenant": "",
	"LBConfigurations": [{
		"Name": "tcp|80",
		"ReplicationControllerName": "byohwebsite",
		"Protocol": "tcp",
		"Port": "80",
		"VirtualIPAddress": null,
		"HostPort": 0,
		"IsInfraDeployment": false,
		"DnsName": null,
		"CertificateArn": null,
		"ExternalPort": 80,
		"IsInternal": false,
		"CloudName": null,
		"ForHealthCheck": false,
		"TenantId": "",
		"State": null
	}],
	"TenantId": "",
	"State": null
}],
	"TenantId": null,
	"State": null
}
