from django.db import models

class EstateType(models.Model):
    name = models.CharField(max_length=30)

class DealType(models.Model):
    name = models.CharField(max_length=30)

class Adress(models.Model):
    parent_id = ForeignKey(Adress)
    name = CharField(max_length=200)
    type = CharField(max_length=30)

class Media(models.Model):
    title = CharField(max_length=200)
    path = CharField(max_length=200)
    announcement = ForeignKey(Announcement)

class User(models.Model):
    name = CharField(max_length=200)
    mail = EmailField(max_length=200)
    is_agency = BooleanField()
    phone = IntegerField()
    adress = ForeignKey(Adress)

class Announcement(models.Model):
    text = TextField(max_lentg=1000)
    deal_type = ForeignKey(DealType)
    estate = ForeignKey(Estate)
    cost = IntegerField()
    publisher = ForeignKey(User)
    is_ictive = BooleanField()
    is_busy = BooleanField()
    publication_date = DateField()
    date = DateField()
    data = TextField(max_lentg=1000)

class Estate(models.Model):
    type = ForeignKey(EstateType)
    address = ForeignType(Address)
    house = CharField(max_length=30)
    structure_type = ForeignKey(StructureType)
    floor = IntegerField(max_length=30)
    floor_count = IntegerField(max_length=30)
    room_count = IntegerField(max_length=30)
    total_space = IntegerField(max_length=30)
    living_space = IntegerField(max_length=30)
    kitchen_space = IntegerField(max_length=30)
    bathroom_type = ForeignKey(BathroomType)
    balcony_type = ForeignKey(BalconyType)

class BalconyType(models.Model):
    name = CharField(max_length=100)

class BathroomType(models.Model):
    name = CharField(max_length=100)

class StructureType(models.Model):
    name = CharField(max_length=100)

class EstateAttributes(models.Model):
    attribute_id = ForeignKey(EstateAttribute)

class EstateAttribute(models.Model):
    name = CharField(max_length=100)
