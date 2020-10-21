from django.db import models

class Cart(models.Model):
    user          = models.ForeignKey('user.User', on_delete = models.CASCADE)
    product       = models.ForeignKey('product.Product', on_delete = models.CASCADE)
    quantity      = models.PositiveIntegerField(default = 1)
    total_price   = models.DecimalField(max_digits = 10, decimal_places = 2)

    class Meta:
        db_table = 'carts'