C FILE: ext_fortran.f
      SUBROUTINE SQUARE(B, X)
      REAL B
      REAL X
Cf2py intent(in) x
Cf2py intent(out) b
      B = X * X
      END
C END FILE ext_fortran.f