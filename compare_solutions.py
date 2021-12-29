import time
import sys

import QBM_makoto as makoto_solver
import solver_xingyaoc as xingyao_solver

if __name__ == "__main__":
    letters, center = sys.argv[1], sys.argv[2]
    start = time.time()
    valid_words_xc = list(xingyao_solver.solve(letters, center))
    # print(valid_words)
    print("--- Xingyao's solver ran in %s seconds ---" % (time.time() - start))
    start = time.time()
    valid_words_mn = makoto_solver.solve(letters, center)
    # print(valid_words)
    print("--- Makoto's solver ran in %s seconds ---" % (time.time() - start))


    xingyao_solver.evaluator(valid_words_mn)
    xingyao_solver.evaluator(valid_words_xc)
