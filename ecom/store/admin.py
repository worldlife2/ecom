from django.contrib import admin
from django.contrib.auth.models import User

from .models import Category, Customer, Product, Order, Profile


# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)

# Mix Profile info and user info
class ProfileInline(admin.StackedInline):
    model = Profile
# Extend the User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ['username', 'first_name', 'last_name', 'email']
    inlines = [ProfileInline]

# Unregister the old way
admin.site.unregister(User)

# Re-register the new way
admin.site.register(User, UserAdmin)
    