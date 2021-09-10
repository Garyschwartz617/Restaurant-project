from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('dish/', views.CreateDishView.as_view(), name = 'dish'),
    path('delete_dish/<int:pk>', views.DishDeleteView.as_view(), name = 'delete_dish'),

    # path('my_cards/', views.MyCardListView.as_view(), name = 'my_cards'),
    path('cart/',views.CartListView.as_view(), name = 'cart'),
    # path('profile/', views.UpdateProfile.as_view(), name='profile'),

    path('singular/<int:pk>', views.CreateSingularView.as_view(), name = 'singular'),
    path('delete_singular/<int:pk>', views.SingularDeleteView.as_view(), name = 'delete_singular'),

    # path('all_dishs/', views.DishListView.as_view(), name = 'all_dishs'),


    path('place_order/<int:pk>', views.placeorder, name = 'place_order'),

    # path('signup/', views.SignupView.as_view(), name='signup' ),
    # path('profile/', views.UpdateProfile.as_view(), name='profile'),
    # path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
]