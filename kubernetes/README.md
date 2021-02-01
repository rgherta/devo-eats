# Kubernetes Resources

TBD

## Ingress requirements

For https we need to generate a key pair and asve as tls secret

`openssl genrsa -out ingress.key 2048`
`openssl req -new -key ingress.key -out domain.csr -subj "/CN=friendly.eats.de"`
`openssl x509 -req -days 365 -in domain.csr -signkey ingress.key -out domain.crt`

The tls secret must be created for domain

`kubectl create secret tls secret-tls-domain --cert=domain.crt --key=ingress.key`


## Create K8 resources

kubectl apply -f ./kubernetes 