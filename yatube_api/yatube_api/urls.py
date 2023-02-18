from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc3MjczODM1LCJqdGkiOiI2NGQ4NGUxYzVhYWQ0ZDk3OGIwOWI3NTQ3MTVjZDdkZSIsInVzZXJfaWQiOjF9.ngLq91bVadysCbnEgs53prcU9pAWj_tgdqw-3x3x-Ko