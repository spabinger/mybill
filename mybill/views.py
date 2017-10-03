from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
from .models import Choice, Question, Bill


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)



class IndexView(generic.ListView):
   template_name = "mybill/index.html"
   context_object_name = "latest_bills_list"

   def get_queryset(self):
       return Bill.objects.all()
       #return Bill.objects.filter(
       #    pub_date__lte=timezone.now()
       #    ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    template_name = "mybill/detail.html"
    model = Question

    def get_queryset(self):
       """
       Excludes any questions that aren't published yet.
       """
       return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
   model = Question
   template_name = "mybill/results.html"

   def vote(request, question_id):
       p = get_object_or_404(Question, pk=question_id)
       try:
           selected_choice = p.choice_set.get(pk=request.POST['choice'])
       except (KeyError, Choice.DoesNotExist):
           return render(request, 'mybill/detail.html', {
               'question': p,
               'error_message': "You didn't select a choice",
           })
       else:
           selected_choice.votes += 1
           selected_choice.save()
           return HttpResponseRedirect(reverse('mybill:results', args=(p.id,)))


def vote(request, question_id):
    print "muh"
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))