import datetime
#from django.contrib.auth.models            import User
from django.db                              import models
from django.utils                           import timezone
from django.conf                            import settings
from django.contrib.auth                    import get_user_model
from django.urls                            import reverse

class Site(models.Model):
  COLOURS = (
        ('white','white'),
        ('black','black'),
        ('red','red'),
        ('lime','lime'),
        ('blue','blue'),
        ('yellow','yellow'),
        ('aqua','aqua'),
        ('fuchsia','fuchsia'),
        ('green','green'),
        ('teal','teal'),
        ('purple','purple'),
        ('navy','navy'),
        ('orange','orange'),
        ('silver','silver'),
  )
  note                         = models.TextField              (blank=True, null=True)
  backgroundcolour             = models.CharField              ('Background Colour', max_length=20, choices=COLOURS)
  datecolour                   = models.CharField              ('Date Colour', max_length=20, choices=COLOURS)
  detailcolour                 = models.CharField              ('Detail Colour', max_length=20, choices=COLOURS)


class Photo(models.Model):
  notes                   = models.TextField          (blank=True, null=True)
  priority                = models.IntegerField       (default=100)
  is_live                 = models.BooleanField       (default=True)
  title                   = models.TextField          (blank=True, null=True)
  cover                   = models.ImageField         (upload_to='images/')
  created_date            = models.DateTimeField      (blank=True, null=True, default=timezone.now)
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

class Event_Old(models.Model):
  event_date        = models.DateField                              (default=timezone.now)
  detail            = models.CharField                              ('Details of event',max_length=200, blank=True,null=True)
  addendum          = models.TextField                              ('Addendum', blank=True,null=True)
  created_date      = models.DateTimeField                          (default=timezone.now,blank=True, null=True)
  is_live           = models.BooleanField                           (default=True, blank=True, null=True)
  status_now        = models.CharField                              (max_length=20,blank=True,null=True)
  sameday           = models.BooleanField                           (default=False)
  def __str__(self):
    return self.event_date

"""
class E(models.Model):
  author                  = models.ForeignKey('auth.User', related_name="authorzz", on_delete=models.CASCADE)
  e_date                  = models.DateField('Date of the event, in the format "yyyy-mm-dd", e.g. for 31st December 2015, enter "2015-12-31"', default=timezone.now, blank=True,null=True)
  detail_public           = models.CharField('Title of event, this be shown publicly', max_length= 200, blank=True, null=True, default='')
  detail_private          = models.TextField('Details of event', blank=True,null=True)
  notes                   = models.TextField(blank=True,null=True)
  #attendees               = models.ManyToManyField(Person, related_name="bookedin", blank=True)
  #hosts                   = models.ManyToManyField(Person, related_name="hh", blank=True)
  created_date            = models.DateTimeField(default=timezone.now, blank=True, null=True)
  is_live                 = models.BooleanField(default=True, blank=True, null=True)
  def __str__(self):
    return self.detail_public
    """


class N(models.Model):
  author                  = models.ForeignKey('auth.User', related_name="authorn", on_delete=models.CASCADE)
  notice                   = models.TextField('Notice', blank=True, null=True, default='')
  created_date            = models.DateTimeField(default=timezone.now)







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
    name                    = models.URLField                        ('Address of bookmark',                                       )
    priority                = models.IntegerField                    (default=100)
    category1               = models.ForeignKey                      ('Category', related_name='cat1',   on_delete=models.CASCADE, blank=True, null=True)
    category2               = models.ForeignKey                      ('Category', related_name='cat2',   on_delete=models.CASCADE, blank=True, null=True)
    category3               = models.ForeignKey                      ('Category', related_name='cat3',   on_delete=models.CASCADE, blank=True, null=True)
    notes                   = models.TextField                       (                                                             blank=True, null=True)
    last_accessed_date      = models.DateTimeField                   (blank=True, null=True,                                      default=timezone.now)
    created_date            = models.DateTimeField                   (blank=True, null=True,                                   default=timezone.now)
    def __str__(self):
        return str(self.name)

class Memo(models.Model):
    priority                = models.IntegerField                    (default=100)
    category1               = models.ForeignKey                      ('Category', related_name='mem1',   on_delete=models.CASCADE, blank=True, null=True)
    category2               = models.ForeignKey                      ('Category', related_name='mem2',   on_delete=models.CASCADE, blank=True, null=True)
    category3               = models.ForeignKey                      ('Category', related_name='mem3',   on_delete=models.CASCADE, blank=True, null=True)
    content                 = models.TextField                       (                                                             blank=True, null=True)
    last_accessed_date      = models.DateTimeField                   ( blank=True, null=True,                                   default=timezone.now)
    created_date            = models.DateTimeField                   (blank=True, null=True,                                    default=timezone.now)
    def __str__(self):
        return str(self.content[:50])

class Category(models.Model):
    name                    = models.CharField(max_length=20)
    priority                = models.IntegerField       (default=100)
    notes                   = models.TextField                       (                                                             blank=True, null=True)
    def __str__(self):
        return str(self.name)

class Identifier(models.Model):
    name                    = models.CharField(max_length=20)
    priority                = models.IntegerField       (default=100)
    notes                   = models.TextField                       (                                                             blank=True, null=True)
    def __str__(self):
        return str(self.name)

class Emailhost(models.Model):
    name                    = models.CharField(max_length=20)
    priority                = models.IntegerField       (default=100)
    notes                   = models.TextField                       (                                                             blank=True, null=True)
    def __str__(self):
        return str(self.name)

class Identifier2(models.Model):
    name                    = models.CharField(max_length=20)
    priority                = models.IntegerField       (default=100)
    notes                   = models.TextField                       (                                                             blank=True, null=True)
    def __str__(self):
        return str(self.name)

class Login(models.Model):
    bookmark                = models.ForeignKey('Bookmark', on_delete=models.CASCADE, default=1)
    priority                = models.IntegerField       (default=100)
    identifier              = models.ForeignKey('Identifier', on_delete=models.CASCADE, default=1)
    emailhost               = models.ForeignKey('Emailhost', on_delete=models.CASCADE, blank=True, null=True)
    identifier2             = models.ForeignKey('Identifier2', on_delete=models.CASCADE, default=1)
    notes                   = models.TextField                       (                                                             blank=True, null=True)
    def __str__(self):
        return str(self.bookmark)

