import { Component } from '@angular/core';
import { Note } from '../../../interfaces/note';
import { NotesService } from '../../../services/notes.service';
import { SideListItemNoteComponent } from '../side-list-item-note/side-list-item-note.component';

@Component({
  selector: 'app-side-list-note',
  standalone: true,
  imports: [SideListItemNoteComponent],
  templateUrl: './side-list-note.component.html',
  styleUrls: ['./side-list-note.component.css'],
})
export class SideListNoteComponent {
  notesList: Note[] = []; // Initialiser le tableau

  constructor(private notesService: NotesService) {
    // Souscrire à l'Observable pour obtenir la liste des notes
    this.notesService.fetchNotesList().subscribe((notes) => {
      this.notesList = notes;
    });
  }

  onNoteClicked(id: number) {
    this.notesService.setSelectedNoteId(id);
  }

  onAddClick(){
    this.notesService.createNote()
    .subscribe(() => {
      this.notesList.push();
      window.location.reload();
    });
  }

  onDeleteClick(id: number) {
    this.notesService.deleteNote(id).subscribe(
      () => {
        this.notesList = this.notesList.filter(note => note.note_id !== id);
      },
      (error) => {
        console.error('Erreur lors de la suppression de la note', error);
      }
    );
  }
}

