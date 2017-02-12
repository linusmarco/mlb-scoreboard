import { Injectable } from '@angular/core';
import { Http, Headers, Response, RequestOptions } from '@angular/http';
import 'rxjs/add/operator/toPromise';

@Injectable()
export class TestResource {
    constructor(private _http: Http) { }

    public getData(): Promise<any[]> {
        return this._http.get('api/data')
            .toPromise()
            .then(response => response.json() as any[])
            .catch(this.handleError);
    };

    public getDatum(id: number): Promise<any> {
        return this._http.get('api/datum/' + id)
            .toPromise()
            .then(response => response.json() as any)
            .catch(this.handleError);
    };

    protected handleError(error: any) {
        return Promise.reject(error.message || error);
    }

}
