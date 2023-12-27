import {Component, OnInit} from '@angular/core';
import {CourseService} from "../../core/services/course.service";
import {ActivatedRoute, Router} from "@angular/router";
import {IAnswers, ICategory} from "../../core/interfaces/course-page.interface";
import {DomSanitizer} from "@angular/platform-browser";
import {Location} from "@angular/common";

@Component({
  selector: 'app-theme',
  templateUrl: './theme.component.html',
  styleUrls: ['./theme.component.scss']
})
export class ThemeComponent implements OnInit{
  isVideoVisible: boolean = false;
  isThemeVisible: boolean = true;
  isQuestionVisible: boolean = false;
  isAlertVisible: boolean = false;

  themeId: number;
  themes: ICategory;

  themeDescription: any;

  selectedAnswers: { [questionId: number]: number } = {};
  correctAnswers: number = 0;
  score: number;

  constructor(
    private _courseService: CourseService,
    private _activatedRoute: ActivatedRoute,
    private sanitizer: DomSanitizer,
    private _location: Location
  ) {}

  ngOnInit(): void {
    this.themeId = +this._activatedRoute.snapshot.params['themeId'];

    if (this.themeId) {
      this.getCurrentTheme(this.themeId);
    }
  }

  getCurrentTheme(themeId: number): void {
    this._courseService.getCurrentTheme(themeId).subscribe({
      next: res => {
        this.themes = res;
        this.themeDescription = this.sanitizer.bypassSecurityTrustHtml(res.description);
        console.log(this.themes)
      }
    })
  }

  changeBlock(block: string): void {
    this.isThemeVisible = false;
    this.isVideoVisible = false;
    this.isQuestionVisible = false;

    if (block === 'Тема') {
      this.isThemeVisible = true;
    }

    if (block === 'Видео') {
      this.isVideoVisible = true;
    }

    if (block === 'Тест') {
      this.isQuestionVisible = true;
    }
  }

  submit(): void {
    this.isAlertVisible = true;

    for (const question of this.themes.questions) {
      const selectedAnswerId = this.selectedAnswers[question.id];
      const selectedAnswer = question.answers.find(answer => answer.id === selectedAnswerId);

      if (selectedAnswer && selectedAnswer.is_correct) {
        this.correctAnswers++;
      }
    }

    const totalQuestions = this.themes.questions.length;
    this.score = (this.correctAnswers / totalQuestions) * 10;

    console.log(`Количество правильных ответов: ${this.correctAnswers}`);
    console.log(`Баллы: ${this.score}`);

    this._courseService.pathCurrentTheme(this.themeId, true).subscribe({
      next: (res) => {
        this.themes.is_passed = true;
      }
    });

    this._courseService.postCorrectAnswer(this.correctAnswers, this.score, this.themeId).subscribe({
      next: (res) => {
        console.log('все окей')
      },
      error: (err) => {
        // Обработка ошибки, если она возникнет при отправке запроса
      }
    });

    setTimeout(() => {
      this.isAlertVisible = false;
      this._location.back();
    }, 15000);
  }

  getCorrectAnswersText(correctAnswers: number, totalQuestions: number): string {
    if (totalQuestions === 10) {
      return 'Отлично! Вы ответили на все вопросы';
    } else if (correctAnswers === 1) {
      return 'Вы правильно ответили на 1 вопрос';
    } else if (correctAnswers > 1 && correctAnswers < 5) {
      return `Вы правильно ответили на ${correctAnswers} вопроса`;
    } else {
      return `Вы правильно ответили на ${correctAnswers} вопросов`;
    }
  }

  protected readonly alert = alert;
}
