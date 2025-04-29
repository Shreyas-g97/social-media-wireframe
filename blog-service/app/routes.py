from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Shreyas'}
    return '''
<html>
    <head>
        <title>Welcome to the Blog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
        <p>Welcome to the blog service.</p>
    </body>
</html>'''