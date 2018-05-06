# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render



# Create your views here.


from .models import Meal
from .forms import MealForm

def index(request):
	template = 'list.html'
	meals = Meal.objects.all()
	context = {
		'meals': meals,
	}

	return render(request, template, context)

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
def add_meal(request):
	template = "add_meal.html"

	if request.method == "POST":
		
		form = MealForm(request.POST)
	#print request.POST

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse_lazy('food:index'))

	else:
		context = {

			'meal_form': MealForm(),
		}
	return render(request, template, context)


def delete_meal(request, meal_id):
	meal = Meal.objects.get(id=int(meal_id))

	meal.delete()
	return HttpResponseRedirect(reverse_lazy('food:index'))



def update_meal(request, meal_id):
	template = "update_meal.html"
	meal = Meal.objects.get(id=int(meal_id))

	if request.method == "POST":
		form = MealForm(request.POST, instance=meal)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse_lazy('food:index'))


	else:
		context = {

			'meal_form': MealForm(instance=meal),

		}
	return render(request, template, context)




