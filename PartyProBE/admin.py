from django.contrib import admin
from .models import Users, GuestRSVP, Testimonials, Admin, Event


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


# class StockList(admin.ModelAdmin):
#     list_display = ('customer', 'symbol', 'name', 'shares', 'purchase_price')
#     list_filter = ('customer', 'symbol', 'name')
#     search_fields = ('customer', 'symbol', 'name')
#     ordering = ['customer']


# admin.site.register(Users, UsersAdmin)
admin.site.register(GuestRSVP, GuestRSVPAdmin)
# admin.site.register(Testimonials, StockList)
# admin.site.register(Event, UsersAdmin)
