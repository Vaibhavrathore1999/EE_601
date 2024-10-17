import numpy as np

x = np.array([0,15,30,45,60])
y = np.array([0,8,15,19,20])
a = np.sum(x**4)
b = np.sum(x**3)
c = np.sum(x**2)
d = np.sum(x)
A = np.array([[a,b,c],[b,c,d],[c,d,5]])
b = np.array([np.sum(x**2*y), np.sum(x*y), np.sum(y)])

coeff = np.dot(np.linalg.inv(A), b)
print(coeff)

def y1(x):
    return coeff[0]*x**2 + coeff[1]*x + coeff[2]

print(y1(122))


def lagrange_interpolation(x, y, target_x):
    """
    Lagrange interpolation to find the value of the polynomial at a given point.
    
    Parameters:
    x (list): List of x-values (known data points).
    y (list): List of y-values corresponding to the x-values.
    target_x (float): The point at which to interpolate the polynomial.
    
    Returns:
    float: Interpolated value at the target_x.
    """
    n = len(x)
    result = 0.0
    
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (target_x - x[j]) / (x[i] - x[j])
        result += term
    
    return result

# Interpolate at x = 2.5
target_x = -31
interpolated_value = lagrange_interpolation(x, y, target_x)
print(interpolated_value)

