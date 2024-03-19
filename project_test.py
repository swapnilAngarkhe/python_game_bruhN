import pygame
import pytest
from project import Player, Obstacle, show_score, collisions, collision_sprite




def test_player_input():
    player = Player()
    player.rect.bottom = 295
    player.player_input()
    assert player.gravity == -16
    assert player.jump_sfx.play.called

def test_obstacle_creation():
    obstacle = Obstacle('fly')
    assert obstacle.frames
    assert obstacle.rect

def test_show_score():
    # pygame.time.get_ticks = lambda: 1000
    assert show_score() == 0

def test_collisions():
    player = pygame.Rect(0, 0, 10, 10)
    obs_rect = pygame.Rect(5, 5, 10, 10)

    assert not collisions(player, [obs_rect])
    assert collisions(player, [])

def test_collision_sprite():
    player = pygame.sprite.Sprite()
    player.rect = pygame.Rect(0, 0, 10, 10)
    obstacle_group = pygame.sprite.Group()

    assert not collision_sprite(player, obstacle_group)
    assert collision_sprite(player, pygame.sprite.Group())
