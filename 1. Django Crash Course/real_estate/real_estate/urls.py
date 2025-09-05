from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from listings.views import (
    listing_list,
    listing_retrieve,
    listing_create,
    listing_update,
    lisitng_delete
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listing_list),
    path('listings/<pk>/', listing_retrieve),
    path('add-listing/', listing_create),
    path('listings/<pk>/edit', listing_update),
    path('listings/<pk>/delete', lisitng_delete)
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)