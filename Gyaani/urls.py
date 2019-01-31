from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from core import views as user_views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from core import views as core_views

urlpatterns = [
	url(r'^$', core_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('core/',include('core.urls')),
    path('register/',user_views.UserFormView.as_view(template_name='core/registration_form.html'),name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='core/logout.html'),name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 