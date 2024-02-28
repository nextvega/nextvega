# General Librery's
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound, HttpResponse
from .forms import FormContacto, FormSingUp, FormSingIn
from .models import EntryBlog, ComentariosBlog,CustomUser
from django.contrib.auth.models import User
from django.contrib import messages


# Create User Token
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse


# Create Template Email
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


# Login Session
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def inicio(request):
    return render(request, 'home/index.html',{
        'title': 'Innovating Through Code'
    })

def about(request):
    return render(request, 'about/index.html',{
        'title': 'Get to Know Me'
    })

def skills(request):
    return render(request, 'skills/index.html',{
        'title': 'My Best Skills'
    })

def portfolio(request):
    return render(request, 'portfolio/index.html',{
        'title': 'Clients Portfolio'
    })

def services(request):
    return render(request, 'services/index.html',{
        'title': 'Tech Services'
    })

def blog(request):
    entryblog = EntryBlog.objects.all().order_by('-id')
    return render(request, 'blog/index.html',{
        'title': 'Blog & News',
        'entryblog': entryblog
    })

def entry(request, slug=""):
    entryblog = get_object_or_404(EntryBlog, slug_noticia = slug)
    comentarios = ComentariosBlog.objects.filter(noticia_comentario = entryblog.id).filter(comentario_padre__isnull = True).order_by('-id')
    countComentarios = ComentariosBlog.objects.filter(noticia_comentario = entryblog.id).count()

    if request.method == 'POST':
        identifier = request.POST.get('identifier')
        usuario = request.POST.get('usuario')
        if usuario.isdigit():
            try:
                searchUsuario = CustomUser.objects.get(pk=usuario)
                if searchUsuario.is_authenticated:
                    if identifier == 'parent':
                        idpost = request.POST.get('idpost')
                        contenido = request.POST.get('contenido') 

                        if len(contenido) > 25:
                            searchIDPost = EntryBlog.objects.get(pk = idpost)
                            newcomentarioBlog = ComentariosBlog(
                                autor_comentario = searchUsuario.first_name,
                                contenido_comentario = contenido,
                                noticia_comentario = searchIDPost,
                                comentario_padre = None,
                                primario = True
                            )
                            newcomentarioBlog.save()
                            return render(request, 'blog/entry.html',{
                                'title': entryblog.nombre_noticia,
                                'entry': entryblog,
                                'comentarios': comentarios,
                                'countComentarios': countComentarios
                            })

                        else:
                            return render(request, 'blog/entry.html',{
                                'title': entryblog.nombre_noticia,
                                'entry': entryblog,
                                'comentarios': comentarios,
                                'countComentarios': countComentarios,
                                'contenidoSave': contenido
                            })


                    elif identifier == 'children':
                        idpost = request.POST.get('idpost')
                        relationship = request.POST.get('relationship')
                        contenido = request.POST.get('contenido') 

                        searchIDPost = EntryBlog.objects.get(pk = idpost)
                        relationshipID = ComentariosBlog.objects.get(pk = relationship)

                        if len(contenido) > 25:

                            newcomentarioBlog = ComentariosBlog(
                                autor_comentario = searchUsuario.first_name,
                                contenido_comentario = contenido,
                                noticia_comentario = searchIDPost,
                                comentario_padre = relationshipID,
                                primario = False
                            )

                            newcomentarioBlog.save()

                            return render(request, 'blog/entry.html',{
                                'title': entryblog.nombre_noticia,
                                'entry': entryblog,
                                'comentarios': comentarios,
                                'countComentarios': countComentarios
                            })
                        
                        else:
                            return render(request, 'blog/entry.html',{
                                'title': entryblog.nombre_noticia,
                                'entry': entryblog,
                                'comentarios': comentarios,
                                'countComentarios': countComentarios,
                                'contenidoSaveChildren': contenido
                            })

                    else:
                        return HttpResponseNotFound('<h1>Ocurrio Un Error</h1>')
                    
            except User.DoesNotExist:
                return HttpResponseNotFound('<h1>Ocurrio Un Error</h1>')
        else:
            return redirect('blog')


    return render(request, 'blog/entry.html',{
        'title': entryblog.nombre_noticia,
        'entry': entryblog,
        'comentarios': comentarios,
        'countComentarios': countComentarios
    })

def contact(request):

    formcontacto = FormContacto()
    return render(request, 'contact/index.html',{
        'title': 'Contact Us',
        'formcontacto' : formcontacto
    })


# Views signIn and signUp
def singUp(request):
    if request.method == 'POST':
        formSingUp = FormSingUp(request.POST)
        if formSingUp.is_valid():
            data_form = formSingUp.cleaned_data

            name_up = data_form.get('name_up')
            email_up = data_form.get('email_up')
            password_up = data_form.get('password_up')

            try:
                user = CustomUser.objects.create_user(username=name_up, email=email_up, password=password_up)
                token = default_token_generator.make_token(user)

                user.first_name = name_up
                user.last_name = name_up
                user.token = token
                user.is_active = False
                user.save()

                if user:
                    email_subject = 'Confirmar tu cuenta en NextVega'
                    email_body = render_to_string('layouts/email.html' , {
                        'confirmation_link' : request.build_absolute_uri(reverse("confirm_account", args=[user.pk, token])),
                        'name_up': name_up
                    })
                    # Crea un mensaje de correo electrónico
                    email_subject = 'Confirmar tu cuenta en NextVega'
                    email_from = 'vegaricardo636@gmail.com'
                    email_to = [user.email]

                    # Envía el correo electrónico como HTML
                    msg = EmailMultiAlternatives(email_subject, email_body, email_from, email_to)
                    msg.attach_alternative(email_body, "text/html")  # Adjunta la versión HTML
                    msg.send()

                else:
                    return redirect('inicio')
            except:
                return redirect('inicio')
            
    return redirect('inicio')

def signIn(request):
    if request.method == 'POST':
        formSignIn = FormSingIn(request.POST)
        if formSignIn.is_valid():
            data_form = formSignIn.cleaned_data
            email_in = data_form.get('email_in')
            password_in = data_form.get('password_in')
            user = authenticate(request, username = email_in, password = password_in)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back: {user}', extra_tags='signin')
                return redirect(inicio)
            else:
                messages.error(request, 'Incorrect username or password',extra_tags='errorForm')
                return redirect(inicio)
        else:
            return redirect(inicio)
        
    return redirect(inicio)

def logout_session(request):
    if request.method == 'GET':
        logout(request)
        return redirect(inicio)

    return redirect(inicio)


def confirm_account(request, user_id, token):
    if request.method == 'GET':
        try:
            searchToken = CustomUser.objects.get(pk=user_id, token=token)
            if searchToken:
                searchToken.token = None
                searchToken.is_active = True
                searchToken.save()
            else:
                return HttpResponse("¡Ocurrio Un Error!")
        except:
            return HttpResponse("¡Ocurrio Un Error!")
    
    return redirect('inicio')