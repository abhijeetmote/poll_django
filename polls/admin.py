from django.contrib import admin

# Register your models here.
from polls.models import Poll,Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class PollAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question']

#     fieldsets = [
#         (None,               {'fields': ['question']}),
#         ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
#     ]
    list_display = ('question', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question']
#admin.site.register(Poll)
admin.site.register(Poll,PollAdmin)