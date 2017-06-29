# -*- coding utf-8 -*-

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

#Константы:
title = "alien invasion"

def run_game():
	#Инициализирует игру и создает объекты экрана.
	pygame.init()
	
	ai_settings = Settings()
	
	
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption(title.title())
	#Make ship.
	ship = Ship(ai_settings, screen)
	#Создание пуль для хранения пуль
	bullets = Group()
	
	#Запуск основного цикла игры
	while True:
		#Отслеживание событий клавиатуры и мыши.
		gf.check_events(ship)
		ship.update()
		bullets.update()
		gf.update_screen( ship, bullets)

run_game()
