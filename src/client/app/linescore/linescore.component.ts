import { Component, OnInit } from "@angular/core";
import { GamesService } from "../services/games.service";

@Component({
    templateUrl: 'linescore.component.html',
    styleUrls: ['linescore.component.css'],
    moduleId: module.id
})

export class LineScoreComponent implements OnInit {
    datum: any[];
    ready: boolean = false;

    constructor(private _gamesService: GamesService) { }

    ngOnInit() {
        this._gamesService.getGamesByDate("18710504").then(d => {
            this.datum = d;
            this.ready = true;
        });
    }
}