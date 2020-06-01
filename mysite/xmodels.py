#import datetime
#from django.contrib.auth.models            import User
from django.db                              import models
from django.utils                           import timezone
from django.conf                            import settings
from django.contrib.auth                    import get_user_model
from django.urls                            import reverse

class Site(models.Model):
  notes                        = models.TextField                 (blank=True, null=True)
  datecolour                   = models.CharField                 (max_length=20, default='black')
  detailcolour                 = models.CharField                 (max_length=20, default='green')
  backgroundcolour             = models.CharField                 (max_length=20, default='yellow')
  backgroundcolourlightness    = models.IntegerField              (null=True)
  backgroundcolourx            = models.CharField                 (max_length=20, blank=True, null=True)
  backgroundcolourlightnessx   = models.IntegerField              (null=True)


class Photo(models.Model):
  notes                   = models.TextField          (blank=True, null=True)
  priority                = models.IntegerField       (default=100)
  is_live                 = models.BooleanField       (default=True)
  title                   = models.TextField          (blank=True, null=True)
  cover                   = models.ImageField         (upload_to='images/')
  created_date            = models.DateTimeField      (default=timezone.now)
  def __str__(self):
    return self.title
  def delete(self, using=None, keep_parents=False):
    self.cover.storage.delete(self.cover.path)
    super().delete()

class Event(models.Model):
  event_date        = models.DateField                              (default=timezone.now)
  detail            = models.CharField                              ('Details of event',max_length=200, blank=True,null=True)
  addendum          = models.TextField                              ('Addendum', blank=True,null=True)
  created_date      = models.DateTimeField                          (default=timezone.now)
  is_live           = models.BooleanField                           (default=True)
  status_now        = models.CharField                              (max_length=20,blank=True,null=True)
  sameday           = models.BooleanField                           (default=False)
  def __str__(self):
    return self.event_date

"""
class Person(models.Model):
  STATUSES = (
        (5, 'Contact'),
        (10, 'Public'),
        (15, 'Prospective'),
        (30, 'Member'),
        (40, 'Committee'),
        (50, 'Treasurer'),
        (60, 'Chair'),
  )
  username                = models.CharField                 (max_length=20, unique=True, blank=True, null=True)
  email                   = models.EmailField                (max_length=40, unique=True, blank=True, null=True)
  display_name            = models.CharField                 (max_length=30, unique=True)
  authorname              = models.CharField                 (max_length=20,blank = True, null = True)
  twitter_name            = models.CharField                 (max_length=40, blank=True, null=True)
  phone_a                 = models.CharField                 (max_length=20, blank=True, null=True)
  phone_b                 = models.CharField                 (max_length=20, blank=True, null=True)
  password                = models.CharField                 (max_length=30, blank=True, null=True)
  status                  = models.IntegerField              (default=15, choices=STATUSES)
  reversevideo            = models.BooleanField              (default=False)
  datecolor               = models.CharField                 (max_length=20, default='black')
  detailcolor             = models.CharField                 (max_length=20, default='#0000C0')
  attendeescolor          = models.CharField                 (max_length=20, default='#00C000')
  backgroundcolor         = models.CharField                 (max_length=20, default='#F3FFF3')
  datecolor_rev           = models.CharField                 (max_length=20, default='white')
  detailcolor_rev         = models.CharField                 (max_length=20, default='aqua')
  attendeescolor_rev      = models.CharField                 (max_length=20, default='lawngreen')
  backgroundcolor_rev     = models.CharField                 (max_length=20, default='black')
  cover                   = models.ImageField                (blank=True, null=True, upload_to='images/')
  notes                   = models.TextField                 (blank=True, null=True)
  last_login_date         = models.DateTimeField             (blank = True, null = True)
  last_logout_date        = models.DateTimeField             (blank = True, null = True)
  created_date            = models.DateTimeField             (default=timezone.now)
  class Meta:
        ordering = ['username']
  def create(self):
    self.created_date = timezone.now()
    self.save()
  def __str__(self):
    return str(self.display_name)
"""

