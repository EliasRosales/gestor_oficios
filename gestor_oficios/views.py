# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from oficios.forms import TradesForm, SenderForm, DepartmentsForm

# Create your views here.


def nuevo_oficio(request):
    context = dict()
    unit_form = TradesForm(request.POST or None)
    if request.method == 'POST':
        if unit_form.is_valid():
            unit_form.save()
            return redirect('nuevo_oficio')
        else:
            context['errors'] = unit_form.errors
    context['edit'] = False
    context['form'] = unit_form
    context['operation'] = 'nuevo oficio'
    return render(request, 'index.html', context=context)



