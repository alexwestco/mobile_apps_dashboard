from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("dashboard/", hello.views.dashboard, name="dashboard"),
    path("create_download/", hello.views.create_download, name="create_download"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]
