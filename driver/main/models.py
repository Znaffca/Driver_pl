from django.conf import settings
from django.db import models


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


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Kategoria")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "Kategorie zagadnień"


class Advice(models.Model):
    tag = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', verbose_name="Kategoria")
    title = models. CharField(max_length=255, verbose_name="Tytuł")
    description = models.TextField(verbose_name="Opis")
    img = models.ImageField(upload_to='images/advices', blank=True, null=True, verbose_name="Obraz")
    video = models.FileField(upload_to='videos/advices', blank=True, null=True, verbose_name="Wideo")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Data dodania")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = "Porady motoryzacyjne"


class TestTraing(models.Model):
    name = models.CharField(max_length=128, verbose_name="Nazwa")
    advice = models.ForeignKey(Advice, on_delete=models.CASCADE, verbose_name="Do której porady")
    result = models.IntegerField(verbose_name="Wynik")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "Dostępne treningi"


class TrainingQuestion(models.Model):
    question = models.TextField(verbose_name="Treść pytania")
    training = models.ForeignKey(TestTraing, on_delete=models.CASCADE, verbose_name="Trening")
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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_tag")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_question')
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

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
