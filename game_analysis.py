from tic_tac_toe import Board
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
import pandas as pd
import random
import numpy as np


def play_random_game(m, n, k):
    b = Board(m, n, k)

    while not b.game_over:
        moves = b.get_available_move_list()
        move = random.sample(moves, 1)[0]
        b.play_move(move[0], move[1])

    return b


def get_move_encoding(m, n):
    encode = dict()
    decode = dict()
    count = 0
    for row in range(m):
        for col in range(n):
            encode[(row, col)] = count
            decode[count] = (row, col)
            count += 1
    return encode, decode


def unroll_encoded_trajectory(b: Board, encode, decode, basis):
    traj = {'states': list(),
            'actions': list()}
    traj['states'].append(np.zeros(len(encode)))
    for ii in range(len(b.p1moves) + len(b.p2moves)):
        if ii%2 == 0:
            traj['actions'].append(basis[encode[b.p1moves[int(ii / 2)]]])
        if ii%2 == 1:
            traj['actions'].append(-basis[encode[b.p2moves[int((ii - 1) / 2)]]])
        traj['states'].append(traj['states'][ii] + traj['actions'][ii])

    return traj


def main():
    NUM_TESTS = 10000
    m = 3
    n = 3
    k = 3

    # Manual testing, ignore this
    # frame1 = np.asarray([1, 1, 1, 1, 1, 1, 1, 1, 1])
    # frame2 = np.asarray([1, -1, 1, -1, 1, -1, 1, 1, -1])

    encode, decode = get_move_encoding(m, n)
    num_actions = len(encode)
    basis = np.eye(num_actions)

    ## PCA analysis on final states:
    df = pd.DataFrame(columns=['state', 'winner'])
    for ii in range(NUM_TESTS):
        b = play_random_game(m, n, k)
        traj = unroll_encoded_trajectory(b, encode, decode, basis)
        winner = b.winner if b.winner is not None else 'None'
        winner_array = ['None' for ii in range(len(traj['states']))]
        winner_array[-1] = winner

        series = [pd.Series([traj['states'][ii], winner_array[ii]], index=df.columns) for ii in range(len(traj['states']))]
        df = df.append(series, ignore_index=True)

    vecs = np.zeros((len(df), 9))
    for i in range(len(df)):
        vecs[i, :] = df['state'][i]
    pca = PCA(n_components=2)
    pca.fit(vecs)
    vecs = pca.transform(vecs)
    print(df.state[0])
    df['comp1'] = [vecs[ii, 0] for ii in range(len(df))]
    df['comp2'] = [vecs[ii, 1] for ii in range(len(df))]

    print(df.head(5))
    plt.figure()
    sns.scatterplot(data=df, x='comp1', y='comp2', hue='winner', palette=['gray', 'r', 'b'], alpha=0.6)
    plt.title('PCA scattering plot of state labels')
    plt.show()



if __name__ == '__main__':
    main()
