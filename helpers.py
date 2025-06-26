import pandas as pd
import numpy as np
from mealpy.swarm_based.PSO import OriginalPSO
from pymcdm_reidentify.methods import SITW, STFN
from pymcdm.methods import TOPSIS
from pymcdm.weights import entropy_weights


def make_bounds(matrix):
    bounds = np.array([[np.min(matrix[:, i]), np.max(matrix[:, i])]
                      for i in range(matrix.shape[1])])
    return bounds


def loadData(app, file_loc):
    data = pd.read_csv(file_loc)
    if data.size == 0:
        return
    app.data_matrix = data.iloc[:, 1:].to_numpy()
    print("matrix")
    print(app.data_matrix)
    print("-----------------------------------------------")


def calculate_STFN(app):
    app.output.clear()
    types = [int(x.strip()) for x in app.types.text().split(',')]
    bounds = make_bounds(app.data_matrix)
    stoch = OriginalPSO(epoch=1000, pop_size=100)
    # expert_rank = [3, 1, 19, 20, 5, 7, 2, 12, 8,
    #                15, 4, 6, 10, 14, 9, 11, 13, 16, 17, 18]
    expert_rank = [3, 1, 9, 10, 5, 7, 2, 6, 8, 4]

    print(f"bounds: {bounds}")
    print(f"types: {types}")

    weights = entropy_weights(app.data_matrix)
    topsis = TOPSIS()
    preference = topsis(app.data_matrix, weights, types)
    rank = topsis.rank(preference)
    print(f"weights: {weights}")
    print(f"rank: {rank}")
    print(f"expert rank: {expert_rank}")

    stfn = STFN(stoch.solve, TOPSIS(), bounds)
    stfn.fit(app.data_matrix, rank, log_to=None)
    print(f"cores: {stfn.cores}")
    print(stfn())
    print(stfn)
    # print(f"model stfn: {stfn()}")

    # sitw = SITW(stoch.solve, TOPSIS(), types)
    # sitw.fit(app.data_matrix, rank, log_to=None)
    # print(f"model sitw: {sitw()}")
