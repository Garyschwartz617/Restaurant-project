from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.kitchen, name = 'kitchen'),

    path('create_ingrediant/', views.CreateIngrediantView.as_view(), name = 'all_ingrediants'),
    path('delete_ingrediant/<int:pk>', views.IngrediantDeleteView.as_view(), name = 'delete_ingrediant'),
    
    path('create_measurement/', views.CreateMeasurementView.as_view(), name = 'all_measurements'),
    path('delete_measurement/<int:pk>', views.MeasurementDeleteView.as_view(), name = 'delete_measurement'),

    path('create_transaction/', views.CreateTransactionView.as_view(), name = 'all_transactions'),

    path('create_combo/', views.CreateComboView.as_view(), name = 'all_combos'),
    path('delete_combo/<int:pk>', views.ComboDeleteView.as_view(), name = 'delete_combo'),

    # path('all_bills/', views.CreateBillView.as_view(), name = 'all_bills'),
    # path('bill/<int:pk>', views.BillDetailView.as_view(), name='bill'),
    # path('update_bill/<int:pk>', views.UpdateBillView.as_view(), name='update_bill'),
    # path('delete_bill/<int:pk>', views.BillDeleteView.as_view(), name = 'delete_bill'),

]