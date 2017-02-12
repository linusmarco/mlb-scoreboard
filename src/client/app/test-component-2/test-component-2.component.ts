import { Component, OnInit } from "@angular/core";
import { TestResource } from "../services/test-service.service";

@Component({
    templateUrl: 'test-component-2.component.html',
    styleUrls: ['test-component-2.component.css'],
    moduleId: module.id
})

export class TestComponent2 implements OnInit {
    datum: any[];
    ready: boolean = false;

    constructor(private _testResource: TestResource) { }

    ngOnInit() {
        this._testResource.getDatum(2).then(d => {
            this.datum = d;
            this.ready = true;
        });
    }
}