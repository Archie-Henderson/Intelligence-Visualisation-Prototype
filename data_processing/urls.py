from django.urls import path
from . import views

app_name = "data_processing"

urlpatterns = [
    # Core pages
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Workspace + report pages
    path('workspace/<int:report_id>/', views.workspace, name='workspace'),
    path('reports/<int:report_id>/', views.report_detail, name='report_detail'),

    # entitiy actions
    path('entity/<int:entity_id>/edit/', views.edit_entity, name='edit_entity'),
    path('entity/<int:entity_id>/delete/', views.soft_delete_entity, name='soft_delete_entity'),
    path('entity/<int:entity_id>/profile/', views.edit_entity_profile, name='edit_entity_profile'),

    # report and entity link actions
    path('report/<int:report_id>/entity/<int:entity_id>/unlink/', views.unlink_entity_from_report, name='unlink_entity_from_report'),
    path('report/<int:report_id>/entity/<int:entity_id>/relink/', views.relink_entity_to_report, name='relink_entity_to_report'),
    path('report/<int:report_id>/entity/add/', views.add_entity_to_report, name='add_entity_to_report'),
]