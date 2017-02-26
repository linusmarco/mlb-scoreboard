# mlb-scoreboard

## IN DEVELOPMENT -- NOT WORKING YET


### Work Plan

#### Version 0.1.0
- [x] Set up database
    + [x] Initialization script
    + [x] Teardown script
- [x] Load historical game log data (Retrosheet)
    + Start with 2016 only
- [x] API to serve data
- [ ] View to display games by day
    + [ ] Day view
    + [ ] Games service

#### Version 0.2.0
- [ ] Tests

#### Version 0.X.X
- [ ] Load more historical data
- [ ] More tests

#### Version 1.0.0
- [ ] Acquire domain
- [ ] Acquire hosting
- [ ] Write deployment scripts
- [ ] Deploy

#### Version 2.0.0
- [ ] Integrate with MLB Gameday API
    + [ ] Navigate Gameday TOS
    + [ ] Script to load into DB 
    + [ ] Integrate streaming data for live updating

#### Version 3.0.0
- [ ] Add game detail view
    + [ ] Scripts to load historical and live data into DB
    + [ ] Game view

#### Version X.X.X (Aspirational)
- [ ] Player views
- [ ] Add pitch f/x data 
- [ ] Links to game stories for historical games
- [ ] Links to MLB.TV for live games


### Getting the app running
After cloning the repo, run the following commands to get the app running:

(From `src/client`)
```
npm install
npm run gulp
npm start
```

(From `src/server`)
```
python run.py
```