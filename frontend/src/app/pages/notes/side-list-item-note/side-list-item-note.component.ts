import { Component, Input } from '@angular/core';
import { Note } from '../../../interfaces/note';
import { SlicePipe } from '@angular/common';

@Component({
  selector: 'app-side-list-item-note',
  standalone: true,
  imports: [SlicePipe],
  templateUrl: './side-list-item-note.component.html',
  styleUrl: './side-list-item-note.component.css',
})
export class SideListItemNoteComponent {
  @Input({ required: true })
  note!: Note;
}
