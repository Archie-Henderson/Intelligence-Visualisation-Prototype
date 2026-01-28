from data_visualisation import views
from django.urls import path

app_name = 'data_visualisation'

urlpatterns = [
    path('', views.graph_view, name='graph'),
    path('entities/<int:ent_id>',views.entity_details, name='ent_details')
]