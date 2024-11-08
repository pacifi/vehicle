from rest_framework import routers

from applica.apis import ConductorModelViewSet

router = routers.SimpleRouter()
router.register("conductors", ConductorModelViewSet)
app_name = "applica"
urlpatterns = router.urls