from rest_framework import serializers
from Order.models import Order,Order_Items


class OrderRequest(serializers.ModelSerializer):

    TOPPINGS_CHOICES = (
        ('mushroom','mushroom'),
        ('sausage','sausage'),
        ('onion','onion'),
        ('black olives','black olives'),
        ('green pepper','green pepper'),
        ('fresh garlic','fresh garlic'),
        ('tomato','tomato'),
    )
    toppings_types = serializers.ListField(child=serializers.ChoiceField(choices=TOPPINGS_CHOICES))

    class Meta:
        model = Order_Items
        fields = ['pizza_name','pizza_type','cheese_type','amount','toppings_types','quantity']



class OrderSerializers(serializers.Serializer):
    customer_id = serializers.IntegerField(required = True)
    delivery_address_id = serializers.IntegerField(required = True)
    pizza_details = OrderRequest(many = True)