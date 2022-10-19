from django.forms import ModelForm

from exam_prep_notes_app.web.models import Profile, Note


class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class AddNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
