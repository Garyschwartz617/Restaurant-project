from django.urls import path,include
from . import views


urlpatterns = [
    path('create_tipes/', views.CreateTipesView.as_view(), name = 'all_tipes'),
    path('delete_tipe/<int:pk>', views.TipeDeleteView.as_view(), name = 'delete_tipe'),
    path('all_bills/', views.CreateBillView.as_view(), name = 'all_bills'),
    path('bill/<int:pk>', views.BillDetailView.as_view(), name='bill'),
    path('update_bill/<int:pk>', views.UpdateBillView.as_view(), name='update_bill'),
    path('delete_bill/<int:pk>', views.BillDeleteView.as_view(), name = 'delete_bill'),

    path('summary', views.financial_summary, name = 'summary'),

]