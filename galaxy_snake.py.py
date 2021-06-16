import pygame
from pygame.locals import *
import time
import random
import os.path


"""
Snake program.
"""
SIZE = 25
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 350
TEXT_GAME = (255,255,255)
TEXT_MENU = (255,255,255)

x_points = list(range(1,int(WINDOW_WIDTH/SIZE-1)))
y_points = list(range(1,int(WINDOW_HEIGHT/SIZE-1)))
x_points_multipled = [element * SIZE for element in x_points]
y_points_multipled = [element * SIZE for element in y_points]

tuples = []
for x in x_points_multipled:
    for y in y_points_multipled:
        tuples.append((x,y))


x_menu_rm = list(range(SIZE,201,SIZE))
y_menu_rm = list(range(300,351, SIZE))

x_ships_rm = [125,150,300,325,475,500]
y_ships_rm = [75,150,225]

ships_remove = [(125,75),(150,75),(300,150),(325,150),(475,225),(500,225)]
scores_remove = [(600,25),(600,50),(625,25),(625,50),(650,25),(650,50),(675,25),(675,50)]
menu_remove = [(25,300),(25,325),(50,300),(50,325),(75,300),(75,325),(100,300),(100,325),(125,300),(125,325),(150,300),(150,325),(175,300),(175,325),(200,300),(200,325)]

remove = ships_remove + scores_remove + menu_remove


for element in remove:
    if element in tuples:
        tuples.remove(element)

available_points = tuples



def loadImage(name, useColorKey=False):
    """
    Load an image and convert its pixels to screen pixel's format. 
    If useColorKey = True, color of (0,0) pixel is treated as transparent.

    return: converted image
    """

    fullname = os.path.join("picture",name)
    image = pygame.image.load(fullname)  
    image = image.convert() 
    if useColorKey is True:
        colorkey = image.get_at((0,0)) 
        image.set_colorkey(colorkey,RLEACCEL) 
    return image

#Moving objects

class Star:
    """
    The class which creates star objects.
    """

    def __init__(self, parent_screen):
        """
        The constructor.
        *param parent_screen: surface for objects
        """

        self.parent_screen = parent_screen
        self.image = loadImage("star.png",True).convert()
        self.image = pygame.transform.scale(self.image, (SIZE, SIZE))        
        self.x = SIZE*3
        self.y = SIZE*3

    def draw(self):
        """
        Draw the object on the screen.
        """

        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        """
        Settle coordinares of new object randomly
        """

        self.x = random.choice(available_points)[0]
        self.y = random.choice(available_points)[1]


class Heart:
    """
    The class which create Heart objects.
    """

    def __init__(self, parent_screen):
        """
        The constructor.
        *param parent_screen: surface for objects
        """

        self.parent_screen = parent_screen
        self.image = loadImage("heart.png",True).convert()
        self.image = pygame.transform.scale(self.image, (SIZE, SIZE))        
        self.x = SIZE*5
        self.y = SIZE*5

    def draw(self):
        """
        Draw the object on the screen.
        """

        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        """
        Settle coordinares of new object randomly
        """

        self.x = random.choice(available_points)[0]
        self.y = random.choice(available_points)[1]



#STABLE OBJECTS 

class Ship:
    """
    The class which creates Ship objects.
    """

    def __init__(self, parent_screen, width, height, x, y):
        """
        The constructor.
        *param parent_screen: surface for objects
        *param width: rate which enable settle width of object as multiple of SIZE 
        *param height: rate which enable settle height of object as multiple of SIZE
        *param x: rate which enable settle first coordinate of left up corner of object as multiple of SIZE
        *param y: rate which enable settle second coordinate of left up corner of object as multiple of SIZE
        """

        self.parent_screen = parent_screen
        self.image = loadImage("ship.png",True).convert()
        self.image = pygame.transform.scale(self.image, (SIZE*width, SIZE*height))        
        self.x = SIZE*x
        self.y = SIZE*y

    def draw(self):
        """
        Draw the object on the screen.
        """

        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

