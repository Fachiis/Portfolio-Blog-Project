from django.urls import path

from .views import BlogListView, BlogDetailView, SearchResultsView

urlpatterns = [
    path('', BlogListView.as_view(), name='allblogs'),
    path('<uuid:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]
