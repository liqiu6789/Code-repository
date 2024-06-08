import matplotlib.pyplot as plt
import numpy as np


def create_waffle_chart(categories, values, height, width, colormap):
    total_values = sum(values)
    category_proportions = [value / total_values for value in values]

    total_num_tiles = width * height
    tiles_per_category = [round(proportion * total_num_tiles) for proportion in category_proportions]

    waffle_chart = np.zeros((height, width))

    category_index = 0
    tile_index = 0

    for row in range(height):
        for col in range(width):
            tile_index += 1

            if tile_index > sum(tiles_per_category[:category_index + 1]):
                category_index += 1

            waffle_chart[row, col] = category_index

    fig, ax = plt.subplots()
    colormap = plt.cm.get_cmap(colormap)
    ax.matshow(waffle_chart, cmap=colormap)
    plt.colorbar(ax.matshow(waffle_chart, cmap=colormap))

    ax.set_xticks(np.arange(-0.5, (width), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, (height), 1), minor=True)
    ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

    ax.tick_params(which='minor', size=0)

    legend_handles = [plt.Rectangle((0, 0), 1, 1, color=colormap(i / len(categories))) for i in range(len(categories))]
    plt.legend(legend_handles, categories, loc='lower center', ncol=len(categories), bbox_to_anchor=(0.5, -0.2))

    plt.title('Waffle Chart')
    plt.show()


# 示例数据
categories = ['类别 A', '类别 B', '类别 C']
values = [50, 30, 20]
colormap = 'tab20'

# 绘制华夫饼图
create_waffle_chart(categories, values, height=10, width=10, colormap=colormap)
