
# installation
```sh
git clone https://github.com/aditiyadwiramadani88/Django_Rest_Crud
pip install -r requirement.txt

```
 # Create token 

```
http://exsample.com/token
method post {
    "username": "admin",
    "password": "admin"
}

```
# refresh token

```
http://exsample.com/resfresh_token
mthod post = {
"refresh": ""
}

```  



# auth

```
headers Authorization: Bearer token
```
# Create Read

```
http://exsample.com/
method = get and post
post = {
	title: string,
	song: file.mp3 
	artist: string
}

```

# Edit Delete read 


```
http://exsample.com/id
method = get and put delete 
put = {
	title: string,
	song: file.mp3 
	artist: string
}

```


