import pygame
import moderngl
import sys
import glm
import numpy
import pywavefront

DEBUG = False

RESOLUTION = glm.vec2(1280, 720)
BACKGROUND_COLOUR = (0,0,0)
MAX_FPS = 90

LIGHT_POSITION = glm.vec3(0,0,0)
LIGHT_COLOUR = glm.vec3(1,1,1)
LIGHT_AMBIENCE = 1.5
LIGHT_DIFFUSION = 1.0
LIGHT_SPECULAR = 1.6

FIELD_OF_VIEW = 50
NEAR_VIEW = 0.1
FAR_VIEW = 100
SPEED = 0.005
SENSITIVITY = 0.04
CAMERA_POSITION = glm.vec3(0,2,0)
CAMERA_Y = -90
CAMERA_X = 0
CAMERA_SCALE = 0.15

MODEL_POSITION = glm.vec3(0,0,0)
MODEL_ROTATION = glm.vec3(0,0,0)
MODEL_SCALE = glm.vec3(1,1,1)

MAIN_DIRECTORY = 'Engine'
COLLISION_SIZE = 0.15
OBJECT_VELOCITY = 0.025

MAXSOUNDCHANNELS = 10
SOUNDPATH = "./Sounds"