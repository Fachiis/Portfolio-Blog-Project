from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = "allblogs.html"
    context_object_name = 'bloglist'


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blogdetail.html"


class SearchResultsView(ListView):
    model = Blog
    context_object_name = 'bloglist'
    template_name = "search_result.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Blog.objects.filter(
            Q(title__icontains=query) #| Q(body__icontains=query)
        )


#def allblogs(request):
    #blogs = Blog.objects.all
    #return render(request, 'allblogs.html', {'blogs':blogs})

#def blogdetailview(request):

    #return render(request, 'blogdetail.html', )
