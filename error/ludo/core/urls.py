
from django.urls import path


from core.views import home, update, delete

urlpatterns = [

    path('', home, name="home"),
    path('update/<int:tudo_id>/', update, name='update'),
    path('delete/<int:tudo_id>/', delete, name="delete"),

]
