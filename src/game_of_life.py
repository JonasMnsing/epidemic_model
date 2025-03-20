import numpy as np
import matplotlib.pyplot as plt

def init_random_state(n_cells_x, n_cells_y, p_alive):
    """Initialize state of the Game of Life based on shape

    Parameters
    ----------
    n_cells_x : _type_
        number of cells in x-direction
    n_cells_y : _type_
        number of cells in y-direction
    p_alive : _type_
        probability for a cell to be initialized as alive

    Returns
    -------
    _type_
        first state
    """
    # Init state as 2D Array of Zeros (dead cells)
    universe = np.zeros((n_cells_x, n_cells_y))

    # For each cell
    for i in range(n_cells_x):
        for j in range(n_cells_y):
            # Sample a random number [0,1)
            random_number = np.random.rand()

            # Set cell to alive given p_alive
            if (random_number < p_alive):
                universe[i,j] = 1

    return universe

def update_state(state):
    """Update state based on given Rule Set

    Parameters
    ----------
    state : _type_
        current system state

    Returns
    -------
    _type_
        next system state
    """
    n_cells_x   = state.shape[0]
    n_cells_y   = state.shape[1]
    state_next  = np.zeros((n_cells_x, n_cells_y))

    # For each cell
    for i in range(n_cells_x):
        for j in range(n_cells_y):

            # Number of living cells in neighborhood 
            n_alive = np.sum(state[(i-1):(i+2), (j-1):(j+2)]) - state[i,j]

            # Rule 1
            if ((state[i,j] == 1) and ((n_alive < 2) or (n_alive > 3))):
                state_next[i,j] = 0

            # Rule 2
            elif ((state[i,j] == 1) and ((n_alive == 2) or (n_alive == 3))):
                state_next[i,j] = 1

            # Rule 3
            elif ((state[i,j] == 0) and (n_alive == 3)):
                state_next[i,j] = 1

    return state_next

if __name__ == '__main__':

    n_cells_x   = 50
    n_cells_y   = 50
    p_alive     = 0.3
    n_iter      = 1000
    states      = []
    state       = init_random_state(n_cells_x=n_cells_x,
                                    n_cells_y=n_cells_y,
                                    p_alive=p_alive)
    states.append(state)
    for _ in range(n_iter-1):
        state   = update_state(state=state)
        states.append(state)

    np.save("data/gol_test.npy", states)
