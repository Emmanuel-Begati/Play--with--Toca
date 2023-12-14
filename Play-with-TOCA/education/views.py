from django.shortcuts import render

# Create your views here.
def innovate(request):
    return render(request, 'education/innovate.html')

def science_one(request):
    return render(request, 'education/science/science.html')

def science_two(request):
    return render(request, 'education/science/science2.html')

def space_one(request):
    return render(request, 'education/space/space.html')

def space_two(request):
    return render(request, 'education/space/space2.html')

def space_three(request):
    return render(request, 'education/space/space3.html')