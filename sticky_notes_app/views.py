# Import functions for http
from django.shortcuts import render, get_object_or_404, redirect
# Import note model
from .models import Note
# Import note form
from .forms import NoteForm


# Define view function for notes list used course material
# course material "Django Sticky Notes application.pdf" for
# reference to function formatting
def list_notes(request):
    notes = Note.objects.all()

    context = {
        "notes": notes,
        "title": "Sticky notes list",
    }
    return render(request, "notes_list.html", context)


# Define view function for note detail
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, "note_detail.html", {"note": note})


# Define view function to create note
def create_note(request):
    # Request form for post requests
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect("list_notes")
    else:
        form = NoteForm()
    return render(request, "note_form.html", {"form": form})


# Define view function to update note
def update_note(request, pk):
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


# Define view function to delete note
def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect("list_notes")
