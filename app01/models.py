from django.db import models

# Create your models here.
class Person(models.Model):
    #django ORM会帮助我们自动创建一个主键
    # id=models.AutoField(primary_key=True)
                    #verbose_name修改的是后台显示字段的名字
    name=models.CharField(max_length=32,verbose_name="姓名")
    age=models.IntegerField(verbose_name="年龄")
    height=models.DecimalField(max_digits=5,decimal_places=2,verbose_name="身高")
    birthday=models.DateField(verbose_name="出生日期")




    def __str__(self):
        return self.name#返回字段的值

    class Meta:
        db_table='person'

        #显示的是后台模块的名字
        verbose_name="用户"
        verbose_name_plural=verbose_name