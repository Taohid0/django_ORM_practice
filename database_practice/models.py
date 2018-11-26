from django.db import models

# class Person(models.Model):
#     SHIRT_SIZES = (
#         ("S","Smsall"),
#         ("M","Medium"),
#         ("L","Large"),
#     )
#     name = models.CharField(max_length=30)
#     shirt_size = models.CharField(max_length=1,choices=SHIRT_SIZES)

class Musician (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician,on_delete=models.CASCADE)
    name =  models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

class Fruit(models.Model):
    name = models.CharField(max_length=100,primary_key=True)

class Fruit2 (models.Model):
    name = models.CharField(max_length=100,unique=True)

class Manufacturer(models.Model):
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)

class Topping(models.Model):
    name = models.CharField(max_length=100)

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=100)
    toppings = models.ManyToManyField(Topping)

class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Group (models.Model):
    name = models.CharField(max_length=100)
    member = models.ManyToManyField(Person,through="Membership")

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=100)

class Person1(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def baby_boomer_status(self):
        import datetime
        if self.birth_date<datetime.date(1945,8,1):
            return "Pre-boomer"
        elif self.birth_date>datetime.date(1965,1,1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        return "%s %s"%(self.first_name,self.last_name)
    test_property = "Test"

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline  = models.TextField()

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.name +="(name modified)"
        super().save(*args,**kwargs)

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()



class Student(CommonInfo):
    home_group = models.CharField(max_length=100)