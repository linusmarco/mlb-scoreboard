import { Routes, RouterModule } from '@angular/router';
import { ModuleWithProviders } from '@angular/core';
import { TestComponent } from '../test-component/test-component.component';

const appRoutes: Routes = [
    {
        path: '',
        redirectTo: 'app/test',
        pathMatch: 'full'
    },
    {
        path: 'app/test',
        component: TestComponent
    },
    { 
        path: '**', 
        redirectTo: 'app/test',
        pathMatch: 'full'
    } 
];

export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes);