#!/usr/bin/env python
# -----------------------------------------------------------------------------
# GENHERNQUIST.DENSITY
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------


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
    
    rho = norm*(r/rs)**(-gamma)*(1+(r/rs)**alpha)**((gamma-beta)/alpha)
    
    return rho
