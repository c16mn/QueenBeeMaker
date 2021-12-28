import time

import QBM_makoto.solve as makoto_solver
import solver_xingyaoc.solve as xingyao_solver

if __name__ == "__main__":
    letters, center = sys.argv[1], sys.argv[2]
    start = time.time()
    valid_words = makoto_solver(letters, center)
    print(valid_words)
    print("--- Makoto's solver ran in %s seconds ---" % (time.time() - start_time))
    start = time.time()
    valid_words = list(xingyao_solver(letters, center))
    print(valid_words)
    print("--- Xingyao's solver ran in %s seconds ---" % (time.time() - start_time))
