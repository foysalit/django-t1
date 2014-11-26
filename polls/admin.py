from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 3
		

class PollAdmin(admin.ModelAdmin):
	"""docstring for PollAdmin"""
	fieldsets = [
		(None, {'fields': ['question']}),
		('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]

	inlines = [ChoiceInline]


# Register your models here.
admin.site.register(Choice)
admin.site.register(Poll, PollAdmin)
