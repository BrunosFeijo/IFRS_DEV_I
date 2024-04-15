from django.contrib import admin
from exemplo.models import Example
from exemplo.models import Person
from exemplo.models import Passport

# Register your models here.
admin.site.register(Example)
admin.site.register(Person)
admin.site.register(Passport)