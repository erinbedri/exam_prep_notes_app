from django import forms

from exam_prep_notes_app.web.models import Profile, Note


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class DeleteNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'readonly': True}),
            'content': forms.TextInput(attrs={'readonly': True}),
            'image_url': forms.URLInput(attrs={'readonly': True}),
        }
