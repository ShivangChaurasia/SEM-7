from django.shortcuts import render
from .feedback_form import FeedbackForm


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            teacher_name = form.cleaned_data['teacher_name']
            subject = form.cleaned_data['subject']
            feedback = form.cleaned_data['feedback']
            rating = form.cleaned_data['rating']

            print(f"Name: {name}")
            print(f"Teacher Name: {teacher_name}")
            print(f"Subject: {subject}")
            print(f"Feedback: {feedback}")
            print(f"Rating: {rating}")

            return render(request, 'success.html', {'name': name})
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})
