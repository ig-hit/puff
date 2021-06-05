from rest_framework.routers import SimpleRouter
from django.conf.urls import url
from user import views

router = SimpleRouter()

urlpatterns = router.urls + [
    url('jwt/create', views.TokenObtainPairView.as_view(), name='jwt-create'),
]
