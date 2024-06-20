from rest_framework import routers
from backend.users import views as user_views

router = routers.DefaultRouter()
router.register(r'users', user_views.UsersViewSet)