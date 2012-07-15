# Same as basic_example, but writes files using a single MovieWriter instance
# without putting on screen
# -*- noplot -*-
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update_line(num, data, line):
    line.set_data(data[...,:num])
    return line,

# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)


fig1 = plt.figure()

data = np.random.rand(2, 25)
l, = plt.plot([], [], 'r-')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('x')
plt.title('test')
line_ani = animation.FuncAnimation(fig1, update_line, 25, fargs=(data, l),
    interval=50, blit=True)
line_ani.save('lines.mp4', writer=writer)

fig2, ax = plt.subplots()

x = np.arange(-9, 10)
y = np.arange(-9, 10).reshape(-1, 1)
base = np.hypot(x, y)
ims = []
for add in np.arange(15):
    ax.cla() # clear the last frame
    im = ax.pcolor(x, y, base + add, norm=plt.Normalize(0, 30))
    ims.append([im])

im_ani = animation.ArtistAnimation(fig2, ims, interval=50, repeat_delay=3000)
im_ani.save('im.mp4', writer=writer)

# Set up formatting for the movie files
Writer = animation.writers['ffmpeg_file']

# we can force ffmpeg to make webm movies if we use -f webm and no
# codec.  webm works by default on chrome and firefox; these will
# display inline in the ipython notebook

#writer = Writer(fps=15, codec='None', extra_args=['-f', 'webm'])
# im_ani.save('movies/im2.webm', writer=writer)