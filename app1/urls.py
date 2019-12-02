from django.urls import path
from app1 import views as app1_views

urlpatterns = [
    path('articles/<int:year>', app1_views.article),
    path('get_name',app1_views.get_name),
    # path('get_name', app1_views.PersonFormView.as_view()),
    path("person_detail/<int:pk>",app1_views.person_detail)

]
