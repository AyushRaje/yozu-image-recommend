from django.urls import path
from views import get_images
urlpatterns = [
    path('\get_images',get_images,name="get_images")
]
