import { OnInit } from '@angular/core'
import { Component } from '@angular/core';
import { Validators } from '@angular/forms'
import { FormBuilder, FormGroup } from '@angular/forms'
import { IInputFieldInterface } from 'src/app/core/interfaces/inputField.interface'

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
      fieldPlaceholder: 'Имя'
    },
    {
      fieldType: 'text',
      fieldControl: 'surname',
      fieldPlaceholder: 'Фамилия'
    },
    {
      fieldType: 'email',
      fieldControl: 'email',
      fieldPlaceholder: 'Почта'
    },
    {
      fieldType: 'password',
      fieldControl: 'password',
      fieldPlaceholder: 'Пароль'
    },
    {
      fieldType: 'password',
      fieldControl: 'repeatPassword',
      fieldPlaceholder: 'Повторите пароль'
    }
  ];
  form: FormGroup;
  passwordControl: string;
  repeatPassword: string;

  constructor(
    private _formBuilder: FormBuilder
  ) {}

  ngOnInit(): void {
    this._createForm();
    console.log(this.form)
  }

  onSubmit() {
    if (this.form.valid) {
      this.passwordControl = this.form.get('password').value;
      this.repeatPassword = this.form.get('repeatPassword').value;
      if (this.passwordControl !== this.repeatPassword) {
        console.log('no');
        this.form.setErrors({ matchPassword: true });
      } else {
        console.log('ok');
        console.log(this.form);
        this.form.reset();
      }
    }
  }

  private _createForm() {
    this.form = this._formBuilder.group({
      name: ['', Validators.required],
      surname: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required],
      repeatPassword: ['', Validators.required],
    })
  }
}
