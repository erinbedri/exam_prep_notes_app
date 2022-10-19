from django.forms import ModelForm

from exam_prep_notes_app.web.models import Profile


class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

