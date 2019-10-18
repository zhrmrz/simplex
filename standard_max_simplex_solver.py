import numpy as np
class StandardMaximizationSimplexSolver:
    def make_matrix(self,factor_of_z,factor_of_eqs,ans_of_eqs):
        factor_of_z *= -1
        num_of_cols = np.size(factor_of_eqs, 1)
        i = np.eye(num_of_cols, dtype=float)
        res=np.vstack((factor_of_eqs,factor_of_z))
        simplex_table = np.concatenate((res, i, ans_of_eqs), axis=1)
        return simplex_table


    def standard_maximization_simplex_solver(self,simplex_table):
        while True:
            last_row = []
            last_row.append(simplex_table[-1])
            entring_col =np.argmin(last_row)
            m=[]
            n=[]
            for i,x in enumerate (simplex_table[:,-1]):
               if x > 0 and simplex_table[i, entring_col] > 0:
                  m.append(x / simplex_table[i, entring_col])
                  n.append(i)
            departing_row=n[m.index(min(m))]
            pivot=simplex_table[departing_row,entring_col]
            simplex_table[departing_row]=simplex_table[departing_row]/pivot
            for i in range(0,np.size(simplex_table,0)):
                if i==departing_row:
                   continue
                r=departing_row*simplex_table[i,entring_col]*-1
                simplex_table[i]+=r*simplex_table[departing_row]
                if not(min(simplex_table[-1]) < 0):
                    return simplex_table


if __name__ == '__main__':
    factor_of_z = np.array([8, 10, 7])

    factor_of_eqs = np.array([[1, 3, 2],
                              [1, 5, 1]
                             ])

    ans_of_eqs = np.array([[10],
                            [8],
                            [0]])
    p1 = StandardMaximizationSimplexSolver()
    simplex_table=p1.make_matrix(factor_of_z, factor_of_eqs, ans_of_eqs)
    print(p1.standard_maximization_simplex_solver(simplex_table))






