# -*- coding utf-8 -*-
class Settings():
	'''Класс для хранения настроик игры Alien Invasion.'''
	
	def __init__(self):
		'''Иницализирует настройки игры.'''
		#Параметры экрана
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = 230, 230, 230
		#Настройки коробля.
		self.ship_speed_factor = 1.5
		
		#Параметры пули
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
