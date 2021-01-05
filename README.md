
<h1>install</h1>
<p>git clone https://github.com/aditiyadwiramadani88/Django_Rest_Crud</p>
<p>pip install -r requirement.txt</p>
<h1> Create token </h1>

```
	http://exsample.com/token
method post {
    "username": "admin",
    "password": "admin"
}

```
<h1>refresh token</h1>

```  
	http://exsample.com/resfresh_token
	mthod post = {
	"refresh": ""
	}

```  



<h1>auth</h1>

```
	headers Authorization: Bearer token
```
<h1>Create Read</h1>

```
	http://exsample.com/
method = get and post
post = {
	title: string,
	song: file.mp3 
	artist: string
}

```

<h1>Edit Delete read </h1>


```
	http://exsample.com/id
method = get and put delete 
put = {
	title: string,
	song: file.mp3 
	artist: string
}

```


