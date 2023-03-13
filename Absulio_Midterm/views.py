from django.shortcuts import render

def Midterm_A(request):
    jobroles = [
        'reporting executive',
        'business analyst',
        'data analyst',
        'statistician',
        'data scientist',
        'data engineer/data architect',
        'machine learning engineer',
        'big data engineer',
    ]
    context = {
        'jobroles': jobroles,
    }
    return render(request, 'midterma.html', context)
