import pygame
import os
import time
import math
import copy

Sprite = pygame.sprite.Sprite
Surface = pygame.Surface
Rect = pygame.rect.Rect
Draw = pygame.draw
Image = pygame.image
Transform = pygame.transform

def make_timer(name:str):
    timer = {"name": name,
             "start" : 0,
             "total" : 0}
    return timer

def start_time(timer:dict):
    start = time.time()
    timer["start"] = start
    return timer

def sum_time(segment:dict):
    new_total = time.time() - segment.get("start")
    segment["total"] += new_total
    return segment

def end_time(segment:dict):
    print(f"{segment.get("name")} took {segment.get("total")} seconds")
    segment["total"] = 0
    return segment