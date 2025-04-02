from django.urls import path
from surface_app import views


urlpatterns = [
    path('', views.configure_surface, name='configure_surface'),
    path('config-complete/<str:task_id>/', views.config_complete, name='config-complete'),
    path('task-status/<str:task_id>/', views.task_status, name='task-status'),
    path('gen-key/', views.gen_encrypt_key, name='gen-surface-encrypt-key'),
    # path('retry-config/', views.retry_config, name='retry-config'),
]