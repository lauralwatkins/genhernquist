#!/usr/bin/env python

import numpy as np
from astropy import units as u
from scipy import special


def Cumulative3D(r, norm, rs, alpha, beta, gamma):
    
    """
    Enclosed mass profile of a generalised Hernquist model.
    
    INPUTS
      r     : radial variable (requires unit)
      norm  : normalisation (requires unit)
      rs    : scale radius of model (requires unit)
      alpha : sharpness of transition between inner and outer
      beta  : outer logarithmic slope
      gamma : inner logarithmic slope
    """
    
    # base units of volume density and their powers
    bases = np.array(norm.unit.bases)
    powers = np.array(norm.unit.powers)
    
    # length unit for volume
    length_unit = bases[powers==-3][0]
    
    
    a = (3-gamma)/alpha
    b = (gamma-beta)/alpha
    y = ((r/rs).to(u.dimensionless_unscaled).value)**alpha
    
    fn = lambda x: x**a * special.hyp2f1(a, -b, 1+a, -x)/a
    
    cumulative = 4*np.pi*norm*rs.to(length_unit)**3*fn(y)/alpha
    
    return cumulative
