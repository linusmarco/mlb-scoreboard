import { Routes, RouterModule } from '@angular/router';
import { ModuleWithProviders } from '@angular/core';
import { TestComponent1 } from '../test-component-1/test-component-1.component';
import { TestComponent2 } from '../test-component-2/test-component-2.component';

const appRoutes: Routes = [
    {
        path: '',
        redirectTo: 'app/component1',
        pathMatch: 'full'
    },
    {
        path: 'app/component1',
        component: TestComponent1
    },
    {
        path: 'app/component2',
        component: TestComponent2
    },
    { 
        path: '**', 
        redirectTo: 'app/component1',
        pathMatch: 'full'
    } 
];

export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes);