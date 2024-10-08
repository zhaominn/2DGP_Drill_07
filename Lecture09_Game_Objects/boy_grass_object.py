from pico2d import *
import random

# Game object class here
class Grass:
    # 생성자 함수 : 객체의 초기 상태를 설정
    def __init__(self):
    # 모양 없는 납작한 붕어빵의 초기 모습 결정
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x, self.y =  random.randint(100, 700), 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = random.randint(0, 7)
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.x, self.y =  random.randint(100, 700), 599
        self.frame = 0
        self.imagenum= random.randint(0, 1)
        if self.imagenum==0:
            self.image = load_image('ball41x41.png')
        elif self.imagenum == 1:
            self.image = load_image('ball21x21.png')

    def update(self):
        if self.imagenum==0:
            if self.y>=70:
                self.y -= random.randint(4, 6)
        if self.imagenum==1:
            if self.y>=60:
                self.y -= random.randint(3, 5)

    def draw(self):
        if self.imagenum==0:
            self.image.clip_draw(0, 0, 41, 41, self.x, self.y)
        elif self.imagenum == 1:
            self.image.clip_draw(0, 0, 21, 21, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global team
    global balls

    running = True
    grass = Grass() # 잔디를 찍어낸다. 생성한다.
    team=[Boy() for i in range(11)]
    balls=[Ball() for i in range(20)]

def update_world():
    grass.update() # 객체의 상태를 업데이트, 시뮬레이션
    for boy in team:
        boy.update()
    for ball in balls:
        ball.update()

def render_world():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()
    update_canvas()

running = True

open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    # game logic
    handle_events()
    update_world() # 상호작용을 시뮬레이션
    render_world() # 그 결과를 보여준다
    delay(0.05)


close_canvas()
