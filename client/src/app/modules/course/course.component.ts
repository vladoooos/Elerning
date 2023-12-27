import {Component, OnInit} from '@angular/core';
import {ICategory, ICoursePage, ICourseTheme} from 'src/app/core/interfaces/course-page.interface';
import {CourseService} from "../../core/services/course.service";
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'app-course',
  templateUrl: './course.component.html',
  styleUrls: ['./course.component.scss']
})
export class CourseComponent implements OnInit{
  courses: ICategory[] = [];

  coursePage: ICoursePage;

  courseId: number;

  constructor(
    private _courseService: CourseService,
    private _activatedRoute: ActivatedRoute
  ) {}

  ngOnInit(): void {
    this.courseId = +this._activatedRoute.snapshot.params['courseId'];

    if (this.courseId) {
      this.getCourse(this.courseId);
      this.getTheme(this.courseId);
    }
  }

  getCourse(courseId: number): void {
    this._courseService.getCourse().subscribe({
      next: (res: ICoursePage[]): void => {
        this.coursePage = res.find(course => course.id === courseId);
      }
    })
  }

  getTheme(courseId: number): void {
    this._courseService.getTheme(courseId).subscribe({
      next: (res: ICourseTheme) => {
        this.courses = res.results;
        console.log(this.courses)
      }
    })
  }
}
