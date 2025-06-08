import pygame
import random
import sys

# 초기 설정
pygame.init()
WIDTH, HEIGHT = 480, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("피하기 게임")

clock = pygame.time.Clock()

# 색상
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 플레이어
player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 60, 50, 50)
player_speed = 7

# 장애물
enemy = pygame.Rect(random.randint(0, WIDTH - 50), 0, 50, 50)
enemy_speed = 5

# 점수
score = 0
font = pygame.font.SysFont(None, 36)

# 게임 루프
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    # 장애물 이동
    enemy.y += enemy_speed
    if enemy.top > HEIGHT:
        enemy = pygame.Rect(random.randint(0, WIDTH - 50), 0, 50, 50)
        score += 1
        enemy_speed += 0.3  # 점점 빨라짐

    # 충돌 체크
    if player.colliderect(enemy):
        game_over = font.render("Game Over! Score: " + str(score), True, RED)
        screen.blit(game_over, (WIDTH // 2 - 140, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    # 그리기
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, enemy)
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
