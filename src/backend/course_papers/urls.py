from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from applications.views import CoursePapersViewSet

urlpatterns = [
    path('api/course_papers/<str:id>/stages', CoursePapersViewSet.as_view({'post': 'update_stage', 'get': 'list_stages'}), name='course_papers_get_list'),
    path('api/course_papers/<str:id>/stages:count', CoursePapersViewSet.as_view({'get': 'count_stages'}), name='course_papers_stages_get_count'),
    path('api/course_papers:count', CoursePapersViewSet.as_view({'get': 'count'}), name='course_papers_get_count'),
    path('api/course_papers', CoursePapersViewSet.as_view({'post': 'create', 'get': 'list'}), name='course_papers_get_list'),
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]
