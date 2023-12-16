from django.db import models
class tabledata(models.Model):
    reg=models.CharField(max_length=15)
    name=models.CharField(max_length=40)
    fathername=models.CharField(max_length=10)
    mothername=models.CharField(max_length=20)
    phoneno=models.CharField(max_length=40)
    address=models.CharField(max_length=40)
    city=models.CharField(max_length=40)
    gender=models.CharField(max_length=40)
    course=models.CharField(max_length=40)
    btime=models.CharField(max_length=40)
    photo=models.CharField(max_length=40)
    fee=models.CharField(max_length=40)
    refee=models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class passoutdata(models.Model):
    reg=models.CharField(max_length=15)
    name=models.CharField(max_length=40)
    fathername=models.CharField(max_length=10)
    mothername=models.CharField(max_length=20)
    phoneno=models.CharField(max_length=40)
    address=models.CharField(max_length=40)
    city=models.CharField(max_length=40)
    gender=models.CharField(max_length=40)
    course=models.CharField(max_length=40)
    btime=models.CharField(max_length=40)
    photo=models.CharField(max_length=40)
    fee=models.CharField(max_length=40)
    refee=models.CharField(max_length=20)
    def __str__(self):
        return self.name


class feedata(models.Model):
    regno=models.CharField(max_length=50)
    fee=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class feetable(models.Model):
    regno=models.CharField(max_length=50)
    rem=models.CharField(max_length=50)
    totalfee=models.CharField(max_length=50)
    fee=models.CharField(max_length=50)
    date=models.CharField(max_length=50)