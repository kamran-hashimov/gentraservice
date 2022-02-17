from django.contrib import admin
from .models import Post

# Register your models here.


class Posts(admin.ModelAdmin):

    list_display=('title','created_date','published_date')
    list_display_links=('title','created_date','published_date')
    list_filter= ['created_date']
    search_fields = ['published_date']

    class Meta:
        model = Post

admin.site.register(Post,Posts)
