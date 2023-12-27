import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AuthComponent } from './modules/auth/auth.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms'
import { RegistrationComponent } from './modules/registration/registration.component'
import { HttpClientModule } from '@angular/common/http';
import { CoursePageComponent } from './modules/course-page/course-page.component';
import { CourseComponent } from './modules/course/course.component';
import { ThemeComponent } from './modules/theme/theme.component'

@NgModule({
  declarations: [
    AppComponent,
    RegistrationComponent,
    AuthComponent,
    CoursePageComponent,
    CourseComponent,
    ThemeComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
