import { Component, OnInit } from '@angular/core';
import {
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { AuthService } from '../../services/auth-service.service';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-signup',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule],
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css'],
})
export class SignupComponent {
  form: FormGroup;
  errorMessage: string | null = null;

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private router: Router
  ) {
    this.form = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required],
      username: ['', Validators.required],
    });
  }

  signup() {
    if (this.form.valid) {
      const val = this.form.value;
      this.authService.signup(val.email, val.password, val.username).subscribe({
        next: () => {
          alert('Inscription réussie ! Connectez-vous.');
          this.errorMessage = null;
          this.router.navigate(['/login']);
        },
        error: (error) => {
          if (error.status === 400) {
            this.errorMessage = error.error.detail;
          } else {
            this.errorMessage =
              'Une erreur inattendue est survenue. Veuillez réessayer.';
          }
        },
      });
    }
  }

  navigateToLogin() {
    this.router.navigate(['/login']);
  }
}
