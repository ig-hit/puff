from rest_framework import routers

from puff import views

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'', views.IndexView, 'puff')

urlpatterns = router.urls
