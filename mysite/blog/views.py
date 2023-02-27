from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import BlogModel
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    
)
from .forms import BlogForm
# Create your views here.
def index(request):
    queryset = BlogModel.objects.all()[:5] #incomplete
    return render(request,'blog/index.html')

class BlogListView(ListView):
    queryset = BlogModel.objects.all()
    template_name = 'blog/blog_list.html'
    

class BlogDetailView(DetailView):
    template_name = 'blog/blog_detail.html'
    context_object_name= 'object'

    def get_object(self):
        id_= self.kwargs.get("id")
        return get_object_or_404(BlogModel, id=id_)

class BlogCreateView(CreateView):
    template_name = 'blog/blog_create.html'
    form_class = BlogForm
    queryset = BlogModel.objects.all()
    # success_url ='/' 
    # use success_url or define context_objectname
    
    def image(request):
        if request.method == "POST":
            form = BlogForm(data= request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                obj=form.instance
                return render(request,"blog:blog_create.html", {"obj":obj})
            else:
                form= BlogForm()
                img= BlogModel.objects.all()
            return render(request, "blog:blog_create.html",{"img":img, "form":form})

    # def get_success_url(self):
    #     return 'blogmodel-detail/'

    # def form_valid(self,form):
    #     print(form.cleaned_data)
    #     # form.send_email()
    #     return super().form_valid(form)

class BlogUpdateView(UpdateView):
    template_name = 'blog/blog_create.html'
    form_class = BlogForm
    success_url= '/'

    def get_object(self):
        id_= self.kwargs.get("id")
        return get_object_or_404(BlogModel, id=id_)

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)

class BlogDeleteView(DeleteView):
    template_name= 'blog/blog_delete.html'

    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(BlogModel, id=id_)

    def get_success_url(self):
        return reverse('blog:blog-list')





