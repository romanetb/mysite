
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('blog_post.html', views.blog_post, name='blog_post'),
    path('blog_home_1.html', views.blog_home_1, name='blog_home_1'),
    path('blog_home_2.html', views.blog_home_2, name='blog_home_2'),
    path('about.html', views.about, name='about'),
    path('services.html', views.services, name='services'),
    path('portfolio_item.html', views.portfolio_item, name='portfolio_item'),
    path('portfolio_1_col.html', views.portfolio_1_col, name='portfolio_1_col'),
    path('portfolio_2_col.html', views.portfolio_2_col, name='portfolio_2_col'),
    path('portfolio_3_col.html', views.portfolio_3_col, name='portfolio_3_col'),
    path('portfolio_4_col.html', views.portfolio_4_col, name='portfolio_4_col'),
    path('pricing.html', views.pricing, name='pricing'),
    path('faq.html', views.faq, name='faq'),
    # path('admin', admin.site.urls),

]
