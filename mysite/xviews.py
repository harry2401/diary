from django.utils                   import timezone
from django.contrib.auth.models     import User
from django.shortcuts               import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls                    import reverse_lazy
from .models                        import Site, Photo, Event, Medreading, Bookmark, Category, Identifier, Emailhost, Identifier2, Login
from .forms                         import SiteForm, NoteForm, PhotoInsertForm, PhotoUpdateForm
from .forms                         import EventForm, PasswordForm, MedreadingForm
from .forms                         import BookmarkForm, CategoryForm, IdentifierForm, EmailhostForm, Identifier2Form, LoginForm
from django.views.generic           import CreateView, UpdateView, DeleteView, ListView
from mysite.settings                import TITLE


def fromlogin(request):
      return redirect('eventlist', 'current')

def logout(request):
    logout(request)

def homepage(request):
    return redirect('eventlist', 'current')

@login_required
def menu(request):
    site                                                                            =  Site.objects.get()
    context                                                                         =   {'site': site}
    return render                                                                      (request, 'mysite/menu.html', context)

class SiteUpdate(UpdateView):
    model = Site
    form_class = SiteForm
    template_name = 'mysite/insert_update.html'
    success_url = reverse_lazy('menu')

class NoteUpdate(UpdateView):
    model = Site
    form_class = NoteForm
    template_name = 'mysite/insert_update.html'
    success_url = reverse_lazy('menu')

"""
@login_required
def note_update(request):
    site                                                                            =  Site.objects.get()
    if request.method                                                               != 'POST':
        form                                                                        = noteUpdateForm(instance=site)
        context                                                                     =   {'form': form}
        return render                                                               (request, 'mysite/note_update.html', context)
    else:
        form                                                                        = noteUpdateForm(request.POST, instance=site)
        if form.is_valid():
            note                                                                    = form.save(commit=False)
            note.save()
            form.save_m2m()
            return redirect('eventlist', 'current')
        else:
            context                                                                 =   {'form': form, 'site': site}
            return render                                                               (request, 'mysite/note_update.html', context)
"""

@login_required
def photo_list(request):
    site                                             =     Site.objects.get()
    photos                                           =     Photo.objects.filter(is_live=True).order_by('-priority','-created_date')
    context                                          =     {'photos': photos, 'liveness': 'live', 'site': site}
    return render                                          (request, 'mysite/photo_list.html', context)

@login_required
def photo_list_deleted(request):
    site                                             =     Site.objects.get()
    photos                                           =     Photo.objects.filter(is_live=False).order_by('-priority','-created_date')
    context                                          =     {'photos': photos, 'liveness': 'deleted', 'site': site}
    return render                                          (request, 'mysite/photo_list.html', context)

class PhotoInsert(CreateView):
    model = Photo
    form_class = PhotoInsertForm
    template_name = 'mysite/insert_update.html'
    success_url = reverse_lazy('photolist')

class PhotoUpdate(UpdateView):
    model = Photo
    form_class = PhotoUpdateForm
    template_name = 'mysite/insert_update.html'
    success_url = reverse_lazy('photolist')

@login_required
def photo_change(request, pk, mode):
    photo                                                                           =   get_object_or_404(Photo, pk=pk)
    if mode                                                                         ==  'deletetemp':
        photo.is_live                                                               =   False
    elif mode                                                                       ==  'restore':
        photo.is_live                                                               =   True
    photo.save()
    return redirect('photolist')

class PhotoDelete(DeleteView):
    model = Photo
    success_url = reverse_lazy('photolist')

@login_required
def event_list(request, periodsought = 'current'):
    site                                                                            =  Site.objects.get()
    if periodsought == 'current':
        events = Event.objects.filter(is_live=True, event_date__gte=timezone.now()).order_by('event_date')
    else:
        events = Event.objects.exclude(is_live=True, event_date__gte=timezone.now()).order_by('-event_date')

    stored_event_date = '2000-01-01'
    for event in events:
        if event.event_date                          <  timezone.localtime(timezone.now()).date():
          event.status_now                       =  'past'
        elif event.is_live                       == True:
          event.status_now                       =  'live'
        else:
          event.status_now                       = 'deletednonpast'

        current_event_date                       =  event.event_date
        if event.event_date                      ==  stored_event_date:
            event.sameday                        =  True
        else:
            event.sameday                        =  False
        stored_event_date                        =  current_event_date

    #photos 				         = Photo.objects.filter(is_live=True).order_by('-priority','-created_date')
    #context = {'events': events, 'periodsought':periodsought, 'TITLE': TITLE, 'photos' : photos, 'logged_in' : request.user.is_authenticated, 'site': site}
    context = {'events': events, 'periodsought':periodsought, 'TITLE': TITLE, 'logged_in' : request.user.is_authenticated, 'site': site}
    return render(request, 'mysite/event_list.html', context)

