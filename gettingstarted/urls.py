from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("dashboard/", hello.views.dashboard, name="dashboard"),
    path("seed_database/", hello.views.seed_database, name="seed_database"),
    path("admin/", admin.site.urls),
]
