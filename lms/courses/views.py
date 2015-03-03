from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from courses.models import Course, CourseForm



class IndexView(generic.ListView):
    template_name = 'courses/index.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        return Course.objects.order_by('id')[:10]

class ChangeView(generic.UpdateView):
    model = Course
    template_name = 'courses/course_edit.html'

class AddView(generic.CreateView):
    model = Course
    template_name = 'courses/course_edit.html'

class DetailsView(generic.DetailView):
    model = Course
    template_name = 'courses/course_details.html'

def save(request, course_id=None):
    try:
        existing_course = Course.objects.get(pk=course_id)
    except:
        existing_course = None

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance = existing_course)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:index'))