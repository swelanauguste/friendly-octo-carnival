from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from search.views import SearchView

urlpatterns = [
    path("", SearchView.as_view(), name="search"),
    path("incoming/", include("incoming.urls", namespace="incoming")),
    path("search/", include("search.urls", namespace="search")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
