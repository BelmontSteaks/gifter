from django.shortcuts import render, redirect, render_to_response, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from lamps.models import List, Gift
from lamps.forms import UserForm, UserProfileForm, ListForm, AddGiftsForm, EditGiftsForm
from django.contrib.auth import logout
from django.template import RequestContext
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login
from django.forms.models import modelformset_factory

@login_required
def add_list(request):
    if request.method == 'POST':
        lf = ListForm(request.POST, prefix='list')
        if lf.is_valid():
            newlist = lf.save(commit=False)
            newlist.user_id = request.user
            newlist.save()
            urlslug = newlist.slug
            return redirect(list_detail, urlslug, request.user.id)
    else:
        lf = ListForm(prefix='list')
    return render(request, 'gifter/add_list.html', {'listform': lf})

@login_required
def my_list_view(request):
    user = request.user
    myLists = List.objects.filter(user_id=user)
    context = {'myLists': myLists}
    return render(request, 'gifter/my_lists.html', context)

@login_required
def list_detail(request, slug, lid):
    my_list = List.objects.get(list_id=lid, user_id=request.user.id)
    try:
        gift_on_list = Gift.objects.get(list__list_id=lid, list__user_id=request.user.id)
    except Gift.DoesNotExist:
        context = {'my_list': my_list}
        return render(request, 'gifter/list_detail.html', context)
        
    context = {'my_list': my_list, 'gift_on_list': gift_on_list}
    return render(request, 'gifter/list_detail.html', context)

@login_required
def add_gifts(request):
    if request.method == 'POST':
        gf = AddGiftsForm(request.POST, prefix='gifts')
        if gf.is_valid():
            newgift = gf.save(commit=False)
            newgift.user_id = request.user
            newgift.save()
            return HttpResponse("Success")
    else:
        gf = AddGiftsForm(prefix='gifts')
    return render(request, 'gifter/add_gifts.html', {'giftsform': gf})

@login_required
def buy(request, slug):
    if request.method == 'POST':
        formset = EditGiftsForm(request.POST, prefix='buy')

        if formset.is_valid():
            # iterate over all forms in the formset
            for form in formset.forms:
                # only do stuff for forms in which is_checked is checked
                if form.cleaned_data.get('purchased'):
                    form.save()

            redirect('index')

    else:
        GiftFormSet = modelformset_factory(Gift)
        formset = GiftFormSet(queryset=Gift.objects.filter(list__slug=slug, list__user_id=request.user))
                

    return render(request, 'gifter/edit_gifts.html', {'formset': formset})

def index(request):
    return render(request, 'gifter/index.html')

def custom_login(request):
    if request.user.is_authenticated():
        return render(request, 'gifter/index.html')
    else:
        return login(request, template_name='gifter/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/../../gifter/login')

def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix='user')
        upf = UserProfileForm(request.POST, prefix='userprofile')
        if uf.is_valid() * upf.is_valid():
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return render_to_response('gifter/index.html', {'userform': uf, 'userprofileform':upf}, context_instance=RequestContext(request))
    else:
        uf = UserForm(prefix='user')
        upf = UserProfileForm(prefix='userprofile')
    return render(request, 'gifter/register.html', {'userform': uf, 'userprofileform':upf})