@login_required
def event_change(request, pk, mode):
    event                                                =   get_object_or_404(Event, pk=pk)
#    if mode                                              ==  "deletetemp":
#        event.is_live                                    =   False
#        event.save()
#    elif mode                                            ==  "deleteperm":
    if mode                                              ==  "deleteperm":
        event.delete()
    else:                                                                                                       # i.e. mode = "restore"
        event.is_live                                    =   True
        event.save()
    if event.event_date                                  <   timezone.localtime(timezone.now()).date():
        return redirect                                      ('eventlist', 'notcurrent')
    else:
        return redirect                                      ('eventlist', 'current')      

@login_required
def event_insert_update(request, pk, mode):
    if mode                                               !=  "insert":
      event                                     = get_object_or_404(Event, pk=pk)
      event_saved                                     = get_object_or_404(Event, pk=pk)                           # change 1006
    if request.method                           != 'POST':
        if mode                                           ==  'insert':
            form = EventForm()
        elif mode                                         ==  'update':
            form = EventForm(instance=event)
        else:
            return redirect('eventlist')
        #return render(request, 'mysite/event_insert_update.html', {'form': form})                   # ask user for event details
        return render(request, 'mysite/insert_update.html', {'form': form})                   # ask user for event details
    else:
        if mode                                               ==  "insert":
            form = EventForm(request.POST)
        else:
            form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event                                   = form.save(commit=False)
            if event.event_date                         < timezone.localtime(timezone.now()).date():
                error_message                         = 'event date cannot be in the past, please enter a valid date'
                #return render(request, 'mysite/event_insert_update.html', {'form': form, 'error_message': error_message})
                return render(request, 'mysite/insert_update.html', {'form': form, 'error_message': error_message})
            else:
                if mode != 'insert' \
                and event.event_date == event_saved.event_date \
                and event.detail == event_saved.detail \
                and event.addendum == event_saved.addendum:
                    pass
                else:
                    event.save()
                    form.save_m2m()
                return redirect('eventlist')
        else:                                                                                  # i.e. form is not valid, ask user to resubmit it
            #return render(request, 'mysite/event_insert_update.html', {'form': form})
            return render(request, 'mysite/insert_update.html', {'form': form})

@login_required
def password(request):
  if request.method                           != "POST": # i.e. method == "GET":
    form = PasswordForm()
    return render(request, 'mysite/password.html', {'form': form})
  else:                                       # i.e method == 'POST'
    form                                      = PasswordForm(request.POST)
    if form.is_valid():
      user                              =  User.objects.get(id=request.user.id)    # get details of user
      password                                = form.cleaned_data['password']
      user.set_password(password)
      user.save()
      return redirect('eventlist')
    else:                                                                        # i.e. form is not valid, ask user to resubmit it
      return render(request, 'mysite/insert_update.html', {'form': form})


@login_required
def medreading_list(request):
    site                                           =   Site.objects.get()           
    readings                                       =   Medreading.objects.all().order_by('-reading_date')
    context                                        =   { 'readings': readings, 'title': TITLE, 'site': site}
    return render                                      (request, 'mysite/medreading_list.html', context)

class MedreadingInsert(CreateView):
    model = Medreading
    form_class = MedreadingForm
    template_name = 'mysite/insert_update.html'
    success_url = reverse_lazy('medreadinglist')

class MedreadingUpdate(UpdateView):
    model = Medreading
    form_class = MedreadingForm
    template_name = 'mysite/insert_update.html'
    success_url = reverse_lazy('medreadinglist')

class MedreadingDelete(DeleteView):
    model = Medreading
    success_url = reverse_lazy('medreadinglist')

@login_required
def bookmark_list(request, orderby='bookmark'):
    site                                           =   Site.objects.get()           
    if orderby                                     ==  'bookmark':
        bookmarks                                  =   Bookmark.objects.all().order_by('-priority', 'name')
    else:
        bookmarks                                  =   Bookmark.objects.all().order_by('category1','category2','-priority')
        #bookmarks                                  =   Bookmark.objects.all().order_by('category1')
        #bookmarks                                  =   Bookmark.objects.all().order_by('category1','name')
    context                                        =   { 'bookmarks': bookmarks, 'title': TITLE, 'site': site}
    return render                                      (request, 'mysite/bookmark_list.html', context)

