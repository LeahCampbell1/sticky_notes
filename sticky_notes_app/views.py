
# Import functions for HTTP
from django.shortcuts import render, get_object_or_404, redirect
# Import note model
from .models import Note
# Import note form
from .forms import NoteForm


def list_notes(request):
    """Display a list of all notes.

    :param request: The HTTP request object.
    :returns: The rendered notes list page.
    :rtype: HttpResponse
    """
    notes = Note.objects.all()

    context = {
        "notes": notes,
        "title": "Sticky notes list",
    }
    return render(request, "notes_list.html", context)


def note_detail(request, pk):
    """Display the details of a selected note.

    :param request: The HTTP request object.
    :param int pk: The note's primary key.
    :returns: The rendered note detail page.
    :rtype: HttpResponse
    """
    note = get_object_or_404(Note, pk=pk)
    return render(request, "note_detail.html", {"note": note})


def create_note(request):
    """Create a new note using the submitted form.

    :param request: The HTTP request object.
    :returns: The rendered form or a redirect to the notes list.
    :rtype: HttpResponse
    """
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect("list_notes")
    else:
        form = NoteForm()
    return render(request, "note_form.html", {"form": form})


def update_note(request, pk):
    """Update an existing note.

    :param request: The HTTP request object.
    :param int pk: The note's primary key.
    :returns: The rendered form or a redirect to the notes list.
    :rtype: HttpResponse
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect("list_notes")
    else:
        form = NoteForm(instance=note)
    return render(request, "note_form.html", {"form": form})


def delete_note(request, pk):
    """Delete an existing note.

    :param request: The HTTP request object.
    :param int pk: The note's primary key.
    :returns: A redirect to the notes list.
    :rtype: HttpResponseRedirect
    """
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect("list_notes")
