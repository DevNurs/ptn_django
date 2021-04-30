from django.urls import path
from .views import (
    index,
    get_data,
    post_data,
    detail_data,
    update_data,
    delete_data,
)

urlpatterns = [
    path('index/', index, name='index'),
    path('', get_data, name='data'),
    path('postdata/', post_data, name='create_data'),
    path('detail/<int:id>/', detail_data, name='detail_data'),
    path('update/<int:id>/', update_data, name='update_data'),
    path('delete/<int:id>/', delete_data, name='delete_data'),
]