class Message(models.Model):
    sender                = models.CharField          (max_length=20)
    recipient             = models.CharField          (max_length=20)
    sent_date             = models.DateTimeField      (blank=True, null=True, default=timezone.now)
    received_date         = models.DateTimeField      (blank=True, null=True)
    is_live_sender        = models.BooleanField       (default=True)
    is_live_recipient     = models.BooleanField       (default=True)
    content               = models.TextField          (blank=True, null=True)
    class Meta:
        ordering = ['sent_date']
    def sent(self):
        self.sent_date = timezone.now()
        self.save()
    def received (self):
        self.received_date  = timezone.now()
        self.save()
    def __str__(self):
        return str(self.sender)

class Medreading(models.Model):
    reading_date            = models.DateTimeField(default=timezone.now, blank=True, null=True)
    weight                  = models.DecimalField(max_digits=4,decimal_places=1,blank=True,null=True)
    notes                   = models.TextField(blank=True,null=True)
    glucose                 = models.DecimalField(max_digits=3,decimal_places=1,blank=True,null=True)
    HbA1c                   = models.DecimalField(max_digits=2,decimal_places=0,blank=True,null=True)
    blood_pressure_1        = models.DecimalField(max_digits=3,decimal_places=0,blank=True,null=True)
    blood_pressure_2        = models.DecimalField(max_digits=3,decimal_places=0,blank=True,null=True)
    HDL                     = models.DecimalField(max_digits=4,decimal_places=2,blank=True,null=True)
    LDL                     = models.DecimalField(max_digits=3,decimal_places=1,blank=True,null=True)
    created_date            = models.DateTimeField(default=timezone.now, blank=True, null=True)
    def __str__(self):
        return str(self.reading_date)

class Bookmark(models.Model):
    name                    = models.URLField                        ('Address of bookmark',                                       default='http://')
    category                = models.ForeignKey                      ('Category', related_name='cat',    on_delete=models.CASCADE, default=1)
    subcategory             = models.ForeignKey                      ('Category', related_name='subcat', on_delete=models.CASCADE, blank=True, null=True)
    notes                   = models.TextField                       (                                                             blank=True, null=True)
    created_date            = models.DateTimeField                   (                                                             default=timezone.now)
    def __str__(self):
        return str(self.name)

class Category(models.Model):
    name                    = models.CharField(max_length=20)
    notes                   = models.TextField(blank=True,null=True)
    created_date            = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.name)

class Identifier(models.Model):
    name                    = models.CharField(max_length=20)
    notes                   = models.TextField(blank=True,null=True)
    created_date            = models.DateTimeField(default=timezone.now, blank=True, null=True)
    def __str__(self):
        return str(self.name)

class Emailhost(models.Model):
    name                    = models.CharField(max_length=20)
    notes                   = models.TextField(blank=True,null=True)
    created_date            = models.DateTimeField(default=timezone.now, blank=True, null=True)
    def __str__(self):
        return str(self.name)

class Identifier2(models.Model):
    name                    = models.CharField(max_length=20)
    notes                   = models.TextField(blank=True,null=True)
    created_date            = models.DateTimeField(default=timezone.now, blank=True, null=True)
    def __str__(self):
        return str(self.name)

class Login(models.Model):
    bookmark                = models.ForeignKey('Bookmark', on_delete=models.CASCADE, default=1)
    identifier              = models.ForeignKey('Identifier', on_delete=models.CASCADE, default=1)
    emailhost               = models.ForeignKey('Emailhost', on_delete=models.CASCADE, blank=True, null=True)
    identifier2             = models.ForeignKey('Identifier2', on_delete=models.CASCADE, default=1)
    notes                   = models.TextField(blank=True,null=True)
    created_date            = models.DateTimeField(default=timezone.now, blank=True, null=True)
    def __str__(self):
        return str(self.name)

class Colour(models.Model):
    name                    = models.CharField(max_length=20)
    notes                   = models.TextField(blank=True,null=True)
    specification           = models.CharField(max_length=20, default='#000000')
    lightness               = models.IntegerField(default=0)
    created_date            = models.DateTimeField(default=timezone.now, blank=True, null=True)
    def __str__(self):
        return str(self.name)

class Colourscheme(models.Model):
    name                    = models.CharField(max_length=20)
    notes                   = models.TextField(blank=True,null=True)
    backgroundcolour        = models.CharField(max_length=20, default='#000000')
    datecolour              = models.CharField(max_length=20, default='#000000')
    detailcolour            = models.CharField(max_length=20, default='#000000')
    def __str__(self):
        return str(self.name)
