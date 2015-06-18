#!/usr/bin/env python
# -----------------------------------------------------------------------------
# GENHERNQUIST.ENCMASS
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

from numpy import *
from astropy import units as u
from scipy import special


def encmass(r, norm, rs, alpha, beta, gamma):
    
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
    
    a = (3.-gamma)/alpha
    b = (gamma-beta)/alpha
    y = (r/rs)**alpha
    
    fn = lambda x: x**a * special.hyp2f1(a, -b, 1+a, -x)/a
    
    encmass = (4*pi*norm*rs**3*fn(y.value)).to(u.Msun)
    
    return encmass
