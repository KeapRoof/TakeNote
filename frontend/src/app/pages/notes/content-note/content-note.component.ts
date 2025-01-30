import { AsyncPipe } from '@angular/common';
import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { Note } from '../../../interfaces/note';
import { NotesService } from '../../../services/notes.service';
import {FormsModule} from "@angular/forms";

@Component({
  selector: 'app-content-note',
  standalone: true,
  imports: [AsyncPipe, FormsModule],
  templateUrl: './content-note.component.html',
  styleUrl: './content-note.component.css',
})
export class ContentNoteComponent {
  selectedNote$: Observable<Note>;
  editableNote: Note = { note_id: -1, note_name: '', note_content: '' };


  constructor(private notesService: NotesService) {
    this.selectedNote$ = this.notesService.selectedNote$;
  }


  ngOnInit() {
    // Vérification de l'émission
    this.selectedNote$.subscribe(note => {
      if (note){
        this.editableNote = {...note}
      }
    });
  }

  onSaveClick(){
    if (this.editableNote.note_id) {
      // Appel du service pour sauvegarder les modifications
      this.notesService.saveNote(this.editableNote,this.editableNote.note_id).subscribe({
        next: () => {
          window.location.reload();
        },
        error: (error) => {
          console.error('Erreur lors de la sauvegarde de la note:', error);
        }
      });
    } else {
      console.error("Erreur : L'ID de la note est manquant.");
    }
  }


}
