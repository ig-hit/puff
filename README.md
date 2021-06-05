**Puff tracking Service**


**Install and run:**
```bash
make install
. venv/bin/activate
make test
make server
```

**OpenAPI Documentation (Swagger):**<br>
Use `make swagger` to generate docs.<br>
Available in [resources/swagger](./resources/swagger)


**Postman endpoints:**<br>
Load [collection](./resources/postman)

**CURL:**<br>
**Login**:
```bash
curl --location --request POST 'http://localhost:4600/user/jwt/create' \
--header 'Content-Type: application/json' \
--data-raw '{
	"username": "app@app",
	"password": "app"
}'
```


**Add a Puff:**
```bash
curl --location --request POST 'http://localhost:4600/puffs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer jwt-token-from-login-url-above'
```

**Get frequencies:**
```bash
curl --location --request GET 'http://localhost:4600/puffs?from_ago=1h&group_by=1m' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer jwt-token-from-login-url-above'
```

Argument values:<br>
`s`: seconds<br>
`m`: minutes<br>
`h`: hours<br>
`d`: days<br>
`w`: weeks<br>
