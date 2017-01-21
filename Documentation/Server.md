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
* Every DESTRUCTIBLE should have 20% of chance to drop an [UPGRADE](#532-occupied_upgrade);

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

### 4.2 Game Messages
#### 4.2.1 Actual State
Client message:

Field Name | Type | Required | Short Description
---- | ---- | ---- | ----
user_id | TEXT | N | User Id provided by the server
action | TEXT | Y | Action name for getting actual state purposes.

Fields Definition:
* user_id – User Id that was returned from the server for identification purposes. If this filed is provided then server should return actual position of this particular user.
* action – One of the Action Name from action list (take a look at [Actions](#52-actions))

Examlpe Message:
```javascript
{
	'user_id': 'a687346006dd2d95cf33d10cf10b2a9d',
	'action': 'STATE'
}
```
Server response:

Field Name | Type | Required | Short Description
---- | ---- | ---- | ----
actual_state | DICT | Y | Actual map for this round.
state_number | LONG | Y | Actual round.
map_size | TUPLE | Y | Map size height and width
user_position | TUPLE | N | User position
time_left | LONG | Y | Time left in miliseconds for this state.

Fields Definition:
* actual_state – It is a dict that represents actual state. It is further defined in [State Definition](#51-state-definition).
* state_number - Unique round identificator for actual state.
* map_size – 2arg tuple that contains 2 Integer numbers. First one is height of the map and second is width. They are indicating number of fields for example map_size (3, 4) would look like this:

| | | | |
---- | ---- | ---- | ---- | ----
(0,0) | (0,1) | (0,2) | (0,3)
(1,0) | (1,1) | (1,2) | (1,3)
(2,0) | (2,1) | (2,2) | (2,3)

* user_position – Server sends this information only if  user_id was provided. It is position of a specified user returned as a Tuple
* time_left - This is number of miliseconds that's left in order to finish this round.

Examlpe Message:
```javascript
{
	'actual_state': {
		(0, 0): {
			'field_type': 'OCCUPIED_BOMB',
			'bomb_turns_left': 2,
			'bomb_range': 3
		},
		(0, 1): {
			'field_type': 'OCCUPIED_USER',
			'user_name': 'Example_bot_1',
			'bombs_left': 0
		},
		(1, 0): {
			'field_type': 'OCCUPIED_UPGRADE',
			'upgrade_type': 'ADDITIONAL_BOMB'
		},
		(1, 1): {
			'field_type': 'INDESTRUCTIBLE'
		}
	},
	'state_number': 17,
	'map_size': (2, 2),
	'user_position': (1,1),
	'time_left': 190
}
```

#### 4.2.2 User Action
Client message:

Field Name | Type | Required | Short Description
---- | ---- | ---- | ----
user_id | TEXT | Y | User Id provided by the server
action | TEXT | Y | Action name chosen by user.

Fields Definition:
* user_id – User Id that was returned from the server for identification purposes.
* action – One of the Action Name from action list (take a look at [Actions](#52-actions))

Examlpe Message:
```javascript
{
	'user_id': 'a687346006dd2d95cf33d10cf10b2a9d',
	'action': 'MOVE_LEFT'
}
```

Server message:

Field Name | Type | Required | Short Description
---- | ---- | ---- | ----
response | TEXT | Y | User Id provided by the server
information | TEXT | N | Additional information.
actual_state | DICT | N | Actual map for this round.
state_number | LONG | N | Actual round.
time_left | LONG | N | Time left in miliseconds for this state.

Fields Definition:
* response – Response from server. Can contain one of the [Server Responses](#54-server-responses).
* information – Additional informations will be returned for specific responses. 
* actual_state - It is a dict that represents actual state. It is further defined in [State Definition](#51-state-definition).
* state_number - Unique round identificator for actual state.
* time_left – This is number of miliseconds that's left in order to finish this part of server state.

Example Message:
```javascript
{
	'response': 'DECLINED',
	'information': 'DEAD',
	'state_number': 76,
	'time_left': 143
}
```

## 5 Appendix
### 5.1 State Definition
	
Field Name | Type | Required | Short Description
---- | ---- | ---- | ----
field_type | TEXT | Y | [Field type](#53-field-types).
Additional fields depends on [Field type](#53-field-types).

### 5.2 Actions
List of available actions that user can send to server.

Action Name | Description
---- | ----
MOVE_DOWN | Moving character down.
MOVE_LEFT | Moving character left.
MOVE_RIGHT | Moving character
MOVE_UP | Moving character up.
PLACE_BOMB | Placing a bomb.
STATE | Getting actual state from server.

### 5.3 Field Types
List of occurable field types.

Field Type | Description
---- | ----
FREE | Passable terrain. User is able to stand there. 
DESTRUCTIBLE | Destructible terrain. Cannot be moved onto, cen be destructed by bomb's explosion.
INDESTRUCTIBLE | Cannot be stepped or destructed. It blockes the bombs flame.
OCCUPIED_BOMB | Destructible terrain. Has ticking bomb on it.
OCCUPIED_UPGRADE | Free terrain. Some one-time upgrade is placed on it.
OCCUPIED_USER | Free terrain. Player standing on it.

#### 5.3.1 OCCUPIED_BOMB

Field Name | Type | Short Description
---- | ---- | ----
bomb_turns_left | INTEGER | Turns left for a bomb to explode.
bomb_range | INTEGER | Explosion range.

#### 5.3.2 OCCUPIED_UPGRADE

Field Name | Type | Short Description
---- | ---- | ----
upgrade_type | TEXT | One of possible upgrades.

Possible upgrade types:

Upgrade | Short Description
---- | ----
ADDITIONAL_BOMB | Gives Player additional upgrade.
EXPLOSION_RANGE | Gives additional 1 tile of range.

#### 5.3.3 OCCUPIED_USER

Field Name | Type | Short Description
---- | ---- | ----
user_name | TEXT | User name of player that is standing on field.
bombs_left | INTEGER | Number of bombs that this player can place at this round.

### 5.4 Server Responses
Possible server responses on user action.

Response | Returns  Description
---- | ----
ACCEPTED | Action accepted.
CANNOT_MOVE | This move cannot be performed. Field is probably occupied.
DEAD | User with specified userID is already dead and cannot perform any actions.
