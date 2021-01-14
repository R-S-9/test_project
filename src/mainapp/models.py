from django.db import models
from django.utils import timezone


class News(models.Model):
	"""Новость."""

	title = models.CharField(max_length=150, verbose_name='Заголовок')
	date = models.DateTimeField(verbose_name='Дата', default=timezone.now)
	content = models.TextField(verbose_name='Новость')

	def __str__(self):
		return self.title


class Image(models.Model):
	"""Картинка."""

	img = models.ImageField(verbose_name='Изображение')
	news = models.ForeignKey(News, verbose_name='Новость', on_delete=models.CASCADE)
	order = models.IntegerField(verbose_name='Порядковый номер')

	def __str__(self):
		return f'{self.news.title}: рис. {self.order}'
