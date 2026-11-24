# Sources used to format test statements:
# https://docs.djangoproject.com/en/5.0/topics/testing/overview/
# Course material: '06-049-2 Django – Sticky Notes Application Part 2'

from django.test import TestCase
from django.urls import reverse
from .models import Note


# Define class to test model
class NoteModelTest(TestCase):
    # Create note to test
    def setUp(self):
        Note.objects.create(title='Test Note',
                            content='This is a test note')

    # Define function to check title
    def test_note_has_title(self):
        sticky_note = Note.objects.get(id=1)
        self.assertEqual(sticky_note.title, 'Test Note')

    # Define function to check content
    def test_note_has_content(self):
        sticky_note = Note.objects.get(id=1)
        self.assertEqual(sticky_note.content, 'This is a test note')


# Define class to check note view
class NoteViewTest(TestCase):
    # Create note to test
    def setUp(self):
        Note.objects.create(title='Test Note',
                            content='This is a test note')

    # Define function to check list
    def test_sticky_note_list_view(self):
        # Call list notes function to store response
        response = self.client.get(reverse('list_notes'))
        # Check response status
        self.assertEqual(response.status_code, 200)
        # Check note title
        self.assertContains(response, 'Test Note')

    # Define function to check view
    def test_post_detail_view(self):
        # Store note in variable
        sticky_note = Note.objects.get(id=1)
        # Check note details with get
        response = self.client.get(reverse('note_detail',
                                           args=[str(sticky_note.id)]))
        # Check response status
        self.assertEqual(response.status_code, 200)
        # Check note title
        self.assertContains(response, 'Test Note')
        # Check note content
        self.assertContains(response, 'This is a test note')


# Define class to test note creation
class NoteCreateTest(TestCase):
    # Define function to create note
    def test_create_sticky_note(self):
        # Call function to create note with parameters
        response = self.client.post(reverse('create_note'),
                                    {
                                        'title': 'New Sticky Note',
                                        'content': 'A new sticky note'
                                    })
        print(Note.objects.count())
        # Check for duplicate notes
        self.assertEqual(Note.objects.count(), 1)

        # Store note in variable
        sticky_note = Note.objects.first()
        # Check new note title
        self.assertEqual(sticky_note.title, 'New Sticky Note')
        # Check new note content
        self.assertEqual(sticky_note.content, 'A new sticky note')

        # Check redirection
        self.assertEqual(response.status_code, 302)


# Define class to update note
class NoteUpdateTest(TestCase):
    # Create note to update
    def setUp(self):
        self.sticky_note = Note.objects.create(
            title='Note to update',
            content='Content that will be updated'
        )

    def test_update_sticky_note(self):
        # Call function to update note
        response = self.client.post(
            reverse('update_note', args=[self.sticky_note.id]),
            {
                'title': 'Updated note',
                'content': 'Updated details of note'
            }
        )
        # Check note count, check for duplicates
        self.assertEqual(Note.objects.count(), 1)
        # Store note from database in variable
        updated_note = Note.objects.get(id=self.sticky_note.id)

        # Check update title
        self.assertEqual(updated_note.title, 'Updated note')
        # Check update content
        self.assertEqual(updated_note.content, 'Updated details of note')

        # Check redirection
        self.assertEqual(response.status_code, 302)


class NoteDeleteTest(TestCase):
    # Define note creation function
    def setUp(self):
        # Create note for deletion
        self.sticky_note = Note.objects.create(
            title='Note to delete',
            content='Content that will be deleted'
        )

    # Define function to test deletion
    def test_delete_sticky_note(self):
        # Call function to delete note
        response = self.client.get(
                    reverse('note_delete', args=[self.sticky_note.id]))
        # Check note is deleted
        self.assertEqual(Note.objects.count(), 0)
        # Check note doesn't exist
        self.assertFalse(
            Note.objects.filter(id=self.sticky_note.id).exists()
        )
        # Checks redirect
        self.assertEqual(response.status_code, 302)
