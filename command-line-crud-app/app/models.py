from django.db import models
class Char(models.Model):
    name = models.TextField()
    item = models.TextField()
    in_out = models.BooleanField()
# Create your models here.
def create_Char(name, item, in_out):
    n = Char(name=name, item=item, in_out=in_out)
    n.save()
    return n

def view_all():
    return Char.objects.all()

def view_in_out():
    return Char.objects.filter(in_out=True)
        

def view_filter(name):
    n = name
    contacts = Char.objects.filter(name__iexact=n)
    if len(contacts) > 0:
        return contacts[0]
    else:
        return None
    
def update(name,item):

    try:
        n = view_filter(name)
        if n:
            n.item = item
            n.save()
            return n
    except:
        return KeyError
    
def delete(name):
    n = Char.objects.get(name=name)
    n.delete()