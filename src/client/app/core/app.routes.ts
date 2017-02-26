import { Routes, RouterModule } from '@angular/router';
import { ModuleWithProviders } from '@angular/core';
import { ScoreboardComponent } from '../scoreboard/scoreboard.component';

const appRoutes: Routes = [
    {
        path: '',
        redirectTo: 'app/scoreboard/today',
        pathMatch: 'full'
    },
    {
        path: 'app/scoreboard/:date',
        component: ScoreboardComponent
    },
    { 
        path: '**', 
        redirectTo: 'app/scoreboard/today',
        pathMatch: 'full'
    } 
];

export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes);