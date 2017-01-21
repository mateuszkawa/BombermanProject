# Bomberman
###### Server (API) - Documentation

## 1 Introduction
This document describe API of the Bomberman AI focused game.

## 2 Communication Design
Let's take a look at possible communication scenarios.

### 2.1 Client Registration
Before game can start all users have to register by sending proper message to server. Server sets some unique userID for a client (identification purposes).

![Client Registration](https://raw.githubusercontent.com/mateuszkawa/BombermanProject/master/Documentation/resources/registration_flow.png)

### 2.2 Common Round
Client should always have the newest state. that's why all clients must have some way of getting such a information. Server should answear with such a state and also add a time for next state calculation. I am thinking for something like 200ms periods between calculation, we can change it to smaller periods or even "live".

![Common Round](https://raw.githubusercontent.com/mateuszkawa/BombermanProject/master/Documentation/resources/client_server_flow.png)

## 3 Game Rules
Players are fighting, by placing bombs, on a rectangle map. Map should be generated after all users successful registration. Map requirements for classic mode:

* For every user at least one combination of moves should be possible: (MOVE_UP, MOVE_RIGHT), (MOVE_UP, MOVE_LEFT), (MOVE_DOWN, MOVE_RIGHT), (MOVE_DOWN, MOVE_LEFT). This allows player to have a free tile to place a bomb;
* At every odd number of column and and row (for example: (1,1)) field_type is set as INDESTRUCTIBLE;
* There should be at least 30% of DESTRUCTIBLE tiles;
* Every DESTRUCTIBLE should have 20% of chance to drop an UPGRADE;

Every player starts with 1 bomb. Placed bomb explodes after 4 turns and default radius is 3. Explosion effects:

* Kills players on it's road;
* Destroys DESTRUCTIBLE tiles;
* Destroys upgrades;
* Indicates Explosion of other bombs that are on the road;
* Stays one round on a map, after that flames dissapears. They are not contained in a state, becouse there is no possibility to step on an explosion.

## 4 Messages
### 4.1 Registration Message
Client message:

Field Name | Type | Required | Short Description
---- | ---- | ---- | ----
user_name | TEXT | Y | Name of a bot should be provided

Fields Definition:
* user_name – This name would be used for scoring, state etc. Purposes.

Examlpe Message:
```javascript
{
	'user_name': 'Example_bot_1'
}
```
Server response:

Field Name | Type | Required | Short Description
---- | ---- | ---- | ----
user_id | TEXT | Y | Unique Id set by the server for identification purposes.
time_left | LONG | Y | Time left in miliseconds for this particular phase (registration).

Fields Definition:
* user_id – This Id is required for simple authentication. Can be for example MD5 with added random seed counted from provided user name.
* time_left – This is number of miliseconds that's left in order to finish this part of server state.

Example Message:
```javascript
{
	'user_id': 'a687346006dd2d95cf33d10cf10b2a9d',
	'time_left': 10000
}
```


