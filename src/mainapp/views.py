from django.forms import modelformset_factory
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator

from mainapp.forms import AddNews, AddImage
from mainapp.models import News, Image


def index(request):
	news = News.objects.all()
	nums = request.COOKIES.get('items_on_page')

	if not nums:
		nums = 10

	paginator = Paginator(news, nums)

	page_number = request.GET.get('page')
	page = paginator.get_page(page_number)

	return render(request, 'base.html', {'page': page})


def add(request):
	if not request.user.is_authenticated:
		raise Http404

	if request.method == 'GET':
		form = AddNews()
		img = AddImage()
		return render(request, 'news_create.html', context={'form': form, 'img': img})

	ImageFormSet = modelformset_factory(Image, form=AddImage, extra=4)

	if request.method == 'POST':
		files = request.FILES.getlist('img')

		postForm = AddNews(request.POST)
		formset = ImageFormSet(request.POST)

		if postForm.is_valid():
			post_form = postForm.save()
			post_form.save()
			for f in files:
				Image.objects.create(news=post_form, img=f)
			return HttpResponseRedirect("/")
	else:
		postForm = AddNews()
		formset = ImageFormSet()
	return render(request, 'base.html', {'field': postForm, 'formset': formset})
