# -*- coding: utf-8 -*- 
from django.db import models
from datetime import date

class Member(models.Model):
  fname = models.CharField('Etunimi', max_length=15)
  lname = models.CharField('Sukunimi', max_length=30)
  email = models.EmailField('Sähköpostiosoite')
  street = models.CharField('Katuosoite', max_length=50, blank=True)
  code = models.CharField('Postinumero', max_length=10, blank=True)
  town = models.CharField('Postitoimipaikka',max_length=30, blank=True)
  phone = models.CharField('Puhelin', max_length=20, blank=True)
  kotipaikka = models.CharField(max_length=30)
  application_date = models.DateField('Hakemus jätetty', default=date.today())
  accepted_date = models.DateField('Hakemus hyväksytty', null=True, blank=True)
  TYY_member = models.BooleanField('TYYn jäsen')
  picture = models.ImageField('Kuva', blank=True, upload_to='member_pictures')
  admin = models.BooleanField('Admin', default=False)
  not_visible = models.BooleanField('En halua nimeni näkyvän julkisessa listauksessa')
  last_paid = models.DateField('Viimeksi maksanut', blank=True, null=True)
  

  def __unicode__(self):
    return self.lname + ' ' +self.fname

