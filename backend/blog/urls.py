from django.urls import path
from .views import BlogPostListView, BlogPostDetailedView, BlogPostFeaturedView, BlogPostCategoryView


urlpatterns = [
    path('', BlogPostListView.as_view()),
    path('featured', BlogPostFeaturedView.as_view()),
    path('category', BlogPostCategoryView.as_view()),
    path('<slug>', BlogPostDetailedView.as_view()),    
]

# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))] #to handle url routing for our React side