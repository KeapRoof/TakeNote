import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ContentNoteComponent } from '../content-note/content-note.component';
import { SideListNoteComponent } from '../side-list-note/side-list-note.component';

@Component({
  selector: 'app-note-page',
  standalone: true,
  imports: [RouterOutlet, ContentNoteComponent, SideListNoteComponent],
  templateUrl: './note-page.component.html',
  styleUrl: './note-page.component.css',
})
export class NotePageComponent {}
