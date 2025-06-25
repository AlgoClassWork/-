from pygame import *
# Игровой таймер
clock = time.Clock()
FPS = 100
# Настройки окна
WINDOW_X = 0
WINDOW_Y = 0
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
WINDOW_BACKGROUND = 'background.jpg'
# Настройки игрока
PLAYER_X = 0
PLAYER_Y = 0
PLAYER_SPEED = 3
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 100
PLAYER_IMAGE = 'player.png'
# Создание экрана
window = display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT) )
display.set_caption('Догонялки')
# Загрузка картинок
background_image = transform.scale( image.load(WINDOW_BACKGROUND), (WINDOW_WIDTH, WINDOW_HEIGHT) )
player_image = transform.scale( image.load(PLAYER_IMAGE), (PLAYER_WIDTH, PLAYER_HEIGHT) )
# Игровой цикл
while True:
    # Обрабатываем выход из игры 
    for some_event in event.get():
        if some_event.type == QUIT:
            exit()
    # Отображаем картинки
    window.blit(background_image, (WINDOW_X, WINDOW_Y))
    window.blit(player_image, (PLAYER_X, PLAYER_Y))
    # Движение персонажа
    keys = key.get_pressed()
    if keys[K_d] and PLAYER_X < WINDOW_WIDTH - PLAYER_WIDTH:
        PLAYER_X += PLAYER_SPEED
    if keys[K_a] and PLAYER_X > WINDOW_X:
        PLAYER_X -= PLAYER_SPEED
    if keys[K_w] and PLAYER_Y > WINDOW_Y:
        PLAYER_Y -= PLAYER_SPEED
    if keys[K_s] and PLAYER_Y < WINDOW_HEIGHT - PLAYER_HEIGHT:
        PLAYER_Y += PLAYER_SPEED
    # Обновляем экран
    display.update()
    # Частота кадров
    clock.tick(FPS)


