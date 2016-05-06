#!/usr/bin/env python
# -----------------------------------------------------------------------------
# GENHERNQUIST.DENSITY
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

from astropy import units as u


def density(r, norm, rs, alpha, beta, gamma):
    
    """
    Density profile of a generalised Hernquist model.
    
    INPUTS
      r     : radial variable (requires unit)
      norm  : normalisation (requires unit)
      rs    : scale radius of model (requires unit)
      alpha : sharpness of transition between inner and outer
      beta  : outer logarithmic slope
      gamma : inner logarithmic slope
    """
    
    rrs = (r/rs).to(u.dimensionless_unscaled)
    
    rho = norm*rrs**(-gamma)*(1+rrs**alpha)**((gamma-beta)/alpha)
    
    return rho
