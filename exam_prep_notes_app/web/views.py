from django.shortcuts import render, redirect

from exam_prep_notes_app.web.forms import CreateProfileForm
from exam_prep_notes_app.web.models import Profile, Note


def get_profile():
    profile = Profile.objects.all().first()
    return profile


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show homepage')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)


def show_homepage(request):
    profile = get_profile()
    notes = Note.objects.all()

    if profile is None:
        return create_profile(request)

    context = {
        'profile': profile,
        'notes': notes,
    }

    return render(request, 'home-with-profile.html', context)


def add_note(request):
    context = {}

    return render(request, 'note-create.html', context)


def edit_note(request):
    context = {}

    return render(request, 'note-edit.html', context)


def delete_note(request):
    context = {}

    return render(request, 'note-delete.html', context)


def show_note(request):
    context = {}

    return render(request, 'note-details.html', context)


def show_profile(request):
    context = {}

    return render(request, 'profile.html', context)

