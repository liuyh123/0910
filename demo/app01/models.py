from django.db import models

# Create your models here.
class Person(models.Model):
    #django ORM会帮助我们自动创建一个主键
    # id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    height=models.DecimalField(max_digits=5,decimal_places=2)
    birthday=models.DateField()

    class Meta:
        db_table='person'