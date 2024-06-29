from django.urls import path
from . import views

urlpatterns = [
    # this name parameter is an identifier for this url. we can reference it somewhere else in the app.
    # pretty cool. <a href="{%url 'index' %}">Home</a>. 
    # this is called reverse URL mapping. 
    # Note: We can hard code the link as in <a href="/catalog/">Home</a>),
    #  but if we change the pattern for our home page, for example, to /catalog/index) the templates will no longer link correctly.
    #  Using a reversed URL mapping is more robust.
    path('', views.index, name='index'),
]
