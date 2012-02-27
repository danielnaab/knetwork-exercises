from django.contrib import admin

from exercises.models import KhanExerciseTreeNode

class KhanExerciseTreeNodeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in KhanExerciseTreeNode._meta.fields]

admin.site.register(KhanExerciseTreeNode, KhanExerciseTreeNodeAdmin)
