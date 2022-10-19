from django.shortcuts import render


def show_homepage(request):
    context = {}

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

