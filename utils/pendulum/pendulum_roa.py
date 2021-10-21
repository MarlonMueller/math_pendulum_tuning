from typing import Optional
import numpy as np
from utils.pendulum.safe_region import SafeRegion

class PendulumRegionOfAttraction(SafeRegion):

    """
    See SB3-Contrib REPO.
    """

    def __init__(
            self,
            A: Optional[np.ndarray] = None,
            b: Optional[np.ndarray] = None,
            vertices: Optional[np.ndarray] = None
    ):
        super(PendulumRegionOfAttraction, self).__init__(A, b, vertices)

    def __contains__(self, state):
        theta, thdot = state
        cutoff = 1 + 1e-10
        det_12 = 10.62620981660255
        max_theta = 3.092505268377452
        if (abs((theta * 3.436116964863835)/det_12) <= cutoff and
                abs((theta * 9.326603190344699 + thdot * max_theta)/det_12) <= cutoff):
             return True
        return False

    def linspace(self, num_theta=5, num_thdot=3):

        num_theta -= 1
        num_thdot -= 1

        if not (num_theta & (num_theta -1) == 0 and num_theta != 0 and
                num_thdot & (num_thdot -1) == 0 and num_thdot != 0):
            raise ValueError(f'Choose (num_theta-1) and (num_thdot-1) as powers of two')

        fac_1 = -1.
        fac_2 = 1.
        dfac_theta = 2/num_theta
        dfac_thdot = 2/num_thdot

        states = []
        max_theta = 3.092505268377452
        while fac_2 >= -1:
            while fac_1 <= 1:
                theta = fac_2 * (-max_theta)
                thdot = fac_1 * 3.436116964863835 + fac_2 * 9.326603190344699
                states.append([theta, thdot])
                fac_1 += dfac_thdot
            fac_1 = -1.
            fac_2 -= dfac_theta

        return states


    def sample(self):
        fac_1, fac_2 = self.rng.uniform(-1., 1., 2)
        max_theta = 3.092505268377452
        theta = fac_2 * (-max_theta)
        thdot = fac_1 * 3.436116964863835 + fac_2 * 9.326603190344699
        return [theta, thdot]
