import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { routing } from './core/app.routes';
import { AppComponent } from './core/app.component';
import { NavComponent } from './nav/my-nav.component';
import { ScoreboardComponent } from './scoreboard/scoreboard.component';
import { LineScoreComponent } from './linescore/linescore.component';
import { GamesService } from './services/games.service';

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
        ScoreboardComponent,
        LineScoreComponent
    ],
    providers: [
        GamesService
    ],
    bootstrap: [AppComponent]
})
export class AppModule { }