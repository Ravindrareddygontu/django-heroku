from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['Created_by', 'Title', 'Opinion']

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.Created_by:
            instance.Created_by = user
        instance.modified_by = user
        instance.save()
        form.save_m2m()
        return instance