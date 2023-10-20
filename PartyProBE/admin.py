from django.contrib import admin
from .models import FoodItem, GuestRSVP, Catering, Event, User


# class UsersAdmin(admin.ModelAdmin):
#     list_display = ('user_id', 'passwords', 'rsvp_id')
#     list_filter = ('user_id', 'rsvp_id')
#     search_fields = ('user_id', 'rsvp_id')
#     ordering = ['user_id']


class GuestRSVPAdmin(admin.ModelAdmin):
    list_display = ('rsvp_id', 'event_id', 'email', 'first_name', 'last_name', 'food_choice')
    list_filter = ('event_id', 'food_choice')
    search_fields = ('event_id', 'first_name', 'last_name')
    ordering = ['event_id']


class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('food', 'dessert')
    list_filter = ('food', 'dessert')
    search_fields = ('food', 'dessert')


class CateringAdmin(admin.ModelAdmin):
    list_display = ('event', 'date', 'number_of_guest', 'other', 'rsvp_id')
    list_filter = ('event', 'date', 'number_of_guest', 'other')
    search_fields = ('event', 'date', 'number_of_guest', 'other')

# class EventAdmin(admin.ModelAdmin):
#     list_display = ('event_id', 'user_id', 'rsvp_id')
#     list_filter = ('user_id', 'rsvp_id')
#     search_fields = ('user_id__user_id', 'rsvp_id__rsvp_id', 'user_id')


# class StockList(admin.ModelAdmin):
#     list_display = ('customer', 'symbol', 'name', 'shares', 'purchase_price')
#     list_filter = ('customer', 'symbol', 'name')
#     search_fields = ('customer', 'symbol', 'name')
#     ordering = ['customer']


# admin.site.register(Users, UsersAdmin)
admin.site.register(GuestRSVP, GuestRSVPAdmin)
admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(Catering, CateringAdmin)
# admin.site.register(Event, EventAdmin)
# admin.site.register(Testimonials, StockList)
# admin.site.register(Event, UsersAdmin)
