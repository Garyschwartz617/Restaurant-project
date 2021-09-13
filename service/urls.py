from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('dish/', views.CreateDishView.as_view(), name = 'dish'),
    path('delete_dish/<int:pk>', views.DishDeleteView.as_view(), name = 'delete_dish'),

    path('cart/',views.CartListView.as_view(), name = 'cart'),

    path('singular/<int:pk>', views.CreateSingularView.as_view(), name = 'singular'),
    path('delete_singular/<int:pk>', views.SingularDeleteView.as_view(), name = 'delete_singular'),

    # path('all_dishs/', views.DishListView.as_view(), name = 'all_dishs'),

    path('place_order/<int:pk>', views.placeorder, name = 'place_order'),

    path('staff-order/', views.CreateStaffOrderView.as_view(), name = 'staff_order'),
    path('delete_cart/<int:pk>', views.CartDeleteView.as_view(), name = 'delete_cart'),
    path('staff_singular/<int:pk>/', views.CreateStaffSingularView.as_view(), name = 'staff_singular'),
    path('staff_singular/<int:pk>/<int:dish_pk>', views.CreateStaffSingularView.as_view(), name = 'staff_singular_post'),
    path('delete_singular_staff/<int:pk>', views.StaffSingularDeleteView.as_view(), name = 'delete_singular_staff'),

]