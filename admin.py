from django.contrib import admin

# Register your models here.
from .models import Post


class BlogModelAdmin(admin.ModelAdmin):
	list_display = ["title","created_date","upadted_date"]
	list_display_linkls = ["created_date,updated_date"]
	list_editable = ["title","body"]
	list_filter = ["updated_date","created_date"]

	search_field = ["title", "body"]
	class Meta:
		model = Post




admin.site.register(Post, BlogModelAdmin)