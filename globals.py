TITLE = "Downgraded"

TILE_SIZE = 32
WIN_WIDTH_T = 20
WIN_HEIGHT_T = 15
WIN_WIDTH_PX = WIN_WIDTH_T * TILE_SIZE      # 640
WIN_HEIGHT_PX = WIN_HEIGHT_T * TILE_SIZE    # 480

PLAYER_MAX_HEALTH = 10
PLAYER_SPEED = 125
PLAYER_ANIM_DELAY = 0.2
PLAYER_ATTACK_DELAY = 0.2
PLAYER_SPAWN = (WIN_WIDTH_PX / 2, WIN_HEIGHT_PX / 2)

ENEMY_MAX_HEALTH = 10
ENEMY_SPEED = 50
ENEMY_ANIM_DELAY = 0.2
ENEMY_ATTACK_DELAY = 1.0
ENEMY_SPIN_DELAY = 0.2
ENEMY_AGGRO_RADIUS = 6

EXPLOSION_ANIM_DELAY = 0.1

BULLET_SPEED = 400

ROOMS = [
    [
        "@@@_@@@@@@@@@@@@_@@@",
        "@..................@",
        "@..................@",
        "@.........E........@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@@@@@@@@@@@@@@@@@@@@"],
        [
        "@@@_@@@@@@@@@@@@_@@@",
        "@..................@",
        "@....E.............@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@..............E...@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@@@_@@@@@@@@@@@@_@@@"],
        [
        "@@@_@@@@@@@@@@@@_@@@",
        "@..................@",
        "@..................@",
        "@...E..............@",
        "@..................@",
        "@...............E..@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@.....E............@",
        "@..................@",
        "@..................@",
        "@@@_@@@@@@@@@@@@_@@@"],
        [
        "@@@@@@@@@@@@@@@@@@@@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@..................@",
        "@@@_@@@@@@@@@@@@_@@@"]]

BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
