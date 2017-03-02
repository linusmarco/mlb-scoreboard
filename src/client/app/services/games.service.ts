import { Injectable } from '@angular/core';
import { Http, Headers, Response, RequestOptions } from '@angular/http';
import 'rxjs/add/operator/toPromise';

@Injectable()
export class GamesService {
    constructor(private _http: Http) { }

    private handleError(error: any) {
        return Promise.reject(error.message || error);
    };

    public getGamesByDate(date:string): Promise<any[]> {
        return this._http.get('api/games/date/' + date)
            .toPromise()
            .then(response => response.json() as any[])
            //.catch(this.handleError);
            .catch(reason => []);
    };

    public parseDate(date:string): any {
        return {
            day: date.substr(6,2),
            month: date.substr(4,2),
            year: date.substr(0,4)
        }
    };

    public unparseDate(date:any): string {
        let str = date.year.toString();
        str += ("0" + date.month).substr(-2,2);
        str += ("0" + date.day).substr(-2,2);
        return str;
    };
}
