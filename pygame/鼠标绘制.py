import pygame
import sys

# 初始化pygame
pygame.init()

# 设置窗口大小
win_size = (800, 600)
screen = pygame.display.set_mode(win_size)

# 设置颜色（RGB）
WHITE = (255, 255, 255)  # 修正背景色为白色
RED = (255, 0, 0)

# 变量来跟踪是否正在绘制
drawing = False
# 列表来存储线条的点
lines = []

# 创建一个时钟对象来控制帧率
clock = pygame.time.Clock()

# 游戏主循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左键按下
                drawing = True
                lines.append([(event.pos[0], event.pos[1])])  # 开始新线条
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # 左键释放
                drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                mouse_pos = event.pos
                # 追加当前点到当前线条的列表中
                lines[-1].append((mouse_pos[0], mouse_pos[1]))

                # 填充背景颜色
    screen.fill(WHITE)

    # 绘制所有线条
    for line in lines:
        for i in range(1, len(line)):
            pygame.draw.line(screen, RED, line[i - 1], line[i], 5)

            # 更新显示
    pygame.display.flip()

    # 设置帧率
    clock.tick(60)

# 退出pygame
pygame.quit()
sys.exit()