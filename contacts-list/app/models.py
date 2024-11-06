from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    is_fav = models.BooleanField()


def create_contact(name, email, phone, is_fav):
    new_cont = Contact(name=name, email=email, phone=phone, is_fav=is_fav)
    new_cont.save()
    return new_cont


def all_contacts():
    return Contact.objects.all()


def find_contact_by_name(name):
    n = name
    contacts = Contact.objects.filter(name__iexact=n)
    if len(contacts) > 0:
        return contacts[0]
    else:
        return None


def favorite_contacts():

    return Contact.objects.filter(is_fav=True)


def update_contact_email(name, nemail):
    try:
        n = find_contact_by_name(name)
        if n:
            n.email = nemail
            n.save()
            return n
    except:
        return KeyError
def delete_contact(name):
    n = Contact.objects.get(name=name)
    n.delete()
    