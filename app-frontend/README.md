## NGINX server with static files  

Static files are saved in the src folder.


### Enabling TLS  

For enabling tls mode we generate the certs with 

`openssl genrsa -out domain.key 2048`  
`openssl req -new -key domain.key -out domain.csr -subj "/CN=friendly.eats.de"`  
`openssl x509 -req -days 365 -in domain.csr -signkey domain.key -out domain.crt`  

sample test certs are in certs folder