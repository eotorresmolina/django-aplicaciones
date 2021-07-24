from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    string = '''
                <html>
                    <head>
                        <title>Index</title>
                    </head>
                    <body style='background-color:#33FFDA'>
                        <div style='background-color:black'>
                            <h1 style='color:red'>Welcome User!!</h1>
                            <h2 style='color:blue'>My first Web Page in Django!</h2>
                        </div>
                    </body>
                </html>
            '''
    return HttpResponse(string)