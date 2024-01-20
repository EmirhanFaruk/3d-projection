
# Modification date: Thu Jan  5 19:24:36 2023

# Production date: Sun Sep  3 15:43:51 2023

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (400, 400)

# Create the window
screen = pygame.display.set_mode(window_size, DOUBLEBUF|OPENGL)

# Set the background color
glClearColor(0.5, 0.5, 0.5, 1.0)

# Set the projection matrix
gluPerspective(45, (window_size[0]/window_size[1]), 0.1, 50.0)

# Set the camera position and orientation
gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)

# Initialize the cube's orientation
angle = 0.0

clock = pygame.time.Clock()
# Run the game loop
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    # Update the cube's orientation
    #if angle < 30:
    angle += 0.01
    
    # Rotate the cube around the y-axis
    glRotatef(angle, 1, 1, 1)
    
    # Draw the 3D cube
    glBegin(GL_QUADS)
    # Front face
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    # Back face
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)
    # Left face
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    
    # Top face
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    # Bottom face
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glEnd()
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
