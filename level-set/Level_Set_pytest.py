import pytest
from Level_Set import Level_Set
import numpy as np

class TestClass:

    def test_dist_reg_p2(self):
        # Ensure that dist_reg_p2 returns 
        ls = Level_Set('double-well')
        phi = np.array([[-2,-2.1,-2.2],[-2.1,-2.2,-2.3],[-2.1,-2.2,-2.3]])
        result = ls.dist_reg_p2(phi)
        print(len(result))
        assert len(result) == 3 and len(result[0]) == 3

