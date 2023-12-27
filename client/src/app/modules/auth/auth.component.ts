import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms'
import { AuthService } from 'src/app/core/services/auth.service';
import {Router} from "@angular/router";

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.scss']
})
export class AuthComponent implements OnInit {
  form: FormGroup;
  emailValue: string;
  passwordValue: string;
  errorMessageResponse: string;

  constructor(
    private _formBuilder: FormBuilder,
    private _authService: AuthService,
    private _router: Router
    ) { }

  ngOnInit(): void {
    this._createForm();
  }

  onSubmit() {
    const dataRequest = {
      email: this.emailValue,
      password: this.passwordValue
    }
    console.log(dataRequest)

    this._authService.auth(dataRequest).subscribe({
      next: res => {
        console.log(res);
        localStorage.setItem('token', res.auth_token);
        this._router.navigate(['']);
        this.form.reset();
      },
      error: err => {
        console.log(err);
        this.errorMessageResponse = err.err.email;
      }
    })
  }

  private _createForm() {
    this.form = this._formBuilder.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required]
    })
  }
}
