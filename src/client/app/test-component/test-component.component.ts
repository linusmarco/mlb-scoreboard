import { Component } from "@angular/core";

@Component({
    templateUrl: 'test-component.component.html',
    styleUrls: ['test-component.component.css'],
    moduleId: module.id
})

export class TestComponent {
    text = "THIS IS A TEST";
}