from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import include, path

# Create your views here.
def mainpage(request):
    return render(request, 'mainpage.html', {})



from django import forms

class DesieseForm(forms.Form):
    sex = forms.ChoiceField(label='Sex')
    age = forms.IntegerField(label="Age", help_text="4-1056")
    duration = forms.IntegerField(label="Duration", help_text="15-66")
    mri = forms.ChoiceField(label="MRI")
    cortisol = forms.IntegerField(label="Cortisol", help_text="8-590")
    plasma = forms.IntegerField(label="Plasma", help_text="1-55")

    def post(self, request):
        return render(request, 'form.html', {})





import ctypes

#libname = "/Users/daryabaranovskaya/Django/pr2/polls/liblibrary3.dylib"
#libname = "/Users/daryabaranovskaya/C++ programming/Algorithms and Data structuresHW/untitled/libraryMax.dylib"
#libname = "/Users/daryabaranovskaya/C++ programming/Algorithms and Data structuresHW/untitled/libhello.dylib"
#libname = "/pr2/polls/libhello.so"
#libc = ctypes.CDLL(libname)
from ctypes import *
import os
dir = os.path.dirname(os.path.realpath(__file__)) + '/'
libc = ctypes.CDLL(dir + "libhello.so")
#alloc_func = libc.mainfunc
#alloc_func.restype = ctypes.POINTER(ctypes.c_char)

import numpy


from django.views import View
class DesieseView(View):
    def get(self, request):
        return render(request, 'mainpage.html', {})

    def post(self, request):
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        duration = float(request.POST.get('duration'))
        mri = request.POST.get('mri')
        cortisol = request.POST.get('cortisol')
        plasma = request.POST.get('plasma')
        # context = {
        #     'sex' : sex,
        #     'age' : age,
        #     'duration' : duration,
        #     'mri': mri,
        #     'cortisol' : cortisol,
        #     'plasma' : plasma
        #
        # }
        cort_m2 = ctypes.c_longdouble(cortisol)
        ach_m2 = ctypes.c_longdouble(plasma)
        age_ = ctypes.c_longdouble(age)
        duration_ = ctypes.c_longdouble(duration)
        sex_ = ctypes.c_float(float(sex))
        mri_ = ctypes.c_float(float(mri))
        answ = libc.mainfunc(cort_m2, ach_m2, age_, duration_, sex_, mri_)
        #answ = libc.mainfunc(cort_m2, ach_m2, age_, duration_, sex_, mri_)
        #resstring = alloc_func(cort_m2, ach_m2, age_, duration_, sex_, mri_)
        #answ2 = ctypes.c_char_p.from_buffer(resstring)
        if answ == 0:
            text = "Remission within 3 years"
            percent = "93% [89%, 96%]"
        elif answ == 1:
            text = "Recurrence within 3 years"
            percent = "93% [89%, 96%]"
        cont = {
            'what_to_do' : '''alert('Hello! I am an alert box!!  %s '); ''',
            'answer': text,
            'percents': percent
        }
        #free_func = libc.mainfunc
        #free_func.argtypes = [ctypes.POINTER(ctypes.c_char), ]
        #free_func(answ)
        return render(request, 'mainpage.html', cont)


# from forms import DesieseForm
# def fill_form(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = DesieseForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = DesieseForm()
#
#     return render(request, 'mainpage.html', {'form': form})
