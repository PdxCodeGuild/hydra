This guide covers the content in the folder **Forms and Links**.
## How to use a model and a database

Before continuing further, add a new URL in the my_app > urls.py folder:

```python
urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('posts/', views.blog_posts, name = 'posts'),
    path('add/', views.add_post, name = 'add_posts')
]
```

- Go to the my_app folder > views.py, import the model and add a new function based view:

```python
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog

def blog_posts(request):
    blogs = Blog.objects.all()  # gets all of the blog posts from the database and store them in a variable
  
    # creates the context dictionary to send the blog posts to the template
    context = {
       'blogs': blogs
    }
    return render(request, 'pages/posts.html', context)

def add_post(request):
    if request.method == 'GET': # if its a GET request, just display the add.html template
        return render(request, 'pages/add.html')
    elif request.method == 'POST': # if it's a POST request ..
        title = request.POST['title']   # get the title from the POST submission, this comes from a form
        text = request.POST['text']     # get the text from the POST submission, this comes from a form
        pub_date = request.POST['pub_date']
        # add the new blog post to the database. objects.create() automatically saves the new blog post for us.
        Blog.objects.create(title = title, text = text, pub_date = pub_date)
        return redirect('posts')
   
```

- In the Pages folder create a new page `posts.html` and add the following:

```html
{% extends 'base.html' %}
{% block content %}
<ul>
<a href="{% url 'add_posts' %}">add a blog post</a>
  {% for post in blogs %}
  <p>Title: {{ post.title }}</p>
  <p>ID: {{ post.id }}</p>
  <p>Description: {{ post.text }}</p>
  <p>Pub Date: {{post.pub_date}}</p>
  {% empty %}
  {% endfor %}
</ul>
{% endblock %}
```

## Add a form to create blog posts.

- In the Pages folder create a new page `add.html` and add the following:

```html
{% extends 'base.html' %}
{% block content %}
<form action="{% url 'add_posts' %}" method="POST">
    {% csrf_token %} title: <br />
    <input type="text" name="title" placeholder="enter blog post title" /><br /><br />
    <textarea name="text" id="" cols="30" rows="10"></textarea><br />
    <input type="date" id="start" name="pub_date" value="2018-07-22" min="2018-01-01" max="2030-12-31">
    <br />
    <input type="submit" />
</form>
{% endblock %}

```

## Delete a blog post

In the html file `posts.html` add an anchor tag. The complete code in the page should be:

```html

{% extends 'base.html' %}
{% block content %}
<a href="{%url 'add_posts'%}">add a blog post</a>
<ul>
  {% for post in blogs %}
  <p>Title: {{ post.title }}</p>
  <p>ID: {{ post.id }}</p>
  <p>Description: {{ post.text }}</p>
  <p>Pub Date: {{post.pub_date}}</p>
  <a href="">Delete Post</a>
  {% empty %}
  {% endfor %}
</ul>
{% endblock %}
```

In `views.py`, add an extra function to handle the deletion process:

```python
def delete_post(request, id):
    blog_post = Blog.objects.get(id=id)
    print(blog_post) ## check the terminal, it should output the object before it gets deleted
    blog_post.delete()
    return redirect('posts')
```

Let's create a path to handle the view. In `urls.py` add:

```python

    path('delete_post/<int:id>', views.delete_post, name='delete_post')
```

Go back to `posts.html` and add the route to the anchor tag:

```html
{% extends 'base.html' %}
{% block content %}
<a href="{%url 'add_posts'%}">add a blog post</a>
<ul>
  {% for post in blogs %}
  <p>Title: {{ post.title }}</p>
  <p>ID: {{ post.id }}</p>
  <p>Description: {{ post.text }}</p>
  <p>Pub Date: {{post.pub_date}}</p>
  <a href="{% url 'delete_post' post.id%}">Delete Post</a>

  {% empty %}
  {% endfor %}
</ul>
{% endblock %}

```

You should now be able to delete blog posts!




