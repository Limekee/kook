from django.urls import path
from .views import index, top_sellers
#переменная которая хранит ссылки
#функция path создает ссылку и говорит какой оброботчик будет давать на нее ответ
urlpatterns = [
    path('', index, name ='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers')
]
