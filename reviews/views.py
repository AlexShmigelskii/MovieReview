from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .models import Review
from .forms import ReviewForm
from .predict import predict_review_sentiment


def index(request):
    context = {
            'poject_name': 'Классификация отзывов'
    }

    return render(request, 'index.html', context)


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']
            sentiment, rating = predict_review_sentiment(text)
            review = Review(text=text, sentiment=sentiment, rating=rating)
            review.save()

            return render(request, 'review_result.html', {'sentiment': sentiment, 'rating': rating})

    else:
        form = ReviewForm()

    return render(request, 'add_review.html', {'form': form})
