from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator
import threading
import time

class Order(models.Model):
    '''Model for order'''

    customer_id = models.IntegerField(verbose_name='Provide the customer_id')
    

    total_amount = models.FloatField(verbose_name="Gives the total amount of all order items",default = 0,validators=[MinValueValidator(0)])

    order_created_on = models.DateTimeField( auto_now_add=True)

    order_updated_on = models.DateTimeField(auto_now=True)

    

    ORDER_STATUS = (
        ('Placed','Placed'),
        ('Accepted','Accepted'),
        ('Preparing','Preparing'),
        ('Dispatched','Dispatched'),
        ('Delivered','Delivered')
    )

    order_status = models.CharField(max_length=100,default='Placed',choices=ORDER_STATUS,verbose_name="Provide the status")#created,paid,placed

    additional_info = models.JSONField(blank=True,null=True)

    delivery_address_id = models.IntegerField(verbose_name='Provide the customer_address id from Customer Address table from CFS project')
    
    class Meta:
        app_label = 'Order'
        ordering = ['-order_updated_on']

def async_func(order_id):
    mail_fun = threading.Thread(target=order_status,args=(order_id,))
    mail_fun.start()
    return None

def order_status(order_id):
        order = Order.objects.get(id = order_id)
        time.sleep(1*60)
        order.order_status = "Accepted"
        order.save()
        print("status changed")
        time.sleep(1*60)
        order.order_status = "Preparing"
        order.save()
        print("status changed")
        time.sleep(3*60)
        order.order_status = "Dispatched"
        order.save()
        print("status changed")
        time.sleep(5*60)
        order.order_status = "Delivered"
        order.save()
        print("status changed")
        return None

class Order_Items(models.Model):

    order = models.ForeignKey('Order',on_delete=models.CASCADE,
                                verbose_name='Provides the order_id')
    
    pizza_name = models.CharField(max_length=255,verbose_name='Provide the piza name')


    PIZZA_CHOICES = (
        ('thin-crust','thin-crust'),
        ('normal','normal'),
        ('cheese-burst','cheese-burst'),
    )

    CHEESE_CHOICES = (
        ('mozzarella','mozzarella'),
        ('parmesan','parmesan'),
        ('cheddar','cheddar'),
        ('provolone','provolone'),
    )

    quantity = models.PositiveIntegerField(verbose_name="Provide the quantity of the particular published product",default=1)

    pizza_type = models.CharField(max_length=255,choices = PIZZA_CHOICES,verbose_name="Provide the pizza choice")

    cheese_type = models.CharField(max_length=255,choices = CHEESE_CHOICES,verbose_name="Provide the cheese choice")

    toppings = models.JSONField()

    amount = models.FloatField(verbose_name="Provide the amount",validators=[MinValueValidator(0)])


# Create your models here.
