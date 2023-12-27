export interface ICoursePage {
  id: number,
  title: string,
  description: string
}

export interface ICourse {
  count: number,
  next: number,
  previous: number,
  results: ICourseTheme[]
}

export interface ICourseTheme {
  count: number,
  next: number,
  previous: number,
  results: ICategory[]
}

export interface ICategory {
  id: number,
  title: string,
  short_description: string,
  description: string,
  video: string,
  time_course: number,
  is_passed: boolean,
  questions: IQuestions[]
}

export interface IQuestions {
  id: number,
  text: string,
  answers: IAnswers[]
}

export interface IAnswers {
  id: number,
  is_correct: boolean,
  text: string
}
