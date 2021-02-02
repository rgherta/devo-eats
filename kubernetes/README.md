# Kubernetes Resources

TBD

## Ingress requirements

For https we need to generate a key pair and asve as tls secret

`openssl genrsa -out domain.key 2048`  
`openssl req -new -key domain.key -out domain.csr -subj "/CN=friendly.eats.de"`  
`openssl x509 -req -days 365 -in domain.csr -signkey domain.key -out domain.crt`  

The tls secret must be the same as used for 

`kubectl create secret tls secret-tls-domain --cert=domain.crt --key=domain.key`


## Create K8 resources

kubectl apply -f ./kubernetes 