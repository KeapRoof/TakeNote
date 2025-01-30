import { Routes } from '@angular/router';
import { ConnectionComponent } from './pages/connection/connection.component';
import { SignupComponent } from './pages/signup/signup.component';
import { NotePageComponent } from './pages/notes/note-page/note-page.component';

export const routes: Routes = [
  { path: 'login', component: ConnectionComponent },
  { path: 'signup', component: SignupComponent },
  { path: 'notes', component: NotePageComponent },
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  { path: '**', redirectTo: '/notes', pathMatch: 'full' },
]