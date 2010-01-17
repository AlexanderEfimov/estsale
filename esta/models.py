from django.db import models

class EstateType(models.Model):
    name = models.CharField(max_length=30)

class DealType(models.Model):
    name = models.CharField(max_length=30)

class Address(models.Model):
    parent_id = ForeignKey(Address)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=30)

class Media(models.Model):
    title = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    announcement = models.ForeignKey(Announcement)

class User(models.Model):
    name = models.CharField(max_length=200)
    mail = models.EmailField(max_length=200)
    is_agency = models.BooleanField()
    phone = models.IntegerField()
    address = models.ForeignKey(Address)

class Announcement(models.Model):
    text = models.TextField(max_lentg=1000)
    deal_type = models.ForeignKey(DealType)
    estate = models.ForeignKey(Estate)
    cost = models.IntegerField()
    publisher = models.ForeignKey(User)
    is_ictive = models.BooleanField()
    is_busy = models.BooleanField()
    publication_date = models.DateField()
    date = models.DateField()
    data = models.TextField(max_lentg=1000)

class Estate(models.Model):
    type = models.ForeignKey(EstateType)
    address = models.ForeignType(Address)
    house = models.CharField(max_length=30)
    structure_type = models.ForeignKey(StructureType)
    floor = models.IntegerField(max_length=30)
    floor_count = models.IntegerField(max_length=30)
    room_count = models.IntegerField(max_length=30)
    total_space = models.IntegerField(max_length=30)
    living_space = models.IntegerField(max_length=30)
    kitchen_space = models.IntegerField(max_length=30)
    bathroom_type = models.ForeignKey(BathroomType)
    balcony_type = models.ForeignKey(BalconyType)

class BalconyType(models.Model):
    name = models.CharField(max_length=100)

class BathroomType(models.Model):
    name = models.CharField(max_length=100)

class StructureType(models.Model):
    name = models.CharField(max_length=100)

class EstateAttributes(models.Model):
    attribute_id = models.ForeignKey(EstateAttribute)

class EstateAttribute(models.Model):
    name = models.CharField(max_length=100)
