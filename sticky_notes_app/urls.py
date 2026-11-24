from django.urls import path
from .views import (
    list_notes,
    note_detail,
    create_note,
    update_note,
    delete_note,
)

urlpatterns = [
    path("", list_notes, name="list_notes"),
    path("note/<int:pk>/", note_detail, name="note_detail"),
    path("note/create", create_note, name="create_note"),
    path("note/<int:pk>/edit/", update_note, name="update_note"),
    path("post/<int:pk>/delete/", delete_note, name="note_delete"),
]
