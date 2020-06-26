from django.db import models

# Create your models here.


class Products(models.Model):
    ProductName = models.CharField(max_length=300)
    Barcode = models.CharField(max_length=300, primary_key=True)
    CostPrice = models.PositiveIntegerField()
    SellingPrice = models.PositiveIntegerField()
    Unit = [
        ("Number", "Number"),
        ("Kg", "Kg"),
    ]
    MeasuringUnit = models.CharField(
        max_length=10, choices=Unit, default="Number")
    QuantityAvilable = models.PositiveIntegerField()
    TotalQuantity = models.PositiveIntegerField(default=0, editable=False)
    total = models.PositiveIntegerField(blank=True, null=True, editable=False)


    def total_cal(self):
        totalcal = int(self.SellingPrice) * int(self.QuantityAvilable)
        return totalcal

    def save(self):
        self.total = self.total_cal()
        return super(Products, self).save()



    def __str__(self):
        return self.ProductName


