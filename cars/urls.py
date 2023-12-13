from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
#router.register('cars', views.CarViewSet, basename='cars')
router.register('owners', views.OwnerViewSet)


owners_router = routers.NestedDefaultRouter(router, 'owners', lookup='owner')
owners_router.register('cars', views.CarViewSet, basename='owner-cars')


# URLConf
urlpatterns = router.urls + owners_router.urls
