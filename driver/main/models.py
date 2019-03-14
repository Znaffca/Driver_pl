from django.conf import settings
from django.db import models
from django.utils.text import slugify

from main.utils import get_unique_slug

ANSWERS = (
    (1, "A"),
    (2, "B"),
    (3, "C"),
    (4, "D"),
)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Użytkownik")
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Data urodzenia")
    description = models.CharField(max_length=255, verbose_name="Opis")
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, null=True, verbose_name="Zdjęcie profilowe")
    total_points = models.IntegerField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name_plural = "Profile użytkowników"


class CategoryTag(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nazwa")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "Kategorie zagadnień"


class Advice(models.Model):
    title = models. CharField(max_length=255, verbose_name="Tytuł")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug")
    lead = models.TextField(verbose_name="Opis")
    img = models.ImageField(upload_to='images/advices', blank=True, null=True, verbose_name="Obraz")
    video = models.FileField(upload_to='videos/advices', blank=True, null=True, verbose_name="Wideo")
    tag = models.ForeignKey(CategoryTag, on_delete=models.CASCADE, related_name='category', verbose_name="Kategoria")
    count = models.IntegerField(verbose_name="Liczba poleceń")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Data dodania")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = "Porady motoryzacyjne"


class AdviceQuestion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Użytkownik")
    advice = models.ForeignKey(Advice, on_delete=models.CASCADE, verbose_name="Porada")
    question = models.TextField(verbose_name="Treść pytania")

    def __str(self):
        return f'{self.user} - {self.advice}: {self.question}'

    class Meta:
        verbose_name_plural = "Pytania do porad"


class TestTraining(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Użytkownik")
    test_name = models.CharField(max_length=128, unique=True, verbose_name="Nazwa")
    advice = models.ForeignKey(Advice, on_delete=models.CASCADE, verbose_name="Do której porady")
    result = models.IntegerField(verbose_name="Wynik")

    def _get_unique_test_name(self):
        test_name = slugify(self.advice.title)
        unique_test_name = f'{test_name}-test'
        num = 1
        while TestTraining.objects.filter(test_name=unique_test_name).exists():
            unique_test_name = f'{test_name}-test-{num}'
            num += 1
        return unique_test_name

    def save(self, *args, **kwargs):
        if not self.test_name:
            self.test_name = self._get_unique_test_name()
        super().save(self, *args, **kwargs)

    def __str__(self):
        return f'{self.result}'

    class Meta:
        verbose_name_plural = "Dostępne treningi"


class TrainingQuestion(models.Model):
    question = models.TextField(verbose_name="Treść pytania")
    training = models.ForeignKey(TestTraining, on_delete=models.CASCADE, verbose_name="Trening")
    correct_answer = models.IntegerField(choices=ANSWERS, verbose_name="Prawidłowa odpowiedź")
    answer_a = models.TextField(verbose_name="Odpowiedź A")
    file_a = models.FileField(upload_to='answer_files/', null=True, blank=True, verbose_name="Media A")
    answer_b = models.TextField(verbose_name="Odpowiedź B")
    file_b = models.FileField(upload_to='answer_files/', null=True, blank=True, verbose_name="Media B")
    answer_c = models.TextField(verbose_name="Odpowiedź C")
    file_c = models.FileField(upload_to='answer_files/', null=True, blank=True, verbose_name="Media C")
    answer_d = models.TextField(verbose_name="Odpowiedź D")
    file_d = models.FileField(upload_to='answer_files/', null=True, blank=True, verbose_name="Media D")

    def __str__(self):
        return f'{self.question}'

    class Meta:
        verbose_name_plural = "Pytania do treningu"


class ForumPost(models.Model):
    category = models.ForeignKey(CategoryTag, on_delete=models.CASCADE, related_name="category_tag")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_question')
    title = models.CharField(max_length=255, verbose_name="Tytuł")
    slug = models.SlugField(max_length=255, verbose_name="Slug")
    description = models.TextField(verbose_name="Slug")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Data dodania")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} - {self.user}'

    class Meta:
        verbose_name_plural = "Posty na forum"


class AnswerPost(models.Model):
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE, verbose_name="Post z forum")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_answer", verbose_name="Użytkownik")
    answer = models.TextField(verbose_name="Odpowiedź")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Data dodania")

    def __str__(self):
        return f'{self.user} - {self.answer}'

    class Meta:
        verbose_name_plural = "Odpowiedzi na posty"
