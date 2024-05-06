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
# 列表来存储线条的点及宽度
lines = []
# 初始化画笔大小
line_width = 5

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
                lines.append({'points': [(event.pos[0], event.pos[1])], 'width': line_width})  # 开始新线条
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # 左键释放
                drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                mouse_pos = event.pos
                # 追加当前点到当前线条的列表中
                lines[-1]['points'].append((mouse_pos[0], mouse_pos[1]))
        elif event.type == pygame.KEYDOWN:
            if not drawing and lines:  # 确保不在绘制状态且至少有一条线条
                last_line_index = len(lines) - 1
                if event.key == pygame.K_UP and lines[last_line_index]['width'] < 10:  # 增大画笔
                    lines[last_line_index]['width'] += 1
                elif event.key == pygame.K_DOWN and lines[last_line_index]['width'] > 1:  # 减小画笔
                    lines[last_line_index]['width'] -= 1

                    # 填充背景颜色
    screen.fill(WHITE)

    # 绘制所有线条，使用它们各自的宽度
    for line_data in lines:
        points = line_data['points']
        line_width = line_data['width']
        for i in range(1, len(points)):
            pygame.draw.line(screen, RED, points[i - 1], points[i], line_width)

            # 更新显示
    pygame.display.flip()

    # 设置帧率
    clock.tick(60)

# 退出pygame
pygame.quit()
sys.exit()