import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { routing } from './core/app.routes';
import { AppComponent } from './core/app.component';
import { NavComponent } from './nav/my-nav.component';
import { TestComponent } from './test-component/test-component.component';

@NgModule({
    imports: [
        BrowserModule,
        FormsModule,
        ReactiveFormsModule,
        HttpModule,
        routing
    ],
    declarations: [
        AppComponent,
        NavComponent,
        TestComponent
    ],
    providers: [
        
    ],
    bootstrap: [AppComponent]
})
export class AppModule { }