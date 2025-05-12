import scipy
import numpy as np

def gaus(fwidth, data_orig):
    sigma = fwidth / np.sqrt(12.0)
    data_filtered = scipy.ndimage.gaussian_filter(data_orig, sigma=sigma, mode='reflect', radius=100)
    return data_filtered