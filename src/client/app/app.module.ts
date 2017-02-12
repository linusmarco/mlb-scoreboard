import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { routing } from './core/app.routes';
import { AppComponent } from './core/app.component';
import { NavComponent } from './nav/my-nav.component';
import { TestComponent1 } from './test-component-1/test-component-1.component';
import { TestComponent2 } from './test-component-2/test-component-2.component';
import { TestResource } from './services/test-service.service';

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
        TestComponent1,
        TestComponent2
    ],
    providers: [
        TestResource
    ],
    bootstrap: [AppComponent]
})
export class AppModule { }