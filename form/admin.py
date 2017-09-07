from django.contrib import admin

# Register your models here.
from .models import Programming_Competition,NOSKode

class Programming_CompetitionAdmin(admin.ModelAdmin):
    list_display=("id","full_name", "email","phone_no","programming_language")
    
class NOSKodeAdmin(admin.ModelAdmin):
    list_display=("id","team_name","team_leader","email","phone_number","total_team_members","project_title","project_description")


admin.site.register(Programming_Competition, Programming_CompetitionAdmin)
admin.site.register(NOSKode, NOSKodeAdmin)
