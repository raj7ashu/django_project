from django.urls import path
from .import views

app_name = "listings"

urlpatterns = [
    path('', views.index, name="index"),
    path('greetings',views.greetings,name="greetings"),
    path('all_listings', views.all_listings, name="all_listings"),
    path('mew_listing/',views.new_listing, name='new_listing'),
]
