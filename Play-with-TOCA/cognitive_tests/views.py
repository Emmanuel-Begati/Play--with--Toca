from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def cognitive(request):
    if not request.user.is_authenticated:
            messages.warning(request, 'You need to log in to take the test.')

            return render(request, 'cognitive_tests/cognitive.html')
    else:
         return render(request, 'cognitive_tests/cognitive.html')

@login_required
def questions(request):
    return render(request, 'cognitive_tests/questions.html')

@login_required
def visual(request):
    return render(request, 'cognitive_tests/visual.html')