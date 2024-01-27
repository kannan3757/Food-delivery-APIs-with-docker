from rest_framework import generics, status
from rest_framework.response import Response
from Order.models import Order,Order_Items,async_func
from Order.v1.order_serializer import OrderSerializers,OrderRequest
from rest_framework.views import APIView


class OrderAPI(generics.GenericAPIView):
    serializer_class = OrderSerializers
    #Create
    
    def post(self,request):
        '''
            Create layout

            This is used for the layout of the product
        '''
        try:
            serializer = OrderSerializers(data=request.data)
            if serializer.is_valid():
                customer_id = request.data.get('customer_id')
                address = request.data.get('delivery_address_id')
                pizza_details = request.data.get('pizza_details')
                total_amount = 0
                for obj in pizza_details:
                    toppings = obj.get('toppings_types')
                    if len(toppings) > 5:
                        return Response({"message":"Sorry,only five toppings are allowed to add for this item"},status=status.HTTP_400_BAD_REQUEST)
                order_obj = Order.objects.create(customer_id = customer_id,delivery_address_id = address)
                for obj in pizza_details:
                    toppings = {"toppings":obj.get('toppings_types')}
                    Order_Items.objects.create(order = order_obj,pizza_name = obj.get('pizza_name'),pizza_type = obj.get('pizza_type'),
                                                 cheese_type = obj.get('cheese_type'),amount = obj.get('amount'),
                                                 toppings = toppings,quantity = obj.get('quantity'))
                    total_amount = total_amount + (obj.get('amount')*obj.get('quantity'))
                order_obj.total_amount = total_amount
                order_obj.save()
                status_change = async_func(order_id=order_obj.id)
                return Response({"message":"Order placed successfully"},status=status.HTTP_201_CREATED)
            else:
                response = serializer.errors
                return Response(response,status=status.HTTP_400_BAD_REQUEST)
     
        except Exception as ex:
            order_obj.delete()
            return Response({"message": str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)
        

class TrackOrder(APIView):
    
    def get(self,request,order_id):
        '''
            Track order

            This is used for the track of the status of order
        '''
        try:
            order_obj = Order.objects.get(id = order_id)
            return Response({"message":"Your order status is "+str(order_obj.order_status)})
        except Order.DoesNotExist:
            return Response({"message":"Order id does not exist"},status=status.HTTP_404_NOT_FOUND)
     
        except Exception as ex:
            return Response({"message": str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)
