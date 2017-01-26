import numpy as np
from scipy.optimize import linprog

# Constraint 1:  1(y0)+3(y1)=>6
# Constraint 2:  2(y0)+1(y1)=>3
# Min.:        w=3(y0)+2(y1)

# When the constraints are greater than, we must make the values
# in both of those variables negative so that they evaluate correctly.

upper_bounds = np.array([
    [1, 3],
    [2, 1] 
])

ub_constraints_row = np.array([6, 3])  # Fab and Finish caps, totals or right-hand-side

# Moved the obj values to the left side of the equation to match the upper bounds above
objective = np.array([3, 2])  #so now -130(x1)-160(x2)+z=0

y0_bounds = (0, None)
y1_bounds = (0, None)

result = linprog(c=objective,
                 A_ub=-upper_bounds,
                 b_ub=-ub_constraints_row,
                 bounds=(y0_bounds,
                         y1_bounds
                         )
                )

# The optimal value is negative because we moved the obj values. So make it positive
print "Optimal Value: %s" % (result.fun)  
print "Parameters at Optimal Value: %s" % result.x


#############################
# My own explorations of Theorem of Duality
x0_bounds = (0.0, None)
x1_bounds = (0.0, None)

result = linprog(c=(-1*ub_constraints_row),
                 A_ub=(np.transpose(upper_bounds)),
                 b_ub=(objective),
                 bounds=(x0_bounds,
                         x1_bounds
                         )
                )

# The optimal value is negative because we moved the obj values. So make it positive
print "Optimal Value: %s" % (result.fun * -1)  
print "Parameters at Optimal Value: %s" % result.x