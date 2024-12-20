from django.contrib import admin
from .models import CustomUser, Learner, Course


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_joined', 'first_name', 'last_name')
    search_fields = ('email', 'first_name', 'last_name')

    # Override the save_model method to ensure a corresponding Learner is created
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        
        # If a new user is created, create a corresponding Learner
        if not change:  # If it's a new user
            Learner.objects.create(user=obj)

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Learner)
class LearnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_id', 'full_name', 'date_of_birth')
    search_fields = ('user__username', 'full_name', 'student_id')
    

# Register the Course model
admin.site.register(Course)