class Author:
    """
    The class which creates author page.
    """

    def __init__(self, parent_screen, width, height, x, y):
        """
        The constructor.
        *param parent_screen: surface for objects
        *param width: rate which enable settle width of object as multiple of SIZE 
        *param height: rate which enable settle height of object as multiple of SIZE
        *param x: rate which enable settle first coordinate of left up corner of object as multiple of SIZE
        *param y: rate which enable settle second coordinate of left up corner of object as multiple of SIZE
        """

        self.parent_screen = parent_screen
        self.image = loadImage("author.png",True).convert()
        self.image = pygame.transform.scale(self.image, (SIZE*width, SIZE*height))
        
        self.x = SIZE*x
        self.y = SIZE*y

    def draw(self):
        """
        Draw the object on the screen.
        """

        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

class Description:
    """
    The class which creates description page.
    """

    def __init__(self, parent_screen, width, height, x, y):
        """
        The constructor.
        *param parent_screen: surface for objects
        *param width: rate which enable settle width of object as multiple of SIZE 
        *param height: rate which enable settle height of object as multiple of SIZE
        *param x: rate which enable settle first coordinate of left up corner of object as multiple of SIZE
        *param y: rate which enable settle second coordinate of left up corner of object as multiple of SIZE
        """

        self.parent_screen = parent_screen
        self.image = loadImage("description.png",True).convert()
        self.image = pygame.transform.scale(self.image, (SIZE*width, SIZE*height))
        
        self.x = SIZE*x
        self.y = SIZE*y

    def draw(self):
        """
        Draw the object on the screen.
        """

        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

class Instructions:
    """
    The class which creates instructions page.
    """

    def __init__(self, parent_screen, width, height, x, y):
        """
        The constructor.
        *param parent_screen: surface for objects
        *param width: rate which enable settle width of object as multiple of SIZE 
        *param height: rate which enable settle height of object as multiple of SIZE
        *param x: rate which enable settle first coordinate of left up corner of object as multiple of SIZE
        *param y: rate which enable settle second coordinate of left up corner of object as multiple of SIZE
        """

        self.parent_screen = parent_screen
        self.image = loadImage("instructions.png",True).convert()
        self.image = pygame.transform.scale(self.image, (SIZE*width, SIZE*height))
        
        self.x = SIZE*x
        self.y = SIZE*y

    def draw(self):
        """
        Draw the object on the screen.
        """

        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()




#SNAKE 

class Snake:
    """
    The class which creates Snake objects.
    """

    def __init__(self, parent_screen,length):
        """
        The constructor.
        *param parent_screen: surface for objects
        """

        self.parent_screen = parent_screen
        self.block = loadImage("body.png",True).convert()
        self.block = pygame.transform.scale(self.block, (SIZE, SIZE))        
        self.direction = 'down'
        self.length = length
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.life = 1
        self.heart_counter = 1
    
    def move_left(self):
        """
        Go left.
        """

        self.direction = 'left'

    def move_right(self):
        """
        Go right.
        """

        self.direction = 'right'

    def move_up(self):
        """
        Go up.
        """

        self.direction = 'up'

    def move_down(self):
        """
        Go down.
        """

        self.direction = 'down'

    def walk(self):
        """
        Assign coordinates of i-element of snake to i-1 element.
        Change coordinates of first element depending on movement direction.
        """

        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        """
        Draw every object of snake.
        """

        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def lengthen(self):
        """
        Increase length of snake and add new elements to arrays.
        """

        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def minus_life(self):
        """
        Decrease amound of lifes.
        """
        if self.life > 1:
            self.life -= 1

    def plus_life(self):
        """
        Increase amount of lifes.
        """
        if self.heart_counter % 5 == 0:
            self.life += 1
        else:
            pass

    
#GAME

