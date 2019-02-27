from django.contrib import admin
from django.utils.safestring import mark_safe
from main.models import Profile, Category, Advice, TestTraing, TrainingQuestion, ForumPost, AnswerPost


admin.site.site_header = "PL Driver - panel administracyjny aplikacji"
admin.site.site_title = "Driver - aplikacja"
admin.site.index_title = "Strona główna"


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ['photo_image']
    list_display = ['user', 'date_of_birth', 'description', 'total_points', 'photo', 'photo_image', 'date_added']
    list_filter = ('user', 'total_points', 'date_added')
    fieldsets = (
        ('Użytkownik', {'fields': ('user', 'date_of_birth')}),
        ('Opis', {'fields': ('description', 'total_points')}),
        ('Zdjęcie', {'fields': ('photo',)})
    )

    def photo_image(self, obj):
        return mark_safe("<img src='{url}' width='auto' height='50px' >".format(
            url=obj.photo.url,))


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    fieldsets = ('Kategoria', {'fields': ('name',)}),


@admin.register(Advice)
class AdviceAdmin(admin.ModelAdmin):
    list_display = ['tag', 'title', 'description', 'img', 'video', 'date_added']
    list_filter = ['tag', 'date_added']
    fieldsets = (
        ('Szczegóły porady', {'fields': ('tag', 'title', 'description')}),
        ('Media do porady', {'fields': ('img', 'video')}),
    )


@admin.register(TestTraing)
class TestTrainingAdmin(admin.ModelAdmin):
    list_display = ['name', 'advice', 'result']
    list_filter = ['advice']
    fieldsets = (
        ('Trening', {'fields': ('name', 'advice', 'result')}),
    )


@admin.register(TrainingQuestion)
class TrainingQuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'training', 'correct_answer', 'answer_a', 'answer_b', 'answer_c', 'answer_d',
                    'file_a', 'file_b', 'file_c', 'file_d']
    list_filter = 'training',
    fieldsets = (
        ('Zadanie', {'fields': ('question', 'training', 'correct_answer')}),
        ('Odpowiedź 1', {'fields': ('answer_a', 'file_a')}),
        ('Odpowiedź 2', {'fields': ('answer_b', 'file_b')}),
        ('Odpowiedź 3', {'fields': ('answer_c', 'file_c')}),
        ('Odpowiedź 4', {'fields': ('answer_d', 'file_d')}),
    )


@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ['category', 'user', 'title', 'description', 'date']
    list_filter = ['category', 'user', 'date']
    fieldsets = (
        ('Kategoria', {'fields': ('category',)}),
        ('Temat', {'fields': ('user', 'title', 'description')}),
    )


@admin.register(AnswerPost)
class AnswerPostAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'answer', 'date_added']
    list_filter = ['post', 'user', 'date_added']
    fieldsets = (
        ('Temat', {'fields': ('post',)}),
        ('Odpowiedź', {'fields': ('user', 'answer')}),
    )
