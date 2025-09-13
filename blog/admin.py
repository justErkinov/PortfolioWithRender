from django.contrib import admin

from .models import Contact

from  .models import Experience,Education

admin.site.register(Contact)


admin.site.register(Experience)


# Register your models here.

@admin.register(Education)

class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'start_year', 'end_year')

    search_fields = ('institution', 'degree')
