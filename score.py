import pygame

pygame.font.init()
texty = 40
textx = 40
score = 0
font = pygame.font.SysFont("Arial", 30)


def update_score(points):
    global score
    score += points
    print("Score: " + str(score))

def draw_score(screen):
    score_text = font.render(f"Score: {score}", True, "Purple")
    screen.blit(score_text, (textx, texty))