#!/usr/bin/env python


def VolumeDensitySlope(r, rs, alpha, beta, gamma):
    
    """
    The slope of the density profile of a generalised Hernquist model.
    
    INPUTS
      r     : radial variable (requires unit)
      rs    : scale radius of model (requires unit)
      alpha : sharpness of transition between inner and outer
      beta  : outer logarithmic slope
      gamma : inner logarithmic slope
    """
    
    slope = -gamma + (gamma-beta)*r**alpha/(rs**alpha + r**alpha)
    
    return slope