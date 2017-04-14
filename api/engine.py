from enum import IntEnum
from typing import List, Tuple
import random

class FieldType(IntEnum):
    FREE = 1
    DESTRUCTIBLE = 2
    INDESTRUCTIBLE = 3
    OCCUPIED_BOMB = 4
    OCCUPIED_UPGRADE = 5
    OCCUPIED_USER = 6

field_template_dict = {
    FieldType.FREE.value : {},
    FieldType.OCCUPIED_BOMB.value: {'bomb_turns_left': 0, 'bomb_range': 0}
}




def indestructible(number_of_columns=10, number_of_rows=10):
    MIN_COLUMN_COUNT = 2
    MIN_ROW_COUNT = 2
    if number_of_columns < MIN_COLUMN_COUNT:
        raise Exception('COLUMN count have to be > ' + str(MIN_COLUMN_COUNT))
    if number_of_rows < MIN_ROW_COUNT:
        raise Exception('ROW count have to be ' + str(MIN_ROW_COUNT))
    not_useable_fields = set()
    for row in range(0, number_of_rows):
        for column in range(0, number_of_columns):
            if row % 2:
                if column % 2:
                    not_useable_fields.add((row, column))
    return not_useable_fields



def fields_where_user_can_be_placed(number_of_columns=10, number_of_rows=10):
    MIN_COLUMN_COUNT = 2
    MIN_ROW_COUNT = 2
    if number_of_columns < MIN_COLUMN_COUNT:
        raise Exception('COLUMN count have to be > ' + str(MIN_COLUMN_COUNT))
    if number_of_rows < MIN_ROW_COUNT:
        raise Exception('ROW count have to be ' + str(MIN_ROW_COUNT))
    list = []
    for row in range(0, number_of_rows):
        for column in range(0, number_of_columns):
            if not row % 2 and not column % 2:
                list.append((row, column))
    return list


def generate_board(users):
    not_used = indestructible()
    can_be_placed = list(fields_where_user_can_be_placed())
    fields_with_user = {}
    for user in users:
        random_index = random.randint(0, len(can_be_placed))
        fields_with_user[user['name']] = can_be_placed[random_index]
        print(random_index)
        print(can_be_placed[random_index])
        del can_be_placed[random_index]
        print(can_be_placed)
    print(fields_with_user)
    return fields_with_user




class Board:
    def __init__(self, size):
        self.fields: List[Field] = fields
        self.size: Tuple[int] = (12, 24)


class Field:
    def __init__(self):
        self.type = FieldType.FREE


class FieldWithBombs(Field):
    def  __init__(self):
        self.type = FieldType.OCCUPIED_BOMB
        self.bomb_turns_left = 0
        self.bomb_range = 0


class FieldWithUpgrade:
    def __init__(self):
        self.type = FieldType.OCCUPIED_UPGRADE
        self.upgrade_type = 'ADDITIONAL_BOMB'


class FieldUser(Field):
    def __init__(self):
        self.type = FieldType.OCCUPIED_USER
        self.user_name = ''
        self.bombs_left = 0


class Engine:
    def __init__(self, fields: List[Field]):
        self.board: Board = Board(fields)



    state = {
        'actual_state': [{
                'field_type': 'OCCUPIED_BOMB',
                'bomb_turns_left': 2,
                'bomb_range': 3
            },{
                'field_type': 'OCCUPIED_USER',
                'user_name': 'Example_bot_1',
                'bombs_left': 0
            },{
                'field_type': 'OCCUPIED_UPGRADE',
                'upgrade_type': 'ADDITIONAL_BOMB'
            },{
                'field_type': 'INDESTRUCTIBLE'
            }],
        'state_number': 17,
        'map_size': (2, 2),
        'user_position': (1,1),
        'time_left': 190
    }

    def get_state(self):
        state_view = self.create_state_map(self);
        return state_view

    def create_state_map(self):
        return self.state

    def get_state_number(self):
        pass

    def get_user_possition(self):
        pass



if __name__ == '__main__':
    users = [ {'name':'Luk'}, {'name':'Marke'}]
    generate_board(users)