from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from to_do_list.forms import UserForm, UserProfileForm, CreateTaskForm, ManageTaskForm, MemberofForm, GroupForm
from django.contrib.auth.decorators import login_required
from to_do_list.models import UserProfile, Group, Task, Memberof
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django import forms
from django.db.models import Q




# Create your views here.
def login(request):
    # Request the context of the request.
    context = RequestContext(request)
    if request.user.is_authenticated():
        return HttpResponseRedirect('/to_do_list/mainpage/')

    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                auth_login(request, user)
                request.session['sessionUsername'] = username

                return HttpResponseRedirect('/to_do_list/mainpage/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

            # The request is not a HTTP POST, so display the login form.
            # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...

        return render_to_response('login.html', {}, context)


@login_required
def mainpage(request):
    context = RequestContext(request)
    sessuser = request.session['sessionUsername']

    # Create a context dictionary which we can pass to the template rendering engine.
    # We start by containing the name of the category passed by the user.
    context_dict = {'Task_name': sessuser}

    try:
    # Can we find a category with the given name?
    # If we can't, the .get() method raises a DoesNotExist exception.
    # So the .get() method returns one model instance or raises an exception.

        user = User.objects.get(username=sessuser).pk
        userprofile = UserProfile.objects.get(UserProName=user).pk
        task_d = Task.objects.filter(User=userprofile, Completed=False)
        task_c = Task.objects.filter(User=userprofile, Completed=True)
        groupin = Memberof.objects.filter(MemberName=userprofile)

        for gp in groupin:
            gp.url = gp.MemGroupName.GroupName.replace(" ", "_")
            print gp.url
        context_dict['task_c'] = task_c
        context_dict['userprofile'] = userprofile
        context_dict['task_d'] = task_d
        context_dict['groupin'] = groupin


    except Task.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    if 'mark_tasks_done' in request.POST:
        if request.POST.getlist('mark_done'):
            done_items = request.POST.getlist('mark_done')
            # Iterate through array of done items and update its representation in the model
            for thisitem in done_items:
                p = Task.objects.get(id=thisitem)
                p.Completed = True
                p.save()
    if 'mark_task_undone' in request.POST:
        if request.POST.getlist('undo_completed_task'):
            undone_items = request.POST.getlist('undo_completed_task')
            for thisitem in undone_items:
                p = Task.objects.get(id=thisitem)
                p.Completed = False
                p.save()
    if 'mark_task_undone' in request.POST:
        if request.POST.getlist('del_task'):
            deleted_items = request.POST.getlist('del_task')
            for thisitem in deleted_items:
                p = Task.objects.get(id=thisitem)
                p.delete()

    return render_to_response('mainpage.html', context_dict, context)


@login_required
def viewgroup(request, group_name_url):
    context = RequestContext(request)

    group_name = group_name_url.replace('_', ' ')

    context_dict = {'group_name': group_name}

    sessuser = request.session['sessionUsername']

    try:
        grp = Group.objects.get(GroupName=group_name)
        members = Memberof.objects.filter(MemGroupName=grp.id)
        task = Task.objects.filter(Group=grp.id)

        context_dict['members'] = members
        context_dict['grp'] = grp
        context_dict['task'] = task

    except grp.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render_to_response('viewgroup.html', context_dict, context)


def register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        memberof = MemberofForm()
        group = GroupForm()

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.UserProName = user
            profile.save()

            gp = Group(Creator=profile, GroupName=profile, GroupDescription=profile)
            gp.save()
            Memberof(MemberName=profile, MemGroupName=gp).save()

            registered = True


        else:
            print user_form.errors, profile_form.errors


    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response(
        'register.html',
        {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.


    logout(request)
    try:
        del request.session['sessionUsername']
    except KeyError:
        pass


    # Take the user back to the homepage.
    return redirect('/to_do_list/')


"""
@login_required
def createtask(request, group_id_url):
    context = RequestContext(request)

    sessuser = request.session['sessionUsername']
    user = User.objects.get(username=sessuser).pk
    userprofile = UserProfile.objects.get(UserProName=user).pk

    grpname = Memberof.objects.filter(MemberName=userprofile).values_list('MemGroupName__GroupName', flat=True)
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return redirect('/to_do_list/mainpage')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        #If the request was not a POST, display the form to enter details.
        #CreateTaskForm.base_fields['User'] = forms.ModelChoiceField(
         #   queryset=Memberof.objects.filter(MemGroupName=group_id_url))
        #CreateTaskForm.base_fields['Group'] = forms.ModelChoiceField(
         #   queryset=Memberof.objects.filter(MemberName=userprofile).values_list('MemGroupName__GroupName', flat=True))
        form = CreateTaskForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('createtask.html', {'form': form}, context)
"""


@login_required
def createtask(request):
    context = RequestContext(request)

    sessuser = request.session['sessionUsername']
    user = User.objects.get(username=sessuser).pk
    userprofile = UserProfile.objects.get(UserProName=user).pk

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return redirect('/to_do_list/mainpage')
        else:

            print form.errors
    else:

        form = CreateTaskForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('createtask.html', {'form': form}, context)


@login_required
def edittask(request, task_id_url):
    task_url_id = task_id_url.replace('_', ' ')

    sessuser = request.session['sessionUsername']

    context_dict = {'Task_name': sessuser}

    try:
        user = User.objects.get(username=sessuser).pk
        userprofile = UserProfile.objects.get(UserProName=user)
        task_d = Task.objects.get(id=task_url_id)
        taskk = get_object_or_404(Task, id=task_id_url)

        if request.POST:
            form = ManageTaskForm(request.POST, instance=taskk)

            if form.is_valid():
                form.save()
                messages.success(request, "The task has been edited.")
                return redirect('/to_do_list/mainpage')
        else:
            form = ManageTaskForm(instance=taskk)

        context_dict['task'] = task_d
        context_dict['userform'] = form

    except task_d.DoesNotExist:
        pass

    return render_to_response('edittask.html', context_dict, context_instance=RequestContext(request))



@login_required
def creategrp(request, user_id):
    context = RequestContext(request)

    sessuser = request.session['sessionUsername']
    user = User.objects.get(username=sessuser).pk
    userprofile = UserProfile.objects.get(UserProName=user)

    if request.method == 'POST':
        form = GroupForm(request.POST)

        if form.is_valid():
            f = form.save(commit=False)
            f.Creator = userprofile
            f.save()
            Memberof(MemberName=userprofile, MemGroupName=f).save()

            return redirect('/to_do_list/mainpage')
        else:

            print form.errors
    else:

        form = GroupForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('creategrp.html', {'form': form}, context)
