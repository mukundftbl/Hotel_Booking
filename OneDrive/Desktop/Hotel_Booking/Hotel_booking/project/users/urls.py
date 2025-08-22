from django.urls import path
from .views import signup,login_view,logout_view,profile

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('profile/', profile, name='profile'),
     
    
]