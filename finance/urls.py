from django.urls import path,include
from . import views


urlpatterns = [
    path('all_tipes/', views.TipeListView.as_view(), name='all_tipess' ),
    path('delete_tipe/<int:pk>', views.TipeDeleteView.as_view(), name = 'delete_tipe'),
    path('all_bills/', views.BillListView.as_view(), name='all_bills' ),
    # path('bill/<int:pk>', views.BillDetailView.as_view(), name='bill'),
    path('bill/<int:pk>', views.UpdateBillView.as_view(), name='bill'),
    path('delete_bill/<int:pk>', views.BillDeleteView.as_view(), name = 'delete_bill'),

]