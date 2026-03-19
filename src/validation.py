def checkIfSTFNReady(app):
    to_check = [app.data_matrix, app.bounds, app.weights, app.expert_rank]
    for item in to_check:
        if item is None:
            return False
    return True


def checkIfPSOReady(pop_size, epoch, c1, c2, w):
    if pop_size <= 0 or epoch <= 0:
        return False
    if not (0 < c1 < 4) or not (0 < c2 < 4) or not (0 < w < 1):
        return False
    return True


def checkIfMCDAReady(app):
    if app.stfn is None:
        return False
    if app.mcda_method is None:
        return False
    return True

def checkIfRankReversalReady(app):
    to_check = [app.stfn, app.expert_rank, app.data_matrix, app.bounds, app.stfn_mcda_body]
    for item in to_check:
        if item is None:
            return False
    return True