from django.contrib import admin

# Register your models here.
from .models import Speaker, Speech, SpeechInstance

# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(BookInstance)


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    # fields = ['first_name', 'last_name']
    

# class SpeechesInstanceInline(admin.TabularInline): 
#     model = SpeechInstance
#     fields = ['speech', 'id']
#     list_display = ('title','id') 
#     extra = 0
    


@admin.register(Speech)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('title', 'speaker')
    # inlines = [SpeechesInstanceInline]



   

