import { Component, OnInit, OnDestroy } from "@angular/core";
import { ActivatedRoute }   from '@angular/router';

import { GamesService } from "../services/games.service";

@Component({
    templateUrl: 'scoreboard.component.html',
    styleUrls: ['scoreboard.component.css'],
    moduleId: module.id
})

export class ScoreboardComponent implements OnInit {
    date: any;
    games: any[];
    ready: boolean = false;

    constructor(private _gamesService: GamesService,
                private _route: ActivatedRoute) { }

    ngOnInit() {
        let subscr = this._route.params.subscribe(params => {
            let getDate;
            let reqDate = params['date'];
            if (reqDate === "today") {
                getDate = "20160404";
            } 
            else {
                getDate = reqDate;
            }
            this.date = this._gamesService.parseDate(getDate);
            this._gamesService.getGamesByDate(getDate).then(d => {
                this.games = d;
                this.ready = true;
                subscr.unsubscribe();
            });
        });
    }
}