import { Injectable } from '@angular/core';
import {environment} from "../../../environments/environments";
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";
import {ICategory, ICoursePage, ICourseTheme} from "../interfaces/course-page.interface";

@Injectable({
  providedIn: 'root'
})
export class CourseService {

  private env = environment;
  constructor(private _http: HttpClient) { }

  public getCourse(): Observable<ICoursePage[]> {
    return this._http.get<ICoursePage[]>(`${this.env.apiUrl}/${this.env.api.block}/`);
  }

  public getTheme(courseId: number): Observable<ICourseTheme> {
    return this._http.get<ICourseTheme>(`${this.env.apiUrl}/${this.env.api.course}/?category=${courseId}`);
  }

  public getCurrentTheme(themeId: number): Observable<ICategory> {
    return this._http.get<ICategory>(`${this.env.apiUrl}/${this.env.api.course}/${themeId}/`);
  }

  public pathCurrentTheme(themeId: number, isPassed: boolean): Observable<ICategory> {
    return this._http.patch<ICategory>(
      `${this.env.apiUrl}/${this.env.api.course}/${themeId}/`,
      { is_passed: isPassed } // Передача значения is_passed в объекте запроса
    );
  }

  public getMe(Authorization: string): Observable<any> {
    const headers = new HttpHeaders({
      'Authorization': `Token ${Authorization}`
    });

    return this._http.get(
      `${this.env.apiUrl}/${this.env.api.auth}/${this.env.api.users}/${this.env.api.me}/`,
      { headers: headers }
    );
  }

  public postCorrectAnswer(correctAnswers: number, score: number, course: number): Observable<any> {
    const data = { correct_answers: correctAnswers, score: score, course: course };

    return this._http.post(
      `${this.env.apiUrl}/${this.env.api.auth}/${this.env.api.users}/${this.env.api.me}/`,
      data
    );
  }
}
