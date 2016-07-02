#from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Course, Step


def course_list(request):
	"""Comprehension used to display list of courses"""
	courses = Course.objects.all()
	#output = ', '.join([str(course) for course in courses])
	#return HttpResponse(output)
	return render(request, 'courses/course_list.html', {'courses': courses})

# Create your views here.
def course_detail(request, pk):
    #course = Course.objects.get(pk=pk)   below accounting for 404 too
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})

def step_detail(request, course_pk, step_pk):
	#course_id is foreign key
    step = get_object_or_404(Step, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})