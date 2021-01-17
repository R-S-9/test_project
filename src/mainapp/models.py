from django.db import models
from django.utils import timezone


class News(models.Model):
	"""Новость."""

	title = models.CharField(max_length=150, verbose_name='Заголовок')
	date = models.DateTimeField(verbose_name='Дата', default=timezone.now)
	content = models.TextField(verbose_name='Новость')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'
		ordering = ('-date',)


class Image(models.Model):
	"""Картинка."""

	img = models.ImageField(verbose_name='Изображение')
	news = models.ForeignKey(News, verbose_name='Новость', on_delete=models.CASCADE)
	order = models.IntegerField(verbose_name='Порядковый номер')

	def save(self, *args, **kwargs):
		last_order = self.__class__.objects.filter(
			news=self.news
		).order_by('order').values_list(
			'order', flat=True
		).last()

		if last_order:
			self.order = last_order + 1
		else:
			self.order = 1

		super(Image, self).save(*args, **kwargs)

	def __str__(self):
		return f'{self.news.title}: рис. {self.order}'

	class Meta:
		verbose_name = 'Картинка'
		verbose_name_plural = 'Картинки'
		unique_together = ('news', 'order')
		ordering = ('order',)
