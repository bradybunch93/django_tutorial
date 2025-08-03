from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    html = """
    <title>Page of Pat Brady</title>
    <body>
    <p>
    What the heck is wrong with you?<br><br>
    Noting<br>
    Why?
    oh yeah!
    </p>
    </body>

    """

    return HttpResponse(html)

