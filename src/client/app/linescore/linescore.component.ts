import { Component, Input } from "@angular/core";

@Component({
    selector: 'linescore',
    templateUrl: 'linescore.component.html',
    styleUrls: ['linescore.component.css'],
    moduleId: module.id
})

export class LineScoreComponent {
    @Input() game:string;
}