
# Django Music Api

## Installation
```sh
git clone https://github.com/aditiyadwiramadani88/Django_Rest_Crud
pip install -r requirement.txt

```
 ## Create token 
 - http://exsample.com/token
- method post

```json
 {
    "username": "admin",
    "password": "admin"
}

```
## Refresh token

- http://exsample.com/resfresh_token
- method post 

```json
 {
"refresh": "tokens"
}

```  
## Auth

```
headers Authorization: Bearer token
```
## Create Read


- http://exsample.com/
- method = get and post

```json
{ 	"title": "string",
	"song": "file.mp3"
	"artist: string"
}

```

## Edit Delete read 

- http://exsample.com/id
- method = get and put delete 

```json
 {
	"title": "string",
	"song": "file.mp3" 
	"artist": "string"
}

```


