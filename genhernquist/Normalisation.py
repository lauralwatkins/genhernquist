#!/usr/bin/env python

from astropy import units as u
from .Cumulative3D import Cumulative3D


def Normalisation(total, rs, alpha, beta, gamma):
    
    """
    Normalisation of a generalised Hernquist model required to have a total
    cumulative quantity.
    
    INPUTS
      total : total quantity enclosed (can have unit)
      rs    : scale radius of model (requires unit)
      alpha : sharpness of transition between inner and outer
      beta  : outer logarithmic slope
      gamma : inner logarithmic slope
    """
    
    # make a trial normalisation with units from the total and the scale radius
    trial_norm = 1*u.Quantity(total).unit/rs.unit**3
    
    # calculate the cumulative total for the trial normalisation
    trial_total = Cumulative3D(rs*1e4, trial_norm, rs, alpha, beta,
        gamma)
    
    # the normalisation for the target total is a simple rescaling
    normalisation = trial_norm*total/trial_total
    
    return normalisation
