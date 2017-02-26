import { Component, OnInit } from "@angular/core";
import { GamesService } from "../services/games.service";

@Component({
    templateUrl: 'scoreboard.component.html',
    styleUrls: ['scoreboard.component.css'],
    moduleId: module.id
})

export class ScoreboardComponent implements OnInit {
    data: any[];
    ready: boolean = false;

    constructor(private _gamesService: GamesService) { }

    ngOnInit() {
        this._gamesService.getGamesByDate("18710504").then(d => {
            this.data = d;
            this.ready = true;
        });
    }
}