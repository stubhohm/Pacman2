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
    """Creates a timer dictionary with the given name.

    Args:
        name (str): The name of the timer.

    Returns:
        dict: A dictionary representing the timer, with 'name', 'start', and 'total' keys.
    """
    timer = {"name": name,
             "start" : 0,
             "total" : 0}
    return timer

def start_time(timer:dict):
    """Starts the timer by recording the current time.

    Args:
        timer (dict): The timer dictionary to start.

    Returns:
        dict: The updated timer dictionary with the start time recorded.
    """
    start = time.time()
    timer["start"] = start
    return timer

def sum_time(segment:dict):
    """Adds the elapsed time to the total time.

    Args:
        segment (dict): The segment dictionary to update.

    Returns:
        dict: The updated segment dictionary with the total time calculated and added.
    """
    new_total = time.time() - segment.get("start")
    segment["total"] += new_total
    return segment

def end_time(segment:dict):
    """Prints the elapsed time for the given segment.

    Args:
        segment (dict): The segment dictionary to print the time for.
    """
    print(f"{segment.get("name")} took {segment.get("total")} seconds")
    segment["total"] = 0
    return segment