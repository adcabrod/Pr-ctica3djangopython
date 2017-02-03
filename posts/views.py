from django.shortcuts import render
from posts.models import Post
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound, HttpResponse
from django.views import View
from django.utils import timezone
from django.shortcuts import render
from posts.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from practica3.forms import PostForm
from django.urls import reverse



class home(View):

    def get(self, request):
        """
        Renderiza el home con un listado de posts
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        # recupera todos los posts de la base de datos y los ordeno por fecha de publicación
        posts = Post.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')
        context ={'posts_list': posts[:7]}
        return render(request, 'posts/home.html', context)

class blogsView(View):

    def get(self, request):

        """
        Renderiza el /blogs con un listado de los blogs, un blog por usuario
        :param  request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpRequest con los datos de la respuesta
        """

        blog = User.objects.order_by('username')
        context = {'blogs_list': blog[:7]}
        return render(request, 'posts/blogs.html', context)


class PostView(View):
    def get (self, request, username, pk):
        """
        Renderiza un post en detalle
        :param request:objeto HttpRequest con los datos de la petición
        :param pk: clave primaria del post a recuperar
        :return: objeto httpResponse con los datos de la respuesta
        """
        post = PostQueryset.get_posts_by_user(request.user, username).filter(pk=pk)
        context = {'post': post[0], 'username': username}
        return render(request, 'posts/postView.html', context)

class blogDetailView(View):
    def get(self, request, username):
        """
        Renderiza los artículos de un usuario
        :param request: objeto HttpRequest con los datos de la petición
        :param username: username del autor del artículo a recuperar
        :return: objeto HttpResponse con los datos de la respuesta
        """
        # Muestro los post de un usuario en concreto
        posts = PostQueryset.get_posts_by_user(request.user, username).order_by('-publication_date')
        context = {'posts_list': posts, 'username': username}
        return render(request, 'posts/userBlog.html', context)


class PostCreationView(View):

    @method_decorator(login_required())
    def get(self, request):
        """
        Presenta el formulario para crear un post
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        message = None
        post_form = PostForm()
        context = {'form': post_form, 'message': message}
        return render(request, 'posts/post_creation.html', context)

    @method_decorator(login_required())
    def post(self, request):
        """
        Presenta el formulario para crear un post y, en caso de que la petición sea POST la valida
        y la crea en caso de que sea válida
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        message = None
        post_with_user = Post(owner=request.user)
        post_form = PostForm(request.POST, instance=post_with_user)
        if post_form.is_valid():
            new_post = post_form.save()
            post_form = PostForm()
            message = 'Post creado satisfactoriamente. <a href="{0}">Ver post</a>'.format(
                reverse('post_view', args=[new_post.owner.username, new_post.pk])
            )
            # reverse - django hace la revision de la url post_view con los argumentos username y pk

        context = {'form': post_form, 'message': message}
        return render(request, 'posts/post_creation.html', context)











class PostQueryset(object):

    @staticmethod
    def get_posts_by_user(user, username):
        posts = Post.objects.all().select_related("owner")
        if not user.is_authenticated():
            posts = posts.filter(publication_date__lte=timezone.now(), owner__username=username)
        elif not user.is_superuser:
            if user.username == username:
                posts = posts.filter(owner=user)
            else:
                posts = posts.filter(publication_date__tle=timezone.now(), owner__username=username)
        else:
            posts = posts.filter(owner__username=username)
        return posts





class PostListApiQueryset(object):
    @staticmethod
    def get_post_by_user(user, username):
        posts = Post.object.all().select_related("owner")
        if not user.is_authenticated():
            posts = posts.filter(publication_date_lte=timezone.now(), owner__username=username)
        elif not user.is_superuser:
            if user.username == username:
                posts = posts.filter(owner=user)
            else:
                posts = posts.filter(publication_date__lte=timezone.now(), owner__username=username)
        else:
            posts = posts.filter(owner__username=username)
        return posts




