#This game is based on a player navigating around three enemies and trying to catch the prize.
#The enemies and the prize will move at different heights and speeds from right to left and vice versa.
#If the player collides with the enemies, they lose.
#If the player catches the prize, they win.

import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# This creates the player and gives it the image found in this folder (similarly with the enemies and the prize images). 

player = pygame.image.load("player.jpg")
enemy1 = pygame.image.load("monster.jpg")
enemy2 = pygame.image.load("monster.jpg")
enemy3 = pygame.image.load("monster.jpg")
prize = pygame.image.load("prize.jpg")

#Create boundary walls on the sides of the screen so that when the enemies and prizes collide with the walls, they move in the opposite direction.
#To create the walls, draw lines using "pygame.draw.line(surface, colour , point1, point2 , width)"
#The colour of the lines have not been set.

leftBound = pygame.draw.line(screen, (0, 0, 0), (0, 0), (0, screen_height),1)
rightBound = pygame.draw.line(screen, (0, 0, 0), (screen_width-1, 0), (screen_width-1, screen_height),1)

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).

image_height = player.get_height()
image_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

# Store the positions of the player and enemy as variables so that you can change them later.
# The player will start at a random position on the left side of the screen so that the player has enough time to see all the enemies positions.

playerXPosition = random.randint(0, screen_width/3)
playerYPosition = random.randint(0, screen_height - image_height)

# The enemies will start at a random x positions on the right half of the screen. To ensure that enemies don't overlap each other, the screen height is divided by 3 so that each enemy will occur in their own 1/3rd of the screen. 

enemy1XPosition =  random.randint(screen_width/2, screen_width - enemy1_width)
enemy1YPosition =  random.randint(0, screen_height/3)
enemy2XPosition =  random.randint(screen_width/2, screen_width - enemy2_width)
enemy2YPosition =  random.randint(screen_height/3, 2*screen_height/3)
enemy3XPosition =  random.randint(screen_width/2, screen_width - enemy3_width)
enemy3YPosition =  random.randint(2*screen_height/3, screen_height - enemy3_height)

# Prize position will start anywhere on the right side of the screen

prizeXPosition =  random.randint(screen_width/2, screen_width - prize_width)
prizeYPosition =  random.randint(0, screen_height - prize_height)

# This checks if the up or down key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False. 
# Boolean values are True or False values that can be used to test conditions and test states that are binary, i.e. either one way or the other. 

keyUp= False
keyDown = False
keyLeft = False
keyRight = False

#Set the direction the enemies and the prize are travelling in. When the boolean is True, they move left. The boolean changes to False when they hit the boundart wall on the left which then changes their direction so that they move right.

enemy1_direction = True
enemy2_direction = True
enemy3_direction = True
prize_direction = True

#Set the starting speed of each enemy and the prize. Use the random function so that they all start at different speeds

enemy1_speed = random.randint(15,40)/100        #Divide by 100 to get a float value
enemy2_speed = random.randint(15,40)/100
enemy3_speed = random.randint(15,40)/100
prize_speed = random.randint(15,40)/100

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play. 

while 1: # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting).  

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 0.5
    if keyDown == True:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 0.5
    if keyLeft == True:
        if playerXPosition > 0 : # This makes sure that the user does not move the player to the left of the window.
            playerXPosition -= 0.5
    if keyRight == True:
        if playerXPosition < screen_width - image_width:# This makes sure that the user does not move the player to the right of the window.
            playerXPosition += 0.5
    
    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for enemies:
    
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    # Bounding box for the prize:
    
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

  
    # Test collision of the boxes:
    
    if playerBox.colliderect(enemy1Box):
    
        # Display losing status to the user: 
        
        print("\nEnemy catches you. You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy2Box):
    
        # Display losing status to the user: 
        
        print("\nYou have been eaten. You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy3Box):
    
        # Display losing status to the user: 
        
        print("\nToo slow. You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)

    if playerBox.colliderect(prizeBox):
    
        # Display losing status to the user: 
        
        print("\nYou caught the cherry. You win!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)


    #To ensure that the enemies and the prize change direction when they collide with the boundary walls on the left and right, the booleans must change as mentioned above.
    #To make the game more interesting, the enemies travel at different Y positions and speeds when moving left or right
    #After each wall collision, use random function to calculate the new Y position and the new speed of each enemy and the prize


    if enemy1Box.colliderect(leftBound):
        enemy1_direction = False                                    #Enemy collides with left wall
        enemy1YPosition =  random.randint(0, screen_height/3)       #Calculate new Y Position
        enemy1_speed = random.randint(15,60)/100                    #Calculate new speed
        
    if enemy1Box.colliderect(rightBound):
        enemy1_direction = True                                     #Enemy collides with right wall
        enemy1YPosition =  random.randint(0, screen_height/3)       #Calculate new Y Position
        enemy1_speed = random.randint(15,60)/100                    #Calculate new speed
        
    if enemy2Box.colliderect(leftBound):
        enemy2_direction = False
        enemy2YPosition =  random.randint(screen_height/3, 2*screen_height/3)
        enemy2_speed = random.randint(15,60)/100
    
    if enemy2Box.colliderect(rightBound):
        enemy2_direction = True
        enemy2YPosition =  random.randint(screen_height/3, 2*screen_height/3)
        enemy2_speed = random.randint(15,60)/100

    if enemy3Box.colliderect(leftBound):
        enemy3_direction = False
        enemy3YPosition =  random.randint(2*screen_height/3, screen_height - enemy3_height)
        enemy3_speed = random.randint(15,60)/100
    
    if enemy3Box.colliderect(rightBound):
        enemy3_direction = True
        enemy3YPosition =  random.randint(2*screen_height/3, screen_height - enemy3_height)
        enemy3_speed = random.randint(15,60)/100

    if prizeBox.colliderect(leftBound):
        prize_direction = False
        prizeYPosition =  random.randint(0, screen_height - prize_height)
        prize_speed = random.randint(15,60)/100
    
    if prizeBox.colliderect(rightBound):
        prize_direction = True
        prizeYPosition =  random.randint(0, screen_height - prize_height)
        prize_speed = random.randint(15,60)/100
    
    #Based on the booleans above, the enemies and the prize will move in the appropriate direction and at the randome speeds calculated above
    
    
    if enemy1_direction == True:
        enemy1XPosition -= enemy1_speed

    if enemy1_direction == False:
        enemy1XPosition += enemy1_speed

    if enemy2_direction == True:
        enemy2XPosition -= enemy2_speed

    if enemy2_direction == False:
        enemy2XPosition += enemy2_speed

    if enemy3_direction == True:
        enemy3XPosition -= enemy3_speed

    if enemy3_direction == False:
        enemy3XPosition += enemy3_speed

    if prize_direction == True:
        prizeXPosition -= prize_speed

    if prize_direction == False:
        prizeXPosition += prize_speed
 
   
    # ================The game loop logic ends here. =============
