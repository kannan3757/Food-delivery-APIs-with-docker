from django.urls import path
from Order.v1.order_api import OrderAPI,TrackOrder

urlpatterns = [
 path('rest/v2/create-order', OrderAPI.as_view()),
 path('rest/v2/track-order/<int:order_id>', TrackOrder.as_view())
]