class Game:
    """
    The class which create game.
    """

    def __init__(self):
        """
        The constructor.
        """

        pygame.init()
        pygame.display.set_caption("GALAXY SNAKE")
        
        pygame.mixer.init()
        self.play_bkg_music("never_ending")
        
        self.surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        
        self.ship1 = Ship(self.surface, 2, 1, 5, 3)
        self.ship2 = Ship(self.surface, 2, 1, 12, 6)
        self.ship3 = Ship(self.surface, 2, 1, 19, 9)

        self.snake = Snake(self.surface,1)
        self.snake.draw()
        
        self.star = Star(self.surface)
        self.star.draw()
        self.heart = Heart(self.surface)
        self.heart.draw()
        
        self.author = Author(self.surface, 3, 1, 0.5, 12.5)
        self.description = Description(self.surface, 3, 1, 4, 12.5)
        self.instructions = Instructions(self.surface, 3, 1, 7.5, 12.5)
        


    def collision(self, x1, y1, x2, y2, width = 1, height = 1):
        """
        Check if elements with given coordinates collide.
        *param x1: first coorfinate of first element
        *param y1: second coorfinate of first element
        *param x2: first coorfinate of second element
        *param y2: second coorfinate of second element
        """

        if x1 >= x2 and x1 < x2 + SIZE*width:
            if y1 >= y2 and y1 < y2 + SIZE*height:
                return True
        return False


    def sound(self,sound):
        """
        Load a sound.
        *param sound: sound which is supposed to be loaded.
        """

        sound = pygame.mixer.Sound(f"sounds/{sound}.mp3")
        pygame.mixer.Sound.play(sound)

    def render_background(self,picture):
        """
        Load the background picture.
        """
        background = loadImage(f"{picture}").convert()
        background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.surface.blit(background, (0,0))


    def play(self):
        """
        Draw objects, call functions in case of collision and change directions
        when snake is on the edge of screen.
        """

        self.render_background("snake_back.jpg")
        self.ship1.draw()
        self.ship2.draw()
        self.ship3.draw()
        self.snake.walk()
        self.star.draw()
        self.heart.draw() 
        self.display_score_lives()
        self.author.draw()
        self.description.draw()
        self.instructions.draw()
        pygame.display.flip()

        #eating a star
        if self.collision(self.snake.x[0], self.snake.y[0], self.star.x, self.star.y):
            self.sound("ding")
            self.snake.lengthen()
            self.star.move()

        #eating a heart
        if self.collision(self.snake.x[0], self.snake.y[0], self.heart.x, self.heart.y):
            self.sound("ding")
            self.snake.heart_counter += 1
            self.snake.plus_life()
            #timer = threading.Timer(10.0, self.heart.move(), args = None, kwargs = None)
            #timer.start()
            #pygame.time.set_timer(self.heart.move(),5)
            self.heart.move()

        #hiting with ships
         
        if self.collision(self.snake.x[0], self.snake.y[0], self.ship1.x, self.ship1.y, 2):
            self.sound("hit")
            self.snake.life = 0
            raise "Over!"

        if self.collision(self.snake.x[0], self.snake.y[0], self.ship2.x, self.ship2.y, 2):
            self.sound("hit")
            self.snake.life = 0 
            raise "Over!"

        if self.collision(self.snake.x[0], self.snake.y[0], self.ship3.x, self.ship3.y, 2):
            self.sound("hit")
            self.snake.life = 0
            raise "Over!"
        

        # snake collide with itself
        for i in range(3, self.snake.length):
            if self.collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.snake.minus_life()
                self.sound("hit")
                raise "Over!"
        
        #loading menu
        if self.collision(self.snake.x[0], self.snake.y[0], self.author.x, self.author.y, 3, 2):
            raise "Over!"

        if self.collision(self.snake.x[0], self.snake.y[0], self.description.x, self.description.y, 3, 2):
            raise "Over!"

        if self.collision(self.snake.x[0], self.snake.y[0], self.instructions.x, self.instructions.y, 3, 2):
            raise "Over!"

        #changing direction on the edge of window
        if self.snake.x[0] < 0:
            self.snake.x[0] = WINDOW_WIDTH
            self.snake.move_left()

        if self.snake.x[0] > WINDOW_WIDTH:
            self.snake.x[0] = -SIZE
            self.snake.move_right()

        if self.snake.y[0] < 0:
            self.snake.y[0] = WINDOW_HEIGHT
            self.snake.move_up()

        if self.snake.y[0] > WINDOW_HEIGHT:
            self.snake.y[0] = -SIZE
            self.snake.move_down()

    def display_score_lives(self):
        """
        Display score and amount of lives in the corner of window.
        """

        font = pygame.font.Font('GrandHotel-Regular.otf',35)
        score = font.render(f"Score: {self.snake.length-1}",True,(TEXT_GAME))
        self.surface.blit(score,(600,10))
        score = font.render(f"Life: {self.snake.life}",True,(TEXT_GAME))
        self.surface.blit(score,(600,40))
        
        font1 = pygame.font.Font('GrandHotel-Regular.otf', 15)


        
    def show_game_over(self):
        """
        Set the backgound picture and fontS. Display message.
        """

        self.render_background("background.jpg")
       
        font1 = pygame.font.Font('GrandHotel-Regular.otf', 60)
        font2 = pygame.font.Font('GrandHotel-Regular.otf', 40)

        line1 = font1.render(f"Game is over! Your score is {self.snake.length-1}.", True, TEXT_MENU)
        line1_rect = line1.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2-100))
        self.surface.blit(line1, line1_rect)
        
        
        line2 = font2.render("To play again press ENTER", True, TEXT_MENU)
        line2_rect = line2.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        self.surface.blit(line2, line2_rect)
        
        line3 = font2.render("To exit press ESCAPE", True, TEXT_MENU)
        line3_rect = line3.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2+50))
        self.surface.blit(line3, line3_rect)
        
        pygame.display.flip()
        pygame.mixer.music.pause()
        self.play_bkg_music("astronomia")
        

    def show_warning(self):
        """
        Set the backgound picture and font. Display message.
        """

        self.render_background("background.jpg")
        
        font1 = pygame.font.Font('GrandHotel-Regular.otf', 50)
        font2 = pygame.font.Font('GrandHotel-Regular.otf', 30)

        line1 = font1.render(f"Collision! Look out!", True, TEXT_MENU)
        line1_rect = line1.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2-100))
        self.surface.blit(line1, line1_rect)
        
        line2 = font2.render(f"You have {self.snake.life} chances.", True, TEXT_MENU)
        line2_rect = line2.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        self.surface.blit(line2, line2_rect)
        
        line3 = font2.render("Press ENTER to continue.", True, TEXT_MENU)
        line3_rect = line3.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2+50))
        self.surface.blit(line3, line3_rect)
        
        pygame.display.flip()
        pygame.mixer.music.pause()
        self.play_bkg_music("oops")

    def show_author(self):
        """
        Set the backgound picture and font. Display message.
        """
        
        self.render_background("background.jpg")

        font = pygame.font.Font('GrandHotel-Regular.otf', 45)
        line = font.render(f"Wypych Karolina", True, TEXT_MENU)
        line_rect = line.get_rect(center=(WINDOW_WIDTH/4, 120))
        self.surface.blit(line, line_rect)

        font = pygame.font.Font('GrandHotel-Regular.otf', 25)
        line = font.render(f"Applied Mathematics", True, TEXT_MENU)
        line_rect = line.get_rect(center=(WINDOW_WIDTH/4, 175))
        self.surface.blit(line, line_rect)

        font = pygame.font.Font('GrandHotel-Regular.otf', 25)
        line = font.render(f"Lover of dogs, star and horrors.", True, TEXT_MENU)
        line_rect = line.get_rect(center=(WINDOW_WIDTH/4, 230))
        self.surface.blit(line, line_rect)

        font = pygame.font.Font('GrandHotel-Regular.otf', 25)
        line = font.render(f"Press 'enter' to play.", True, TEXT_MENU)
        line_rect = line.get_rect(center=(WINDOW_WIDTH/4, 300))
        self.surface.blit(line, line_rect)

        background = loadImage("author.jpg").convert()
        background = pygame.transform.scale(background, (300, 310))
        background_rect = background.get_rect(center=(3*WINDOW_WIDTH/4, WINDOW_HEIGHT/2))
        self.surface.blit(background, background_rect)

        pygame.display.flip()


    def show_instructions(self):
        """
        Set the backgound picture and fontS. Display message.
        """

        self.render_background("background.jpg")

        font1 = pygame.font.Font('GrandHotel-Regular.otf', 30)
        font2 = pygame.font.Font('GrandHotel-Regular.otf', 50)
        font3 = pygame.font.Font('GrandHotel-Regular.otf', 20)

        line = font2.render("How to move?", True, TEXT_MENU)
        line_rect = line.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/5))
        self.surface.blit(line, line_rect)

        line = font1.render("K_UP - move up", True, TEXT_MENU)
        line_rect = line.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2.4))
        self.surface.blit(line, line_rect)

        line = font1.render("K_DOWN - move down", True, TEXT_MENU)
        line_rect = line.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2.4+45))
        self.surface.blit(line, line_rect)

        line = font1.render("K_RIGHT - move right", True, TEXT_MENU)
        line_rect = line.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2.4+90))
        self.surface.blit(line, line_rect)

        line = font1.render("K_LEFT - move left", True, TEXT_MENU)
        line_rect = line.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2.4+135))
        self.surface.blit(line, line_rect)

        line = font3.render("Press 'enter' to play the game or 'escape' to quit. ", True, TEXT_MENU)
        line_rect = line.get_rect(center=((WINDOW_WIDTH/2), WINDOW_HEIGHT/2.5+185))
        self.surface.blit(line, line_rect)


        pygame.display.flip()
    
    def show_description(self):
        """
        Set the backgound picture and fontS. Display message.
        """

        self.render_background("background.jpg")

        font1 = pygame.font.Font('GrandHotel-Regular.otf', 30)
        font2 = pygame.font.Font('GrandHotel-Regular.otf', 50)
        font3 = pygame.font.Font('GrandHotel-Regular.otf', 20)

        line = font2.render("Description", True, TEXT_MENU)
        line_rect = line.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/5))
        self.surface.blit(line, line_rect)

        line = font1.render("Collect stars to get longer and longer.", True, TEXT_MENU)
        line_rect = line.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2.5))
        self.surface.blit(line, line_rect)

        line = font1.render("Multiply of 5 hearts increments your chances.", True, TEXT_MENU)
        line_rect = line.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2.5+35))
        self.surface.blit(line, line_rect)

        line = font1.render("Look out for spaceships!", True, TEXT_MENU)
        line_rect = line.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2.5+70))
        self.surface.blit(line, line_rect)

        line = font1.render("They will kill you!", True, TEXT_MENU)
        line_rect = line.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2.5+105))
        self.surface.blit(line, line_rect)

        line = font1.render("If you collide yourself, you lose one chance.", True, TEXT_MENU)
        line_rect = line.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2.5+140))
        self.surface.blit(line, line_rect)

        line = font3.render("Press 'enter' to play the game or 'escape' to quit. ", True, TEXT_MENU)
        line_rect = line.get_rect(center=((WINDOW_WIDTH/2), WINDOW_HEIGHT/2.5+185))
        self.surface.blit(line, line_rect)

        pygame.display.flip()


    def reset(self):
        """
        Reset the game and start again.
        """

        self.snake = Snake(self.surface,1)
        self.star = Star(self.surface)

    def play_bkg_music(self,sound):
        """
        Load background music.
        """

        sound = pygame.mixer.music.load(f"sounds/{sound}.mp3")
        pygame.mixer.music.play(loops=-1)
    
    def run(self):
        """
        Use buttons to control a snake. 
        """
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    
                    if event.key == K_RETURN:
                        pause = False
                        pygame.mixer.music.pause()
                        self.play_bkg_music("never_ending")
                                            
                    if not pause:
                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running = False

            try:
                if not pause:
                    self.play()

            except Exception as e:
                if self.collision(self.snake.x[0], self.snake.y[0], self.author.x, self.author.y, 3, 2):
                    self.show_author()
                    self.snake.x[0] = SIZE
                    self.snake.y[0] = WINDOW_HEIGHT/2
                    pause = True

                elif self.collision(self.snake.x[0], self.snake.y[0], self.description.x, self.description.y, 3, 2):
                    self.show_description()
                    self.snake.x[0] = SIZE
                    self.snake.y[0] = WINDOW_HEIGHT/2
                    pause = True

                elif self.collision(self.snake.x[0], self.snake.y[0], self.instructions.x, self.instructions.y, 3, 2):
                    self.show_instructions()
                    self.snake.x[0] = SIZE
                    self.snake.y[0] = WINDOW_HEIGHT/2
                    pause = True

                else:
                    if self.snake.life == 0:
                        self.show_game_over()
                        self.snake.x[0] = SIZE
                        self.snake.y[0] = SIZE
                        pause = True
                    else:
                        self.show_warning()
                        self.snake.x[0] = SIZE
                        self.snake.y[0] = SIZE
                        pause = True
                        self.reset()
            time.sleep(.1)

if __name__ == '__main__':
    game = Game()
    game.run()


        