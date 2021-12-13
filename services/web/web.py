import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    print(os.getenv("COUNTRY"), flush=True)
    return f'''<!DOCTYPE html>
<html>
<head>
<title>Projector 14 Homework</title>
</head>

<body>
<h1>Hello World</h1>
<h2>{os.getenv("COUNTRY")}</h2>
</body>

</html> 
'''
