from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    password = models.IntegerField()
    catering_id = models.OneToOneField('Catering', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.user_id)


class GuestRSVP(models.Model):
    rsvp_id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey('Event', on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    food_choice = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        unique_together = ('event_id', 'email')


class Catering(models.Model):
    event = models.CharField(max_length=50)
    date = models.DateField()
    number_of_guest = models.CharField(max_length=50)
    other = models.CharField(max_length=10)
    rsvp_id = models.ForeignKey(GuestRSVP, on_delete=models.SET_NULL, null=True, blank=True)
    user_id = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, blank=True)
    catering_id = models.AutoField(primary_key=True)
    # event_id = models.ForeignKey('Event', on_delete=models.SET_NULL, null=True, blank=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.pk)


class FoodItem(models.Model):
    catering = models.ForeignKey(Catering, on_delete=models.CASCADE, related_name='food_items', blank=True, null=True)
    food = models.CharField(max_length=200)
    dessert = models.CharField(max_length=50)

    def __str__(self):
        return self.food


class Testimonials(models.Model):
    names = models.CharField(max_length=50)
    ratings = models.CharField(max_length=50)
    reviews = models.CharField(max_length=50)
    user_id = models.ForeignKey('Users', on_delete=models.SET_NULL, null=True, blank=True)
    rsvp_id = models.ForeignKey('GuestRSVP', on_delete=models.SET_NULL, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    testimonials_id = models.AutoField(primary_key=True)

    def created(self):
        self.acquired_date = timezone.now()
        self.save()

    def updated(self):
        self.recent_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.pk)


class Admin(models.Model):
    admin_id = models.CharField(max_length=30, primary_key=True)
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
    rsvp_id = models.ForeignKey('GuestRSVP', on_delete=models.CASCADE)
    testimonials_id = models.ForeignKey('Testimonials', on_delete=models.CASCADE)

    def __str__(self):
        return self.pk


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE, null=True)
    rsvp_id = models.ForeignKey('GuestRSVP', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Event ID: {self.event_id}, User ID: {self.user_id_id}'
