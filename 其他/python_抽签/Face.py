import pygame,sys
import math
import random

pygame.init()  # 初始化pygame类
screen = pygame.display.set_mode((600, 600))  # 设置窗口大小
pygame.display.set_caption('幸运大转盘')  # 设置窗口标题
tick = pygame.time.Clock()
fps = 10  # 设置刷新率，数字越大刷新率越高
picture = pygame.transform.scale(pygame.image.load("./幸运大转盘.png"), (600, 600))
bg=picture.convert()
picture = pygame.transform.scale(pygame.image.load("./1.png"), (30, 230))
hand = picture.convert_alpha()

rewardDict = {
    'first level': (0, 0.03),
    'second level': (0.03, 0.2),
    'third level': (0.2, 1)
}
def rewardFun():
    """用户的得奖等级"""
    # 生成一个0～1之间的随机数
    number = random.random()
    # 判断随机转盘是几等奖
    for k, v in rewardDict.items():
        if v[0] <= number < v[1]:
            return k

def start():
    while True:
        for event in pygame.event.get():

            # 处理退出事件
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                else:
                    return
        screen.blit(bg,(0,0))
        newRect = hand.get_rect(center=(300,150))
        screen.blit(hand,newRect)

        pygame.draw.circle(screen,(255,255,0),(300,300),50)

        textFont = pygame.font.Font("./font.ttf", 80)
        textSurface = textFont.render("go", True, (110, 55, 155))
        screen.blit(textSurface, (270, 230))
        pygame.display.update()

def middle():
    angle = 0
    while True:
        posx = 300 + int(150 * math.sin(angle * math.pi / 180))
        posy = 300 - int(150 * math.cos(angle * math.pi / 180))
        print(posx, posy, math.sin(angle * math.pi / 180))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(bg,(0,0))

        newhand = pygame.transform.rotate(hand, -angle)

        newRect = newhand.get_rect(center=(posx,posy))
        screen.blit(newhand,newRect)
        pygame.draw.circle(screen,(255,255,0),(300,300),50)

        angle += 10

        if angle > 500:
            k = rewardFun()
            end(k)
            break

        tick.tick(fps)
        pygame.display.flip()  # 刷新窗口


def end(k):
    textFont = pygame.font.Font("./font.ttf", 50)
    print("恭喜你，你抽中了"+k)
    textSurface = textFont.render("your awards is ：%s" % k, True, (110, 55, 155))
    screen.fill((155, 155, 0))
    screen.blit(textSurface, (30, 230))


if __name__ == '__main__':
    start()
    middle()
