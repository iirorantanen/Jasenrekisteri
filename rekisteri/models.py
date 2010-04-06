# -*- coding: utf-8 -*- 
from django.db import models


class Member(models.Model):
  fname = models.CharField('Etunimi', max_length=15)
  lname = models.CharField('Sukunimi', max_length=30)
  email = models.EmailField('Sähköpostiosoite')
  street = models.CharField('Katuosoite', max_length=50)
  town = models.CharField('Postitoimipaikka',max_length=30)
  code = models.CharField('Postinumero', max_length=10)
  kotipaikka = models.CharField(max_length=30)
  application_date = models.DateField('Hakemus jätetty')
  accepted_date = models.DateField('Hakemus hyväksytty', null=True, blank=True)
  TYY_member = models.BooleanField('TYYn jäsen')

  def __unicode__(self):
    return self.lname + ' ' +self.fname

# Create your models here.
