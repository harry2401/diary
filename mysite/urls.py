from django.contrib             import admin
from django.urls                import path, include
from django.conf                import settings
from django.conf.urls.static    import static
from django.conf.urls           import url
from .                          import views
from .views  import SiteUpdate, NoteUpdate, PhotoInsert, PhotoDelete, PhotoUpdate, MedreadingInsert, MedreadingDelete, MedreadingUpdate
from .views  import BookmarkInsert, BookmarkUpdate, BookmarkDelete , CategoryInsert, CategoryDelete , IdentifierInsert, IdentifierDelete
from .views  import EmailhostInsert, EmailhostDelete , Identifier2Insert, Identifier2Delete , LoginInsert, LoginUpdate, LoginDelete
#
urlpatterns = [
    path('',                                    views.homepage,                                                                name='homepage'),
    path('logout/',                             views.logout,                    {'next_page': settings.LOGOUT_REDIRECT_URL},  name='logout'),
    path('accounts/',                           include('django.contrib.auth.urls')),
    path('accounts/profile/' ,                  views.fromlogin ),
    path('admin/',                              admin.site.urls),
#
    path('2r4rj34ri2ujjef',                     views.menu,                                                                    name='menu'),
#
    path('siteupdate/<int:pk>/',                SiteUpdate.as_view(),                                                          name='siteupdate'),
    path('noteupdate/<int:pk>/',                NoteUpdate.as_view(),                                                          name='noteupdate'),
#
    path('photolist',                           views.photo_list,                                                              name='photolist'),
    path('photolistdeleted',                    views.photo_list_deleted,                                                      name='photolistdeleted'),
    path('photoinsert',                         PhotoInsert.as_view(),                                                         name='photoinsert'),
    path('photoupdate/<int:pk>/',               PhotoUpdate.as_view(),                                                         name='photoupdate'),
    path('photochange/<int:pk>/<slug:mode>/',   views.photo_change,                                                            name='photochange'),
    path('photodeleteperm/<int:pk>/',           PhotoDelete.as_view(),                                                         name='photodeleteperm'),
#
    path('eventlist/<slug:periodsought>/)',               views.event_list,                         name='eventlist'),
    path('eventlist',                                     views.event_list,                         name='eventlist'),
    path('eventinsertupdate/<int:pk>/<slug:mode>/)',      views.event_insert_update,                name='eventinsertupdate'),
    path('eventchange/<int:pk>/<slug:mode>/',   views.event_change,                                                            name='eventchange'),
#
    path('medreadinglist',                      views.medreading_list,                                                        name='medreadinglist'),
    path('medreadinginsert',                    MedreadingInsert.as_view(),                          name='medreadinginsert'),
    path('medreadingupdate/<int:pk>/',          MedreadingUpdate.as_view(),                          name='medreadingupdate'),
    path('medreadingdeleteperm/<int:pk>/',      MedreadingDelete.as_view(),                          name='medreadingdeleteperm'),
#
    path('bookmarklist',                           views.bookmark_list,                                                         name='bookmarklist'),
    path('bookmarklist/<slug:orderby>/',           views.bookmark_list,                                                         name='bookmarklist'),
    path('bookmarkinsert',                         BookmarkInsert.as_view(),                                                    name='bookmarkinsert'),
    path('bookmarkupdate/<int:pk>/',               BookmarkUpdate.as_view(),                                                    name='bookmarkupdate'),
    path('bookmarkdeleteperm/<int:pk>/',           BookmarkDelete.as_view(),                                                    name='bookmarkdeleteperm'),
#
    path('categorylist',                           views.category_list,                                                         name='categorylist'),
    path('categoryinsert',                         CategoryInsert.as_view(),                                                    name='categoryinsert'),
    path('categorydeleteperm/<int:pk>/',           CategoryDelete.as_view(),                                                    name='categorydeleteperm'),
#
    path('identifierlist',                           views.identifier_list,                                                 name='identifierlist'),
    path('identifierinsert',                         IdentifierInsert.as_view(),                                            name='identifierinsert'),
    path('identifierdeleteperm/<int:pk>/',           IdentifierDelete.as_view(),                                            name='identifierdeleteperm'),
#
    path('emailhostlist',                           views.emailhost_list,                                                 name='emailhostlist'),
    path('emailhostinsert',                         EmailhostInsert.as_view(),                                            name='emailhostinsert'),
    path('emailhostdeleteperm/<int:pk>/',           EmailhostDelete.as_view(),                                            name='emailhostdeleteperm'),
#
    path('identifier2list',                           views.identifier2_list,                                                 name='identifier2list'),
    path('identifier2insert',                         Identifier2Insert.as_view(),                                            name='identifier2insert'),
    path('identifier2deleteperm/<int:pk>/',           Identifier2Delete.as_view(),                                            name='identifier2deleteperm'),
#
    path('loginlist',                           views.login_list,                                                         name='loginlist'),
    path('loginlist/<slug:orderby>/',           views.login_list,                                                         name='loginlist'),
    path('logininsert',                         LoginInsert.as_view(),                                                    name='logininsert'),
    path('loginupdate/<int:pk>/',               LoginUpdate.as_view(),                                                    name='loginupdate'),
    path('logindeleteperm/<int:pk>/',           LoginDelete.as_view(),                                                    name='logindeleteperm'),
#
    path('password/',                                                                      views.password,          name='password'),
]

#

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
