"""
Script has been rewritten to fit within the certain purpose given, however most of the codebase remains the same to the original 
author.

MIT License

Copyright (c) 2023 StanislavPetrovV

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


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