class BookmarkInsert(CreateView):
    model = Bookmark
    form_class = BookmarkForm
    template_name = 'mysite/insert_update.html'
    success_url = reverse_lazy('bookmarklist')

class BookmarkUpdate(UpdateView):
    model = Bookmark
    form_class = BookmarkForm
    template_name = 'mysite/insert_update.html'
    success_url = reverse_lazy('bookmarklist')

class BookmarkDelete(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmarklist')

@login_required
def category_list(request):
    site                                           =   Site.objects.get()           
    categorys                                      =   Category.objects.all().order_by('-priority', 'name')
    context                                        =   { 'categorys': categorys, 'title': TITLE, 'site': site}
    return render                                      (request, 'mysite/category_list.html', context)

class CategoryInsert(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'mysite/insert_update.html'
    success_url = reverse_lazy('categorylist')

class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'mysite/insert_update.html'
    success_url = reverse_lazy('categorylist')

class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('categorylist')

@login_required
def identifier_list(request):
    site                                           =   Site.objects.get()           
    identifiers                                      =   Identifier.objects.all().order_by('-priority', 'name')
    context                                        =   { 'identifiers': identifiers, 'title': TITLE, 'site': site}
    return render                                      (request, 'mysite/identifier_list.html', context)

class IdentifierInsert(CreateView):
    model = Identifier
    form_class = IdentifierForm
    template_name = 'mysite/insert_update.html'
    success_url = reverse_lazy('identifierlist')

class IdentifierUpdate(UpdateView):
    model = Identifier
    form_class = IdentifierForm
    template_name = 'mysite/insert_update.html'
    success_url = reverse_lazy('identifierilist')

class IdentifierDelete(DeleteView):
    model = Identifier
    success_url = reverse_lazy('identifierlist')

@login_required
def emailhost_list(request):
    site                                           =   Site.objects.get()           
    emailhosts                                      =   Emailhost.objects.all().order_by('-priority', 'name')
    context                                        =   { 'emailhosts': emailhosts, 'title': TITLE, 'site': site}
    return render                                      (request, 'mysite/emailhost_list.html', context)

class EmailhostInsert(CreateView):
    model = Emailhost
    form_class = EmailhostForm
    template_name = 'mysite/insert_update.html'
    success_url = reverse_lazy('emailhostlist')

class EmailhostUpdate(UpdateView):
    model = Emailhost
    form_class = EmailhostForm
    template_name = 'mysite/insert_update.html'
    success_url = reverse_lazy('emailhostlist')

class EmailhostDelete(DeleteView):
    model = Emailhost
    success_url = reverse_lazy('emailhostlist')

@login_required
def identifier2_list(request):
    site                                           =   Site.objects.get()           
    identifier2s                                      =   Identifier2.objects.all().order_by('-priority', 'name')
    context                                        =   { 'identifier2s': identifier2s, 'title': TITLE, 'site': site}
    return render                                      (request, 'mysite/identifier2_list.html', context)

class Identifier2Insert(CreateView):
    model = Identifier2
    form_class = Identifier2Form
    template_name = 'mysite/insert_update.html'
    success_url = reverse_lazy('identifier2list')

class Identifier2Update(UpdateView):
    model = Identifier2
    form_class = Identifier2Form
    template_name = 'mysite/insert_update.html'
    success_url = reverse_lazy('identifier2list')

class Identifier2Delete(DeleteView):
    model = Identifier2
    success_url = reverse_lazy('identifier2list')

@login_required
def login_list(request, orderby='bookmark'):
    site                                           =   Site.objects.get()           
    if orderby                                     ==  'bookmark':
        logins                                     =   Login.objects.all().order_by('-priority')
    elif orderby                                   ==  'identifier':
        logins                                     =   Login.objects.all().order_by('identifier','emailhost','-priority')
    else:
        logins                                     =   Login.objects.all().order_by('identifier2', '-priority')
    context                                        =   { 'logins': logins, 'title': TITLE, 'site': site}
    return render                                      (request, 'mysite/login_list.html', context)

class LoginInsert(CreateView):
    model = Login
    form_class = LoginForm
    template_name = 'mysite/insert_update.html'
    success_url = reverse_lazy('loginlist')

class LoginUpdate(UpdateView):
    model = Login
    form_class = LoginForm
    template_name = 'mysite/insert_update.html'
    success_url = reverse_lazy('loginlist')

class LoginDelete(DeleteView):
    model = Login
    success_url = reverse_lazy('loginlist')

