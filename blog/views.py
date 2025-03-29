from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView, DetailView
from .forms import CommentForm
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'main/blog.html'
    context_object_name ='posts'
    ordering = ['-date_posted']
    paginate_by = 4



class PostDetailView(DetailView):
    model = Post
    template_name = 'main/blog_detail.html'
    context_object_name = 'post'
    form_class = CommentForm # Formnai qoshish

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all()  #Blogga tegishli commentlarni ochish 
        return context
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated: #agar user login qilmagan bolsa
            return redirect('login')    #login qilshga jonatadi


        self.object = self.get_object() # hozirgi postni olish
        form = CommentForm(request.POST)


        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = self.object # commentga postni bog'lash
            comment.user = request.user # commentga foydalanuvchini bog'lash
            comment.save()
            return redirect('blog-detail', pk=self.object.pk) #postga qaytish
        
        return self.render_to_response(self.get_context_data(form=form))
        
        