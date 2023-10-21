import { IAuthRequest, IAuthResponse, IRegistration, IRegResponse } from './../interfaces/auth.interface';
import { HttpClient } from '@angular/common/http'
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment as env } from 'src/environments/environments';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(
    private _http: HttpClient
  ) { }

  registration(regData: IRegistration): Observable<IRegResponse> {
    return this._http.post<IRegResponse>(`${env.apiUrl}/${env.api.register}/`, regData)
  }

  auth(authData : IAuthRequest): Observable<IAuthResponse> {
    return this._http.post<IAuthResponse>(`${env.apiUrl}/${env.api.auth}/`, authData)
  }
}
