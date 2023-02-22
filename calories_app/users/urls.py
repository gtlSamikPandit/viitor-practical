from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
urlpatterns = router.urls

urlpatterns += [
    url(r'^user/', include('rest_auth.urls')),
    url(r'^user/registration/', include('rest_auth.registration.urls'))
]
