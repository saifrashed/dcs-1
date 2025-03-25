# Swagger generated server

## Overview
This server was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the
[OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server, you can easily generate a server stub.  This
is an example of building a swagger-enabled Flask server.

This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements
Python 3.5.2+

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080/tutorial/1.0.0/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/tutorial/1.0.0/swagger.json
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```





COMMANDS:

source venv/bin/activate

python setup.py install

pip install -r requirements.txt


pip3 install -r requirements.txt
python3 -m swagger_server


docker build --tag dcs-1/student_service .

docker run -it -p 8080:8080 dcs-1/student_service


microk8s kubectl apply -f .

microk8s status --wait-ready

microk8s kubectl delete deployment.apps/service

microk8s ctr images pull docker.io/saifrashed/student_service:latest

microk8s kubectl logs pod/service-d85858965-5pv6v




Visit deployment: http://192.168.64.2:32318/tutorial/1.0.0/ui/












- Absolute path 
cd /Users/saifrashed/Downloads/uva-master/dcs/assignment-1




