import pygame
import time
import random
pygame.font.init()


width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Falling Snows")

background = pygame.transform.scale(pygame.image.load("bg_5.jpg"),(width, height))

player_width = 80
player_height = 95

player_velocity = 5

star_width = 8
star_height = 10

star_velocity = 5

font = pygame.font.SysFont("Arial", 30)


# Load cartoon character image
player_image = pygame.image.load("character_4.jpg").convert_alpha()
player_image = pygame.transform.scale(player_image, (player_width, player_height))



def draw(player,elapsed_time,stars):
    
    window.blit(background, (0,0))
    
    time_text = font.render(f"Time: {round(elapsed_time)}s", 1,"white" )
    window.blit(time_text, (10,10))
    
    
    #pygame.draw.rect(window, "red", player)
    
    
    # Draw the cartoon character image instead of the red rectangle
    window.blit(player_image, (player.x, player.y))
    
    
    for star in stars:
        pygame.draw.rect(window, "red",star)
    
    pygame.display.update()




def main():

    run = True
    
    player = pygame.Rect(200, height - player_height, player_width, player_height )
    
    
    clock = pygame.time.Clock()

    start_time = time.time()
    elapsed_time = 0
    

    star_add = 2000
    star_count = 0
    
    stars = []
    
    hit = False
    
    
    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        
        if star_count > star_add:
            for _ in range(5):
                star_x = random.randint(0, width - star_width)
                star = pygame.Rect(star_x, - star_height, star_width, star_height)
                stars.append(star)
            
            star_add = max(500, star_add -30)
            star_count = 0
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_velocity >= 0:
            player.x -= player_velocity
        if keys[pygame.K_RIGHT] and player.x + player_velocity + player.width <= width:
            player.x += player_velocity
        
        
        
        for star in stars[:]:
            star.y += star_velocity
            if star.y > height:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        
        
        if hit:
            score = round(elapsed_time)
            
            lost_text = font.render("YOU LOST!!", 5, "red")
            window.blit(lost_text, (width/2 - lost_text.get_width()/2, height/2 - lost_text.get_height()/2 ))
            
            score_text = font.render(f"Your score is: {score}", 5, "red")
            window.blit(score_text, (width/2 - score_text.get_width()/2, height/1.78 - score_text.get_height()/2 ))
            
            pygame.display.update()
            pygame.time.delay(4000)
            break
            
        draw(player, elapsed_time,stars)
        
    
    pygame.quit()
    
    

if __name__ == "__main__":
    main()