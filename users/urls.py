from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.homepage, name = 'home'),
    path('signup/', views.SignupView.as_view(), name='signup' ),
    path('profile/', views.UpdateProfile.as_view(), name='profile'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('all_users/', views.UserListView.as_view(), name = 'all_users'),
    path('delete_user/<int:pk>', views.UserDeleteView.as_view(), name = 'delete_user'),
    
    path('staff_register', views.StaffRegisterCreationView.as_view(), name = 'staff_register'),
    path('start_cart', views.start_cart, name = 'start_cart'),
    path('search_user/', views.search_user, name='search_user'),
    path('create_cart/<int:pk>', views.create_cart, name = 'create_cart'),

]