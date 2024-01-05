import {Component, OnInit} from '@angular/core';
import { ICoursePage } from 'src/app/core/interfaces/course-page.interface';
import {CourseService} from "../../core/services/course.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-course-page',
  templateUrl: './course-page.component.html',
  styleUrls: ['./course-page.component.scss']
})
export class CoursePageComponent implements OnInit{
  coursePages: ICoursePage[] = [];
  token: string =  localStorage.getItem('token')
  name: string = localStorage.getItem('name');

  constructor(
    private _courseService: CourseService,
    private _router: Router
  ) { }

  ngOnInit(): void {
    this.getCourse();
    if (!this.token && !this.name) {
      this._router.navigate(['/auth']);
    }
  }

  getCourse(): void {
    this._courseService.getCourse().subscribe({
      next: (res:  ICoursePage[]): void => {
        this.coursePages = res;
        console.log(res);
      }
    });

    this._courseService.getMe(this.token).subscribe({
      next: res => {
        localStorage.setItem('name', res.name);
      }
    })
  }

  logout(): void {
    localStorage.removeItem('token');
    localStorage.removeItem('name');
    this._router.navigate(['/auth']);
  }

  protected readonly localStorage = localStorage;
}
