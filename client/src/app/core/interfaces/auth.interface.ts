export interface IRegistration {
  name: string,
  surname: string,
  email: string,
  password: string,
  repeatPassword: string
}

export interface IRegResponse {
  id: number,
  name: string,
  surname: string,
  email: string,
  password: string,
  repeatPassword: string
}

export interface IAuthRequest {
  email: string,
  password: string
}

export interface IAuthResponse {
}
