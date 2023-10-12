from django.db import models

from users.models import User

# Create your models here.


NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название', unique=True)
    preview = models.ImageField(upload_to='catalog/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='название', unique=True)
    preview = models.ImageField(upload_to='catalog/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    video_url = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Payments(models.Model):
    PAY_WAY = (
        ('cash', 'наличными'),
        ('bank_transfer', 'перевод на счет'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    date = models.DateField(verbose_name='дата оплаты')

    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='курс')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='урок')

    summ_of_fee = models.IntegerField(verbose_name='цена')
    way_of_pay = models.CharField(max_length=16, verbose_name='способ оплаты', choices=PAY_WAY)


class Subscribe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'course'],
                                    name='unique_subscribe',
                                    ),
        ]
