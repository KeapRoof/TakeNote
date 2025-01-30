import { Component } from '@angular/core';
import {
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth-service.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-connection',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule],
  providers: [AuthService],
  templateUrl: './connection.component.html',
  styleUrls: ['./connection.component.css'],
})
export class ConnectionComponent {
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
    });
  }

  login() {
    const val = this.form.value;
    if (this.form.valid) {
      this.authService.login(val.email, val.password).subscribe({
        next: (response) => {
          this.authService.storeToken(response.access_token);
          this.router.navigateByUrl('/notes');
        },
        error: (err) => {
          console.error('Login failed', err);
          this.errorMessage = 'Email ou mot de passe incorrect';
        },
      });
    }
  }

  navigateToSignup() {
    this.router.navigate(['/signup']);
  }
}
