<h1> Create token </h1>
<code>
	http://exsample.com/token
method post {
    "username": "admin",
    "password": "admin"
}

<h1>refresh token</h1>
<code>
	http://exsample.com/resfresh_token
	mthod post = {
	"refresh": ""
	}
</code>
</code>

<h1>auth</h1>
<code>
	headers Authorization: Bearer token
</code>
<h1>Create Read</h1>

<code>
	http://exsample.com/
method = get and post
post = {
	title: string,
	song: file.mp3 
	artist: string
}

</code>
<h1>Edit Delete read </h1>
<code>
	http://exsample.com/id
method = get and put delete 
put = {
	title: string,
	song: file.mp3 
	artist: string
}
</code>

