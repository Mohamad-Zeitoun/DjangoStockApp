from django.db import models

# Create your models here.

class StockData(models.Model): 
    ticker_symbol = models.CharField(max_length = 50)
    date = models.DateField()
    open_price = models.DecimalField(max_digits = 10, decimal_places = 5)
    close_price = models.DecimalField(max_digits = 10, decimal_places = 5)
    
    class Meta:
        db_table = 'StockData' 

    def __str__(self):
        return self.ticker_symbol