import matplotlib.pyplot as plt # 给matplotlib.pyplot取一个别名plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.style.use('ggplot')
fig, ax = plt.subplots() # fig图对象 ax轴对象
ax.plot(input_values, squares)
# 设置图形标题并给坐标轴加上标签
ax.set_title('Squares Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Squares of Value', fontsize=14)
# 设置刻度标记的大小
ax.tick_params(labelsize=14)

plt.show()