# Duh Legion's Secret Santa
The purpose of this repository is for the Duh Legion Secret Santa project

## Definitive goals are as defined:

### Front-end Goals
- We need a website
  - A Javascript handshake needs to occur for transmitting data to our backend API.
  - ~We need an index page~
  - We need some snazzy flare to it
  - already_registered.html so we can route people here
  - blank page with some Christmas cheer, Avery will do the ServerCode into here
  - *Optional To-Do*
    - Make some stupid memes

___________________
### Back-end Goals

DataBase stuff
- We need to leverage a backend database for PUSHing info off to
    Data Types to be anticipated:
  
      Name  SteamID  IPAddress
      
    *Justification is we need to make sure nobody is being a rude-dude and getting more presents that we anticipate.*
- We need to leverage a backend database for PULLing data from
- All transactions to the Mongo DB will be handled by python queries

_______
Server stuff
- Physical server stuff:
     - MongoDB for database
     - Python Flask server for hosting and API stuff
     - Probably just gonna tag a bounced domain name from actesco

________
Logic Stuff
- Check if we've hit a specific date:

      If we've hit that date, then we're going to check on index load if the user has an ip registered in the database. If they do redirect them to their secret Santa person.

> otherwise check the IP everytime anyways and redirect them to a "already registered" page
