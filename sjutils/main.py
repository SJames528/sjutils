import numpy as np

def quickintegrate(x, y):
    '''
    method to perform a quick integration by trapezium rule on two arrays
    Input:
    :param x: array - points along x-axis for integration. Need not be regularly spaced
    :param y: array - heights along y-axis for integration
    '''
    #ensure x and y in correct format
    try:
        x = np.array(x)
        y = np.array(y)
        #need x and y as 1-D arrays - TODO_yellow: change later to allow for 2-D arrays or y as a function
        assert len(x.shape) == 1
        assert len(y.shape) == 1
    except:
        raise Exception("Please provide x and y as 1-D arrays")

    #reformat x and y into difference/sum arrays for area calculation by trapezium rule
    x_ = x[1:] - x[:-1]
    y_ = y[1:] + y[:-1]
    area = np.sum(x_*y_*0.5)

    return area
