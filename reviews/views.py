from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
from .predict import predict_review_sentiment


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']
            rating, sentiment = predict_review_sentiment(text)
            review = Review(text=text, sentiment=sentiment, rating=rating)
            review.save()
            return redirect('reviews:add_review')

        else:
            form = ReviewForm()
        return render(request, 'add_review.html', {'form': form})
