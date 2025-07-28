import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

# y_values = []
# for x in x_values:
#     y_values.append(x**2)

plt.style.use('ggplot')
fig, ax = plt.subplots()
# ax.scatter(2, 4) # 创建一个点(2,4)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10) # s点的大小

# 设置每个坐标轴的取值范围
ax.axis([0,1100,0,1_100_000]) # 横坐标范围0~1100，纵坐标范围0~1_100_000 1_100_000=1100000
ax.ticklabel_format(style='plain')

plt.savefig('squares_plot.png', bbox_inches='tight') # bbox_inches='tight'把空白区域裁剪掉
plt.show()