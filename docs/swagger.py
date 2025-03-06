from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Clone Twittre API",
      default_version='V 1.1',
      description="This is the whole backend API Full Rest Json part of the Twitter social network clone project",
      contact=openapi.Contact(email="amorey2006@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
