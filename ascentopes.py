
# (1, 2178, 9801, 19008, 20790, 14082, 6099, 1680, 282, 26, 1)
def polytope1():
    ieqs = [[10, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],
 [-1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
 [-3, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
 [-1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [-3, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
 [-1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 [-1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [-6, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
 [-1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [-6, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
 [-3, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
 [-10, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
 [34, -1, 0, 0, -1, 0, 0, 0, -1, -1, 0],
 [27, -1, 0, 0, -1, 0, 0, 0, 0, -1, 0],
 [19, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0],
 [10, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-3, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [-10, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0],
 [34, 0, -1, -1, 0, 0, -1, -1, 0, 0, 0],
 [27, 0, -1, -1, 0, 0, 0, -1, 0, 0, 0],
 [19, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0],
 [10, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
 [10, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
 [10, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
 [10, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0]]
    eqns = [[-55, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    return Polyhedron(ieqs = ieqs, eqns = eqns)

# (1, 2160, 9720, 18792, 20412, 13680, 5850, 1594, 267, 25, 1)
def polytope2():
    ieqs = [[10, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0],
 [-1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
 [-1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [-1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 [-3, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
 [-1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [-1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [-3, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
 [-6, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
 [-1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [-10, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
 [27, -1, 0, 0, 0, 0, 0, -1, 0, -1, 0],
 [10, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-3, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
 [-6, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
 [34, 0, -1, -1, -1, 0, 0, 0, -1, 0, 0],
 [10, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
 [19, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0],
 [10, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
 [10, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0],
 [19, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0],
 [10, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
 [10, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0],
 [19, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0]]
    eqns = [[-55, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    return Polyhedron(ieqs = ieqs, eqns = eqns)

# f_vector (1, 7560, 34020, 64902, 68397, 43481, 17090, 4089, 562, 39, 1)
def polytope3():
    ieqs = [[10, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],
 [-1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
 [-1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
 [-1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [-1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 [-3, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
 [-6, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
 [-10, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0],
 [-1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [-3, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
 [-1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [-3, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
 [-3, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
 [-6, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
 [-1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [-3, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
 [-6, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
 [-6, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
 [-10, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
 [40, -1, 0, 0, 0, -1, -1, -1, 0, -1, 0],
 [19, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0],
 [10, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-3, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [-10, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
 [-15, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0],
 [34, 0, -1, -1, -1, 0, 0, 0, -1, 0, 0],
 [27, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0],
 [27, 0, -1, -1, 0, 0, 0, 0, -1, 0, 0],
 [19, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0],
 [27, 0, -1, 0, -1, 0, 0, 0, -1, 0, 0],
 [19, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0],
 [19, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0],
 [10, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
 [19, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0],
 [10, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0],
 [19, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0],
 [10, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
 [10, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0]]
    eqns = [[-55, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    return Polyhedron(ieqs = ieqs, eqns = eqns)

# 39600 vertices
def polytope4():
    ieqs = [[12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0],
 [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
 [-1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [-1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 [-3, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
 [-3, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
 [-6, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
 [-6, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
 [-10, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0],
 [-1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [-1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [-1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-3, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [-6, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
 [-10, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
 [-10, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
 [-15, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0],
 [57, -1, -1, 0, -1, -1, -1, 0, 0, 0, -1, 0, 0],
 [42, -1, -1, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0],
 [-1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [23, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
 [12, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-3, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [-6, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
 [33, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0],
 [12, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-10, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
 [-15, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
 [-21, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
 [50, 0, 0, -1, 0, 0, 0, -1, -1, -1, 0, -1, 0],
 [42, 0, 0, -1, 0, 0, 0, -1, -1, -1, 0, 0, 0],
 [42, 0, 0, -1, 0, 0, 0, 0, -1, -1, 0, -1, 0],
 [33, 0, 0, -1, 0, 0, 0, 0, -1, -1, 0, 0, 0],
 [33, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, -1, 0],
 [23, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0],
 [23, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0],
 [12, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [12, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
 [23, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0],
 [12, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0],
 [12, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
 [23, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0],
 [12, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0]]
    eqns = [[-78, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    return Polyhedron(ieqs = ieqs, eqns = eqns)

# 112200 vertices
def polytope5():
    ieqs = [[12, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],
 [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
 [-1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
 [-1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [-1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [-3, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
 [-3, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
 [-6, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
 [-6, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
 [-10, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0],
 [-1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [-1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-3, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
 [-3, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 [-6, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
 [-6, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
 [-10, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0],
 [-15, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0],
 [-21, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0],
 [-21, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
 [-28, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
 [-28, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
 [-36, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
 [-36, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
 [-45, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
 [-1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [75, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0],
 [72, -1, 0, -1, -1, -1, -1, -1, -1, 0, -1, -1, 0],
 [72, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0],
 [68, -1, 0, 0, -1, -1, -1, -1, -1, 0, -1, -1, 0],
 [68, -1, 0, 0, -1, -1, -1, 0, -1, -1, -1, -1, 0],
 [63, -1, 0, 0, -1, -1, -1, 0, -1, 0, -1, -1, 0],
 [63, -1, 0, 0, 0, -1, -1, 0, -1, -1, -1, -1, 0],
 [57, -1, 0, 0, 0, -1, -1, 0, -1, 0, -1, -1, 0],
 [50, -1, 0, 0, 0, -1, -1, 0, -1, 0, -1, 0, 0],
 [42, -1, 0, 0, 0, -1, -1, 0, -1, 0, 0, 0, 0],
 [42, -1, 0, 0, 0, 0, -1, 0, -1, 0, -1, 0, 0],
 [33, -1, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0],
 [33, -1, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0],
 [23, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0],
 [23, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],
 [12, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-3, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [-6, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
 [-10, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
 [-10, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
 [-15, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0],
 [-36, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
 [-45, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
 [-45, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
 [-55, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
 [12, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [42, 0, 0, -1, -1, 0, 0, -1, 0, -1, 0, 0, 0],
 [33, 0, 0, -1, -1, 0, 0, -1, 0, 0, 0, 0, 0],
 [12, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [33, 0, 0, 0, -1, 0, 0, -1, 0, -1, 0, 0, 0],
 [23, 0, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0],
 [23, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0],
 [12, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
 [12, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
 [23, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0],
 [12, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0],
 [12, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0]]
    eqns = [[-78, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    return Polyhedron(ieqs = ieqs, eqns = eqns)

# 92880 vertices
def polytope6():
    ieqs = [[12, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0],
 [-1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
 [-1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [-3, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
 [-1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 [-3, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
 [-3, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
 [-6, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
 [-1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [-1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [-3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
 [-1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-3, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [-6, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
 [-6, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
 [-10, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0],
 [-15, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0],
 [57, -1, -1, 0, 0, 0, 0, -1, -1, -1, -1, 0, 0],
 [-1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-3, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
 [-3, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [-6, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
 [-3, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 [-6, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
 [-6, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
 [-10, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
 [12, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
 [-6, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
 [-6, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
 [-10, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
 [-6, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
 [-10, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
 [-10, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
 [-15, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
 [50, 0, -1, 0, 0, 0, 0, -1, -1, -1, -1, 0, 0],
 [42, 0, -1, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0],
 [33, 0, -1, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0],
 [33, 0, -1, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0],
 [23, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
 [33, 0, -1, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0],
 [23, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0],
 [23, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0],
 [12, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-6, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
 [-10, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
 [-10, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
 [-15, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
 [-10, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
 [-15, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
 [-15, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
 [-21, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
 [50, 0, 0, -1, -1, -1, -1, 0, 0, 0, 0, -1, 0],
 [42, 0, 0, -1, 0, -1, -1, 0, 0, 0, 0, -1, 0],
 [33, 0, 0, -1, 0, -1, -1, 0, 0, 0, 0, 0, 0],
 [12, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [12, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
 [23, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0],
 [12, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
 [33, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0],
 [23, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0],
 [23, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0],
 [12, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
 [23, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0],
 [12, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0]]
    eqns = [[-78, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    return Polyhedron(ieqs = ieqs, eqns = eqns)

# 234720 vertices
def polytope7():
    ieqs = [[14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0],
 [-1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 [-1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [-3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
 [-1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [-1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [-3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
 [-1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-3, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 [-6, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
 [-10, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
 [-1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-3, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [-10, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
 [-15, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
 [69, -1, -1, -1, 0, 0, -1, 0, 0, 0, -1, 0, 0, -1, 0],
 [60, -1, -1, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0],
 [50, -1, -1, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0],
 [-1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [-6, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
 [-10, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
 [39, -1, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0],
 [27, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-6, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [-15, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
 [14, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-3, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [14, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-6, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [-15, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
 [14, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-10, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [-21, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
 [60, 0, 0, 0, -1, -1, 0, -1, 0, -1, 0, 0, -1, 0, 0],
 [50, 0, 0, 0, -1, -1, 0, -1, 0, 0, 0, 0, -1, 0, 0],
 [50, 0, 0, 0, -1, 0, 0, -1, 0, -1, 0, 0, -1, 0, 0],
 [39, 0, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0],
 [27, 0, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
 [14, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [27, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0],
 [14, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [14, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
 [14, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
 [27, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, 0],
 [14, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0],
 [14, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0]]
    eqns = [[-105, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    return Polyhedron(ieqs = ieqs, eqns = eqns)
