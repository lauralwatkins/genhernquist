#!/usr/bin/env python

import numpy as np
from astropy import units as u, constants as c
from scipy import special
from .Cumulative3D import Cumulative3D


def CircularVelocity(r, norm, rs, alpha, beta, gamma):
    
    """
    Circular velocity profile of a generalised Hernquist model.
    
    INPUTS
      r     : radial variable (requires unit)
      norm  : normalisation (requires unit)
      rs    : scale radius of model (requires unit)
      alpha : sharpness of transition between inner and outer
      beta  : outer logarithmic slope
      gamma : inner logarithmic slope
    """
    
    mass = Cumulative3D(r, norm, rs, alpha, beta, gamma)
    
    vcirc = (np.sqrt(c.G*mass/r)).to("km/s")
    
    return vcirc
