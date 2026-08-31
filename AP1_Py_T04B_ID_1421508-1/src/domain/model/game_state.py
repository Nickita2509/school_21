from enum import Enum


class GameState(Enum):
    WAITING = "waiting"
    PLAYER_X_TURN = "player_x_turn"
    PLAYER_O_TURN = "player_o_turn"
    DRAW = "draw"
    WIN_X = "win_x"
    WIN_O = "win_o"