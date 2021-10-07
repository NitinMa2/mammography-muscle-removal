import pytest
import numpy as np
import cv2
from Region_Growing import Region_Growing

class TestClass:
    def test_explore_neighbours_with_conn_4_middle(self):
        image_data = cv2.imread("mdb001.pgm", 0)
        rg = Region_Growing(image_data, 6200, threshold=40, conn=4)
        unexplored_neighbours = rg.explore_neighbours([], (1,1))
        assert unexplored_neighbours == [(2, 1), (1, 2), (0, 1), (1, 0)]

    def test_explore_neighbours_with_conn_4_top(self):
        image_data = cv2.imread("mdb001.pgm", 0)
        rg = Region_Growing(image_data, 6200, threshold=40, conn=4)
        unexplored_neighbours = rg.explore_neighbours([], (0,1))
        assert unexplored_neighbours == [(1, 1), (0, 2), (0, 0)]
    
    def test_explore_neighbours_with_conn_4_left_most(self):
        image_data = cv2.imread("mdb001.pgm", 0)
        rg = Region_Growing(image_data, 6200, threshold=40, conn=4)
        unexplored_neighbours = rg.explore_neighbours([], (1,0))
        assert unexplored_neighbours == [(2, 0), (1, 1), (0, 0)]

    def test_explore_neighbours_with_conn_4_top_left(self):
        image_data = cv2.imread("mdb001.pgm", 0)
        rg = Region_Growing(image_data, 6200, threshold=40, conn=4)
        unexplored_neighbours = rg.explore_neighbours([], (0,0))
        assert unexplored_neighbours == [(1,0), (0,1)]

    def test_explore_neighbours_with_conn_8_middle(self):
        image_data = cv2.imread("mdb001.pgm", 0)
        rg = Region_Growing(image_data, 6200, threshold=40, conn=8)
        unexplored_neighbours = rg.explore_neighbours([], (1,1))
        assert unexplored_neighbours == [(2, 1), (2, 2), (1, 2), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0)]

    def test_explore_neighbours_with_conn_8_top(self):
        image_data = cv2.imread("mdb001.pgm", 0)
        rg = Region_Growing(image_data, 6200, threshold=40, conn=8)
        unexplored_neighbours = rg.explore_neighbours([], (0,1))
        assert unexplored_neighbours == [(1, 1), (1, 2), (0, 2), (0, 0), (1, 0)]
    
    def test_explore_neighbours_with_conn_8_left_most(self):
        image_data = cv2.imread("mdb001.pgm", 0)
        rg = Region_Growing(image_data, 6200, threshold=40, conn=8)
        unexplored_neighbours = rg.explore_neighbours([], (1,0))
        assert unexplored_neighbours == [(2, 0), (2, 1), (1, 1), (0, 1), (0, 0)]

    def test_explore_neighbours_with_conn_8_top_left(self):
        image_data = cv2.imread("mdb001.pgm", 0)
        rg = Region_Growing(image_data, 6200, threshold=40, conn=8)
        unexplored_neighbours = rg.explore_neighbours([], (0,0))
        assert unexplored_neighbours == [(1, 0), (1, 1), (0, 1)]

    def test_get_nearest_neighbour(self):
        sample_image = np.array([[0,1,0],[2,0,3],[0,4,0]])
        rg = Region_Growing(sample_image, 6200, threshold=40, conn=4)
        result = rg.get_nearest_neighbour([(0,1), (1,0), (1,2), (2,1)], 5)
        assert result == (3, 1)

    def test_is_pixel_inside_image_within(self):
        image_data = cv2.imread("mdb001.pgm", 0)
        rg = Region_Growing(image_data, 6200, threshold=40, conn=4)
        result = rg.is_pixel_inside_image((1,1), (255,192))
        assert result == True

    def test_is_pixel_inside_image(self):   
        image_data = cv2.imread("mdb001.pgm", 0)
        rg = Region_Growing(image_data, 6200, threshold=40, conn=4)
        result = rg.is_pixel_inside_image((256,1), (255,192))
        assert result == False
