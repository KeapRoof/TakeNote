import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Inject, Injectable, PLATFORM_ID } from '@angular/core';
import { CreateResponse } from '../interfaces/loginInterfaces';
import { BACK_PATH } from '../const/noteConst';
import { catchError, shareReplay } from 'rxjs/operators';
import { throwError } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private token: string | null = null;

  constructor(
    private http: HttpClient,
    @Inject(PLATFORM_ID) private platformId: object
  ) {}

  login(email: string, password: string) {
    return this.http
      .post<{ access_token: string; token_type: string }>(
        'http://localhost:8000/api/login',
        { email, password }
      )
      .pipe(
        shareReplay(),
        catchError((error: HttpErrorResponse) => {
          console.error('Login request failed', error);
          return throwError(
            () => new Error('Login failed; please try again later.')
          );
        })
      );
  }

  signup(email: string, password: string, username: string) {
    return this.http
      .post<CreateResponse>(`${BACK_PATH}/signup`, {
        email,
        password,
        username,
      })
      .pipe(
        catchError((error: HttpErrorResponse) => {
          return throwError(() => error);
        }),
        shareReplay()
      );
  }

  // Stockage du token dans le localStorage ou sessionStorage
  storeToken(token: string): void {
    localStorage.setItem('access_token', token);
  }

  // Récupération du token
  getToken(): string | null {
    return localStorage.getItem('access_token');
  }

  // Méthode pour vérifier si le token existe
  isAuthenticated(): boolean {
    return this.getToken() !== null;
  }
}
