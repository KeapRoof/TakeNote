import { Injectable } from '@angular/core';
import {
  HttpClient,
  HttpHeaders,
  HttpErrorResponse,
} from '@angular/common/http';
import { BehaviorSubject, Observable, switchMap, throwError } from 'rxjs';
import { Note } from '../interfaces/note';
import { AuthService } from './auth-service.service';

@Injectable({
  providedIn: 'root',
})
export class NotesService {
  private selectedNoteId$ = new BehaviorSubject<number | null>(null);

  selectedNote$: Observable<Note> = this.selectedNoteId$.pipe(
    switchMap((noteId) => {
      if (noteId || noteId === 0) {
        return this.fetchNoteContent(noteId);
      } else {
        return new Observable<Note>((subscriber) =>
          subscriber.next(null as any)
        );
      }
    })
  );

  constructor(private http: HttpClient, private authService: AuthService) {}

  setSelectedNoteId(newId: number) {
    this.selectedNoteId$.next(newId);
  }

  private getAuthHeaders() {
    const token = this.authService.getToken();
    if (!token) {
      throw new Error('Token non trouvé. Veuillez vous reconnecter.');
    }
    return new HttpHeaders({
      Authorization: `Bearer ${token}`,
    });
  }

  fetchNotesList(): Observable<Note[]> {
    return this.http.get<Note[]>('http://localhost:8000/api/notes', {
      headers: this.getAuthHeaders(),
    });
  }

  fetchNoteContent(idnote: number): Observable<Note> {
    return this.http.get<Note>(`http://localhost:8000/api/note/${idnote}`, {
      headers: this.getAuthHeaders(),
    });
  }

  createNote() {
    return this.http.post<string>(
      'http://localhost:8000/api/note',
      {},
      {
        headers: this.getAuthHeaders(),
      }
    );
  }

  deleteNote(id: number) {
    return this.http.delete(`http://localhost:8000/api/note/${id}`, {
      headers: this.getAuthHeaders(),
    });
  }

  saveNote(note: any, id: number): Observable<any> {
    const url = `http://localhost:8000/api/note/${id}`; // ID de la note à mettre à jour
    const body = {
      note_name: note.note_name,
      note_content: note.note_content,
    };
    return this.http.put(url, body, { headers: this.getAuthHeaders() });
  }

  private handleError(error: HttpErrorResponse) {
    if (error.status === 401) {
      console.error('Non autorisé, le token est invalide ou expiré.');
    } else {
      console.error("Une erreur s'est produite:", error.message);
    }
    return throwError(
      () =>
        new Error("Une erreur s'est produite. Veuillez réessayer plus tard.")
    );
  }
}
