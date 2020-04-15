from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import registration_form
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import update_profile_form,update_register_form
# Create your views here.
def register(request):
    # form=registration_form()
    if request.method == "POST":
        form=registration_form(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created successfully for {username} !')
            # form.save()
            return redirect("blog-home")
    else:
        form=registration_form()
    # context={'form':registration_form(),}
    return render(request,'users/register.html',{'form':form})


# logged_in_user = request.user
#     logged_in_user_posts = Post.objects.filter(user=user)
@login_required
def profile(request):
    user1=request.user
    # print(type(user1))
    # print(type(request.user.username))
    # print(user1)
    # blog_list=user1.post_set.all()
    blog1=Post.objects.filter(author=user1)
    context={'posts':blog1,}
    return render(request,'users/profile.html',context)


@login_required
def profile(request):
    if request.method == "POST":
        r_form=update_register_form(request.POST, instance=request.user)
        p_form=update_profile_form(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if r_form.is_valid() and p_form. is_valid():
            messages.success(request,f' {request.user} your account has been updated succcessfully!')
            r_form.save()
            p_form.save()
            return redirect('profile')

    r_form=update_register_form(instance=request.user)
    p_form=update_profile_form(instance=request.user.profile)



    context = {
     'r_form': r_form,
     'p_form': p_form,
    }

    return render(request,'users/profile.html',context)
