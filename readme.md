### Simple Fastapi App with KUBERNETES

# Base

Minikube k8s based  Simple backend application that is hosted on cluster.

## Requirements
#### Project:
   
 - is base on minikube k8s cluster
 - uses Dockerfiles for building images
 - uses Taskfile
 - uses Fastapi to set simple endpoint
 - uses containerised "script" app as second deployment
 - uses containerised "test_connection_pod" deployment as connection tester
 
    
Fastapi requirements includes:
   - anyio==3.6.2   
   -  click==8.1.3
   - fastapi==0.89.1
   - h11==0.14.0
   - idna==3.4
   - pydantic==1.10.4
   - sniffio==1.3.0
   - starlette==0.22.0
   - typing_extensions==4.4.0
   - uvicorn==0.20.0


#### Building

Project is operated via Taskfile. Base commands are presented below:
  ####k8s - main-k8s
  - main-create - starts and creates minikube env

  - minikube-build - builds docker images 

  - main-load - loads docker images to minikube cluster

  - create-cronjob - creates cronjob (testing)

  - port-forward - forwards port for a local use (Overall app should be exposed with ingress - #TODO)

  #### Docker 
  - build-base - creates image for base app
  - run-base - runs base app
  - build-script - creates image for script
  - run-script - runs script



