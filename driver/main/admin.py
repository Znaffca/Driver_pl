from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe
from main.models import Profile, CategoryTag, Advice, TestTraining, TrainingQuestion, ForumPost, AnswerPost, \
    AdviceQuestion

admin.site.site_header = "PL Driver - panel administracyjny aplikacji"
admin.site.site_title = "Driver - aplikacja"
admin.site.index_title = "Strona główna"
admin.site.unregister(Group)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ['photo_image']
    list_display = ['user', 'date_of_birth', 'description', 'total_points', 'photo', 'photo_image', 'date_added']
    list_filter = ('user', 'total_points', 'date_added')
    fieldsets = (
        ('Użytkownik', {'fields': ('user', 'date_of_birth')}),
        ('Opis', {'fields': ('description', 'total_points')}),
        ('Zdjęcie', {'fields': ('photo', 'photo_image')}),
    )

    def photo_image(self, obj):
        if obj.photo and hasattr(obj.photo, 'url'):
            return mark_safe("<img src='{url}' width='auto' height='50' />".format(
                url=obj.photo.url,)
            )


@admin.register(CategoryTag)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    fieldsets = ('Kategoria', {'fields': ('name',)}),


@admin.register(Advice)
class AdviceAdmin(admin.ModelAdmin):
    readonly_fields = ['slug', 'img_show', 'date_added']
    list_display = ['title', 'slug', 'lead', 'img', 'img_show', 'video', 'tag', 'count', 'date_added']
    list_filter = ['tag', 'date_added']
    fieldsets = (
        ('Szczegóły porady', {'fields': ('title', 'lead', 'tag')}),
        ('Media do porady', {'fields': ('img', 'video')}),
    )

    def img_show(self, obj):
        if obj.img and hasattr(obj.img, 'url'):
            return mark_safe("<img src='{url}' width='auto' height='50' />".format(
                url=obj.photo.url,)
            )


@admin.register(AdviceQuestion)
class AdviceQuestionAdmin(admin.ModelAdmin):
    list_display = ['user', 'advice', 'question']
    list_filter = ['user', 'advice']
    fieldsets = (
        ("Użytkownik", {'fields': ('user',)}),
        ("Pytanie", {'fields': ('advice', 'question')})
    )


@admin.register(TestTraining)
class TestTrainingAdmin(admin.ModelAdmin):
    list_display = ['user', 'test_name', 'advice', 'result']
    list_filter = ['user',]
    fieldsets = (
        ('Trening', {'fields': ('user', 'advice', 'result')}),
    )


@admin.register(TrainingQuestion)
class TrainingQuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'training', 'correct_answer', 'answer_a', 'answer_b', 'answer_c', 'answer_d',
                    'file_a', 'file_b', 'file_c', 'file_d']
    list_filter = ['training']
    fieldsets = (
        ('Zadanie', {'fields': ('question', 'training', 'correct_answer')}),
        ('Odpowiedź 1', {'fields': ('answer_a', 'file_a')}),
        ('Odpowiedź 2', {'fields': ('answer_b', 'file_b')}),
        ('Odpowiedź 3', {'fields': ('answer_c', 'file_c')}),
        ('Odpowiedź 4', {'fields': ('answer_d', 'file_d')}),
    )


@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    readonly_fields = ['slug', 'date']
    list_display = ['category', 'user', 'title', 'slug', 'description', 'date']
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
