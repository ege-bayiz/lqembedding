import numpy as np

class Dynamics:
    def __init__(self):
        self.A = np.zeros(1)
        self.Bs = np.zeros(1)

def solve_lq_feedback(dyn:Dynamics, costs:np.Array, horizon:int):

    N = len(costs)
    t = horizon
    Zs = []
    Fs = []
    Ps = dict()
    for i in  range(N):
        Zs.append(costs[i].Q)
        Fs.append(np.zeros((dyn.A.size[0], dyn.A.size[1])))
        Ps[i] = np.zeros((dyn.Bs[i].size[1], dyn.Bs[i].size[0], horizon))

    while t > 0:
        #Evaluate P^i_t
        P_temp = compute_feedbacks(dyn, costs, Zs)
        for i in range(N):
            Ps[i][:,:,t] = P_temp[i]

        #Update Fs
        sum = np.zeros((dyn.A.size[0], dyn.A.size[1]))
        for j in range(N):
            sum += dyn.Bs[j] * Ps[j][:,:,t]

        Fs = dyn.A - sum

        #Update Zs
        for i in range(N):
            sum = np.zeros(costs[i].Q.size[0], costs[i].Q.size[1])
            for j in range(N):
                if j in costs[i].Rs:
                    sum += np.transpose(Ps[j][:,:,t]) * (costs[i].Rs[j] * Ps[j][:,:,t])
            Zs[i] = costs[i].Q + sum + np.transpose(Fs) * Zs[i] * Fs

    t -= 1

    return Ps

def compute_feedbacks(dyn:Dynamics, costs, Zs):
    N = len(costs)
    # constructing matrices
    M_matrix = []
    b_matrix = []
    for i in range(N):
        M_row = []
        for j in range(N):
            if i == j:
                M_row.append(costs[i].Rs[i] + np.transpose(dyn.Bs[i]) * Zs[i] * dyn.Bs[i])
            else:
                M_row.append(np.transpose(dyn.Bs[i]) * Zs[i] * dyn.Bs[j])
        M_matrix.append(M_row)
        b_matrix.append(np.transpose(dyn.Bs[i]) * Zs[i] * dyn.A)

    M_matrix = np.asarray(M_matrix)
    b_matrix = np.asarray(b_matrix)

    #solving for P
    P = np.linalg.solve(M_matrix, b_matrix)

    #splitting P back to each player
    Ps = []
    for i in range(N-1):
        action_dim = dyn.Bs[i].size()[2]
        Ps.append(P[1:action_dim, :])
        P = P[action_dim + 1:, :]

    Ps.append(P)

    return Ps


