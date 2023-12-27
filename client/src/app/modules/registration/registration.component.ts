import { OnInit } from '@angular/core'
import { Component } from '@angular/core';
import { Validators } from '@angular/forms'
import { FormBuilder, FormGroup } from '@angular/forms'
import { Router } from '@angular/router';
import { IInputFieldInterface } from 'src/app/core/interfaces/inputField.interface'
import { AuthService } from 'src/app/core/services/auth.service'

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.scss']
})
export class RegistrationComponent implements OnInit {
  inputFields: IInputFieldInterface[] = [
    {
      fieldType: 'text',
      fieldControl: 'name',
      fieldPlaceholder: 'Имя',
      filedValue: ''
    },
    {
      fieldType: 'text',
      fieldControl: 'surname',
      fieldPlaceholder: 'Фамилия',
      filedValue: ''
    },
    {
      fieldType: 'email',
      fieldControl: 'email',
      fieldPlaceholder: 'Почта',
      filedValue: ''
    },
    {
      fieldType: 'password',
      fieldControl: 'password',
      fieldPlaceholder: 'Пароль',
      filedValue: ''
    },
    {
      fieldType: 'password',
      fieldControl: 'repeat_password',
      fieldPlaceholder: 'Повторите пароль',
      filedValue: ''
    }
  ];
  form: FormGroup;
  passwordControl: string;
  repeatPasswordControl: string;
  errorMessageResponse: string;

  constructor(
    private _formBuilder: FormBuilder,
    private _auth: AuthService,
    private _route: Router
  ) {}

  ngOnInit(): void {
    this._createForm();
  }

  onSubmit() {
    const [name, surname, email, password, repeat_password] = this.inputFields.map(filed => filed.filedValue)
    if (this.form.valid) {
      this.passwordControl = this.form.get('password').value;
      this.repeatPasswordControl = this.form.get('repeat_password').value;
      if (this.passwordControl !== this.repeatPasswordControl) {
        this.form.setErrors({ matchPassword: true });
      } else {
        this.form.reset();
      }
    }
    const dataRequest = {
      name,
      surname,
      email,
      password,
      repeat_password
    }
    this._auth.registration(dataRequest).subscribe({
      next: (res) => {
        console.log("Успех", res);
        this._route.navigate(['/auth'])
      },
      error: (error) => {
        console.log(error)
        this.errorMessageResponse = error.error.email;
      }
    });
  }

  private _createForm() {
    this.form = this._formBuilder.group({
      name: ['', Validators.required],
      surname: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required],
      repeat_password: ['', Validators.required],
    })
  }
}
