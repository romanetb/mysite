from django.shortcuts import render

# Create your views here.
# from altapp.forms import NewUserForm


def home(request):
    return render(request, 'home.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def blog_post(request):
    return render(request, 'blog_post.html', {})


def blog_home_1(request):
    return render(request, 'blog_home_1.html', {})


def blog_home_2(request):
    return render(request, 'blog_home_2.html', {})


def about(request):
    return render(request, 'about.html', {})


def services(request):
    return render(request, 'services.html', {})


def portfolio_item(request):
    return render(request, 'portfolio_item.html', {})


def portfolio_1_col(request):
    return render(request, 'portfolio_1_col.html', {})


def portfolio_2_col(request):
    return render(request, 'portfolio_2_col.html', {})


def portfolio_3_col(request):
    return render(request, 'portfolio_3_col.html', {})


def portfolio_4_col(request):
    return render(request, 'portfolio_4_col.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})


def faq(request):
    return render(request, 'faq.html', {})
