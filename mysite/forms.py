from django                              import forms
from django.forms.widgets                import CheckboxSelectMultiple
from .models                             import Site, Photo, Event
from .models                             import Medreading, Bookmark, Category, Identifier, Emailhost, Identifier2, Login

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ('backgroundcolour', 'datecolour', 'detailcolour')


class NoteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ('note',)

class PhotoInsertForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title', 'cover', 'notes')

class PhotoUpdateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title', 'priority', 'notes')

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_date', 'detail', 'addendum')

class PasswordForm(forms.Form):
    password = forms.CharField(label='New password', max_length=20)

class MedreadingForm(forms.ModelForm):
    class Meta:
        model = Medreading
        fields = ('weight', 'glucose', 'blood_pressure_1', 'blood_pressure_2', 'HbA1c', 'HDL', 'LDL', 'reading_date', 'notes')

class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ('name', 'category', 'subcategory', 'notes')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'notes')

class IdentifierForm(forms.ModelForm):
    class Meta:
        model = Identifier
        fields = ('name', 'notes')

class EmailhostForm(forms.ModelForm):
    class Meta:
        model = Emailhost
        fields = ('name', 'notes')

class Identifier2Form(forms.ModelForm):
    class Meta:
        model = Identifier2
        fields = ('name', 'notes')

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ('bookmark', 'identifier', 'emailhost', 'identifier2', 'notes')

"""
class ColourForm(forms.ModelForm):
    class Meta:
        model = Colour
        fields = ('name', 'specification', 'notes')
"""