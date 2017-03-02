import { Component, OnInit, OnDestroy } from "@angular/core";
import { ActivatedRoute } from '@angular/router';

import { GamesService } from "../services/games.service";

@Component({
    templateUrl: 'scoreboard.component.html',
    styleUrls: ['scoreboard.component.css'],
    moduleId: module.id
})

export class ScoreboardComponent implements OnInit, OnDestroy {
    date: any;
    games: any[];
    ready: boolean = false;
    subscriptions = [];

    constructor(private _gamesService: GamesService,
                private _route: ActivatedRoute) { }

    ngOnInit(): void {
        this.subscriptions.push(this._route.params.subscribe(params => {
            let getDate;
            let reqDate = params['date'];
            if (reqDate === "today") {
                getDate = "20160404";
            } 
            else {
                getDate = reqDate;
            }
            this.date = this._gamesService.parseDate(getDate);
            this.updateDate(this.date);
        }));
    }

    updateDate(): void {
        this.ready = false;
        this._gamesService.getGamesByDate(this._gamesService.unparseDate(this.date)).then(d => {
            this.games = d;
            this.ready = true;
        });
    }

    ngOnDestroy(): void {
        this.subscriptions.forEach(x => {
            x.unsubscribe();
        });
    }
}