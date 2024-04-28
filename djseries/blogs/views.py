from django.shortcuts import render


def home(request):
	template_name = "index.html"
	context = {}
	return render(request, template_name, context)


def post_list_view(request):
	template_name = "posts.html"
	context = {}
	return render(request, template_name, context)


def post_detail_view(request):
	template_name = "detail.html"
	context = {}
	return render(request, template_name, context)


def post_edit_view(request):
	template_name = "edit.html"
	context = {}
	return render(request, template_name, context)


def post_create_view(request):
	template_name = "create.html"
	context = {}
	return render(request, template_name, context)


def post_delete_view(request):
	template_name = "delete.html"
	context = {}
	return render(request, template_name, context)