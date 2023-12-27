import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RegistrationComponent } from './modules/registration/registration.component'
import { AuthComponent } from './modules/auth/auth.component'
import { CoursePageComponent } from './modules/course-page/course-page.component';
import { CourseComponent } from './modules/course/course.component';
import { ThemeComponent } from './modules/theme/theme.component';

const routes: Routes = [
  {
    path: '',
    redirectTo: '/course-page',
    pathMatch: 'full'
  },
  {
    path: 'registration',
    component: RegistrationComponent
  },
  {
    path: 'auth',
    component: AuthComponent
  },
  {
    path: 'course-page',
    component: CoursePageComponent
  },
  {
    path: 'course/:courseId',
    component: CourseComponent
  },
  {
    path: 'theme/:themeId',
    component: ThemeComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
