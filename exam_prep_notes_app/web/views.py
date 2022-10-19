from django.shortcuts import render, redirect, get_object_or_404

from exam_prep_notes_app.web.forms import CreateProfileForm, AddNoteForm, EditNoteForm, DeleteNoteForm
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
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show homepage')
    else:
        form = AddNoteForm()

    context = {
        'form': form,
    }

    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('show homepage')
    else:
        form = EditNoteForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            note.delete()
            return redirect('show homepage')
    else:
        form = DeleteNoteForm(instance=note)

    context = {
        'note': note,
        'form': form,
    }

    return render(request, 'note-delete.html', context)


def show_note(request, pk):
    note = get_object_or_404(Note, pk=pk)

    context = {
        'note': note,
    }

    return render(request, 'note-details.html', context)


def show_profile(request):
    profile = get_profile()
    notes_count = Note.objects.all().count()

    context = {
        'profile': profile,
        'notes_count': notes_count,
    }

    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = get_profile()
    notes = Note.objects.all()

    if profile:
        notes.delete()
        profile.delete()

    return redirect('show homepage')

