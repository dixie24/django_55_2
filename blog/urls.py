"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts.views import first_view, second_html_veiw, post_list_view, home_page, post_detail_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home_page),
    path('admin/', admin.site.urls),
    path('view/', first_view),
    path('html2/', second_html_veiw),
    path('posts/', post_list_view),
    path('posts/<int:post_id>/', post_detail_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
