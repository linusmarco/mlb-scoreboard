import { Component, OnInit } from "@angular/core";
import { TestResource } from "../services/test-service.service";

@Component({
    templateUrl: 'test-component-1.component.html',
    styleUrls: ['test-component-1.component.css'],
    moduleId: module.id
})

export class TestComponent1 implements OnInit {
    data: any[];
    ready: boolean = false;

    constructor(private _testResource: TestResource) { }

    ngOnInit() {
        this._testResource.getData().then(d => {
            this.data = d;
            this.ready = true;
        });
    }
}