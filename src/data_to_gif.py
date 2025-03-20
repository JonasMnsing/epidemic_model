import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def data_to_gif(load_path, save_path, delay_between_frames=50,
                delay_between_repeat=1000):

    # Load list of 2D arrays
    states  = np.load(load_path, allow_pickle=True)
    
    # Create a figure object for plotting, without axis and frame
    fig     = plt.figure(frameon=False)
    ax      = fig.add_axes([0,0,1,1], aspect='equal')
    ax.axis('off')

    # Create the imshow object once
    im  = ax.imshow(states[0], cmap='binary', interpolation='nearest')
    
    # List to hold the frame updates for the animation
    def update_frame(i):
        im.set_data(states[i])
        return [im]

    # Animation object and save
    writer  = animation.FFMpegWriter(fps=len(states)/delay_between_frames)
    ani     = animation.FuncAnimation(fig=fig, func=update_frame, frames=len(states),
                                        interval=delay_between_frames, repeat_delay=delay_between_repeat)
    ani.save(save_path, writer=writer)

if __name__ == '__main__':

    load_path   = "data/gol_test.npy"
    save_path   = "img/gol_test.gif"
    data_to_gif(load_path=load_path, save_path=save_path)