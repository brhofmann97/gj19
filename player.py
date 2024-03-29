import pygame
from pygame.locals import *

from main import *

import bullet

class Player(object):
    def __init__(self, game):
        self.game = game
        self.pos = pygame.math.Vector2(game.PLAYER_SPAWN)
        self.dir = pygame.math.Vector2(0, 0)
        self.prev_dir = pygame.math.Vector2(0, 1)
        self.atk_dir = pygame.math.Vector2(0, 0)
        self.imgs = self.game.player_imgs
        self.radius = 16
        self.hp = game.PLAYER_MAX_HEALTH
        self.can_move_x = True
        self.can_move_y = True
        self.can_attack = True
        self.anim_timer = 0.0
        self.atk_timer = 0.0
        self.cur_frame = 0
        self.bullets = []

    def handle_events(self):
        pass

    def update(self):
        # Update direction
        self.dir.x = (self.game.keys[K_d] - self.game.keys[K_a])
        self.dir.y = (self.game.keys[K_s] - self.game.keys[K_w])
        if self.dir.x != 0 or self.dir.y != 0:
            self.prev_dir = pygame.math.Vector2(self.dir)
            # Update animation
            self.anim_timer += self.game.delta
            if self.anim_timer >= self.game.PLAYER_ANIM_DELAY:
                self.cur_frame = (self.cur_frame + 1) % 2
                self.anim_timer = 0.0
        else:
            self.anim_timer = 0.0
            self.cur_frame = 0

        # Update attack timer
        if not self.can_attack:
            self.atk_timer += self.game.delta
            if self.atk_timer >= self.game.PLAYER_ATTACK_DELAY:
                self.can_attack = True
                self.atk_timer = 0.0

        # Update attack direction
        self.atk_dir.x = (self.game.keys[K_RIGHT] - self.game.keys[K_LEFT])
        self.atk_dir.y = (self.game.keys[K_DOWN] - self.game.keys[K_UP])
        if (self.atk_dir.x != 0 or self.atk_dir.y != 0) and self.can_attack:
            # Fire a bullet
            self.bullets.append(bullet.Bullet(
                self.game, pygame.math.Vector2(self.pos),
                pygame.math.Vector2(self.atk_dir), True))
            self.can_attack = False

        # Calculate new position
        new_pos = self.pos + (self.dir * self.game.PLAYER_SPEED * self.game.delta)
        new_xrect = Rect(
            new_pos.x - self.radius,
            self.pos.y - self.radius,
            self.radius * 2,
            self.radius * 2)
        new_yrect = Rect(
            self.pos.x - self.radius,
            new_pos.y - self.radius,
            self.radius * 2,
            self.radius * 2)

        # Check for collisions with walls
        for tile in self.game.obstacles:
            if self.can_move_x and new_xrect.colliderect(tile.rect):
                self.can_move_x = False
            if self.can_move_y and new_yrect.colliderect(tile.rect):
                self.can_move_y = False

        # Update position
        if self.can_move_x:
            self.pos.x = new_pos.x
        if self.can_move_y:
            self.pos.y = new_pos.y
        self.can_move_x, self.can_move_y = True, True

        # Update bullets
        self.bullets[:] = [b for b in self.bullets if b.update() == True]

    def draw(self):
        x, y = self.pos.x - 16, self.pos.y - 16
        if self.dir.x != 0 or self.dir.y != 0:
            self.game.screen.blit(
                self.imgs[tuple(self.dir)][self.cur_frame], (x, y))
        else:
            self.game.screen.blit(
                self.imgs[tuple(self.prev_dir)][2], (x, y))
        if self.game.debug:
            pygame.draw.rect(
                self.game.screen, game.WHITE, (x, y, game.TILE_SIZE, game.TILE_SIZE), 1)

        for b in self.bullets:
            b.draw()

