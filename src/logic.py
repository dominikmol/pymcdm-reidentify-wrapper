import re
import numpy as np

np.set_printoptions(suppress=True, precision=4, linewidth=100)

def make_bounds(data_matrix):
    bounds = np.array([[np.min(data_matrix[:, i]), np.max(data_matrix[:, i])]
                      for i in range(data_matrix.shape[1])])
    return bounds

def parse_bounds_from_text(text):
    matches = re.findall(r'\(([^,]+),\s*([^)]+)\)', text)
    bounds = np.array([[float(x), float(y)] for x, y in matches])
    return bounds

def rw(rankx, ranky, n):
    suma = 0
    for i in range(n):
        suma += ((
            (rankx[i]-ranky[i])**2)
            *((n-rankx[i]+1)+(n-ranky[i]+1)
                    ))
    suma = 6 * suma
    denominator = n**4 + n**3 - n**2 - n
    if denominator == 0:
        return 0
    suma = suma / denominator
    return 1-suma

def WS(rankx, ranky, n):
    suma = 0
    for i in range(n):
        eq = 2 ** (-float(rankx[i]))
        eq2 = abs(rankx[i] - ranky[i]) / max(abs(1 - rankx[i]), abs(n - rankx[i]))
        suma += eq * eq2
    return 1 - suma