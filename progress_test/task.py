from typing import Callable
import numpy as np


def trapz(x: np.ndarray, y: np.ndarray) -> float:
    """Trapezium integration"""
    return sum(
        (x[i + 1] - x[i]) * (y[i + 1] + y[i]) / 2 for i in range(len(x) - 1)
    )


def lagrangian(j: int, xp: float, xn: list[float] | np.ndarray) -> float:
    """Write a function, Lagrangian, to compute the Lagrangian polynomial
    j at a point xp, with given nodes xn.
    The function receives the values j, xp and the array of nodes xn, and
    returns the value:
    Lj(xp) = product_{k=0, k!=j}^n (xp - xk) / (xj - xk)"""
    out = 1
    for k, xk in enumerate(xn):
        if k != j:
            out *= (xp - xk) / (xn[j] - xk)

    return out


def lagr_interp(
    xn: list[float] | np.ndarray,
    yn: list[float] | np.ndarray,
    x: list[float] | np.ndarray,
) -> list[float]:
    """Write a function, LagrInterp, that receives the sets of know values,
    xn and yn, the points to be interpolated x, and returns the
    interpolated values y, by using Lagrangian polynomials."""
    out = []
    for xp in x:
        y = 0
        for j in range(len(xn)):
            y += yn[j] * lagrangian(j, xp, xn)
        out.append(y)
    return out


def splines(
    xn: list[float] | np.ndarray,
    yn: list[float] | np.ndarray,
    x: list[float] | np.ndarray,
    grad_a: float,
    grad_b: float,
) -> list[float]:
    """Write a function, Splines, that receives the sets of know values,
    xn and yn, the points to be interpolated x, the clamped boundary
    conditions y'(a), y'(b), and returns the interpolated values y,
    by using cubic splines"""
    n = len(xn)
    h = np.diff(xn)
    # create matrix for gradients
    a = np.zeros((n, n))
    d = np.zeros(n)
    a[0, 0] = 1
    a[-1, -1] = 1
    d[0] = grad_a
    d[-1] = grad_b
    for j in range(1, n - 1):
        a[j, j - 1] = 1 / h[j - 1]
        a[j, j] = 2 * (1 / h[j - 1] + 1 / h[j])
        a[j, j + 1] = 1 / h[j]
        left = (yn[j] - yn[j - 1]) / (h[j - 1] ** 2)
        right = (yn[j + 1] - yn[j]) / (h[j] ** 2)
        d[j] = 3 * (left + right)
    # solve system
    v = np.linalg.solve(a, d)
    # create matrix for coefficients
    c = np.zeros((n - 1, 4))
    for j in range(n - 1):
        dy = yn[j + 1] - yn[j]
        c[j, 0] = yn[j]
        c[j, 1] = v[j]
        c[j, 2] = 3 * dy / h[j] ** 2 - (v[j + 1] + 2 * v[j]) / h[j]
        c[j, 3] = -2 * dy / h[j] ** 3 + (v[j + 1] + v[j]) / h[j] ** 2

    # interpolate
    out = []
    for xp in x:
        for j in range(n - 1):
            if xn[j] <= xp <= xn[j + 1]:
                dx = xp - xn[j]
                out.append(
                    c[j, 0]
                    + c[j, 1] * dx
                    + c[j, 2] * dx**2
                    + c[j, 3] * dx**3
                )
                break
    return out


def simpson(h: float, yn: list[float] | np.ndarray) -> float:
    """Simpson integration"""
    return sum(
        h / 3 * (yn[i] + 4 * yn[i + 1] + yn[i + 2])
        for i in range(0, len(yn) - 2, 2)
    )


def factorial(n: int) -> int:
    """Factorial"""
    if n == 0:
        return 1
    return n * factorial(n - 1)


def choose(n: int, k: int) -> int:
    """Binomial"""
    return factorial(n) // (factorial(k) * factorial(n - k))


def derivative_fwd(
    k: int, h: float, yn: list[float] | np.ndarray
) -> list[float] | np.ndarray:
    """k-th order derivative using forward method"""
    nodes = len(yn) - k
    dx = np.ndarray(nodes)
    for n in range(nodes):
        dx[n] = sum(
            (-1) ** i * choose(k, i) * yn[n + k - i] for i in range(k + 1)
        )
    return dx / h**k


def derivative_bwd(k: int, h: float, yn: list[float] | np.ndarray):
    """k-th order derivate using backward method"""
    nodes = len(yn) - k
    dx = np.ndarray(nodes)
    for n in range(k, len(yn)):
        dx[n] = sum((-1) ** i * choose(k, 1) * yn[n - i] for i in range(k + 1))
    return dx / h**k


def fwd_euler(
    func: Callable, t0: float, y0: float, t_end: float, h: float
) -> tuple[np.ndarray, np.ndarray]:
    """Forward Euler method"""
    t: np.ndarray = np.arange(t0, t_end + h, h)
    y: np.ndarray = np.zeros(len(t))
    y[0] = y0
    for i in range(1, len(t)):
        y[i] = y[i - 1] + h * func(t[i - 1], y[i - 1])
    return t, y


def ode_rk4(
    func: Callable, t0: float, y0: float, t_end: float, h: float
) -> tuple[np.ndarray, np.ndarray]:
    """Runge-Kutta 4th order method"""
    t: np.ndarray = np.arange(t0, t_end + h, h)
    y: np.ndarray = np.zeros(len(t))
    y[0] = y0
    for i in range(1, len(t)):
        k1 = h * func(t[i - 1], y[i - 1])
        k2 = h * func(t[i - 1] + h / 2, y[i - 1] + k1 / 2)
        k3 = h * func(t[i - 1] + h / 2, y[i - 1] + k2 / 2)
        k4 = h * func(t[i - 1] + h, y[i - 1] + k3)
        y[i] = y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return t, y


# Q1
print("q1")
x = np.arange(0, 10, 1)
y = np.linspace(10, 20, 21)
z = np.ndarray(len(x) + len(y))

z[: len(x)] = x
z[-len(y) :] = y

print(z)


# Q2
print("q2")
x = np.arange(2, np.sqrt(23) + 0.01, 0.01)
y = 1 / np.sqrt(x) + np.sqrt(2 * x)
print(trapz(x, y))

# Q3
# Apply the trapezium rule with dx = dy  = 0.01, to calculate the double
# integral:
# int_0^2 int_0^1 (e^-x + cos(y)) dx dy
print("q3")
print("im kinda off for this qn")

x = np.arange(0, 1 + 0.01, 0.01)
y = np.arange(0, 2 + 0.01, 0.01)


def double_integral(dx: float) -> float:
    """Numerical integration of a double integral"""
    x_domain: np.ndarray = np.arange(0, 1, 0.01)
    y_domain: np.ndarray = np.arange(0, 2, 0.01)
    g_x: np.ndarray = np.zeros(len(x_domain))
    for i, x in enumerate(x_domain):
        z_values: np.ndarray = np.exp(-x) + np.cos(y_domain)
        # z_values[z_values < 0] = 0
        # z_values = np.sqrt(z_values)
        g_x[i] = trapz(y_domain, z_values)
    return trapz(x_domain, g_x)


print(double_integral(0.01))


# set the step intervals in x and y
dx = 0.01
dy = 0.01

# set the x range, not including the boundaries
N = len(x)
# the y range depends of the various values of x, and cannot be fixed here

# integrate in dy, for all the value of x, i.e. find G(x)

G = np.zeros(N)
# for every x
for i in range(0, N):
    # determine the boundaries m and p for this x
    # set the y points for this x, not including the boundaries
    z = np.zeros(len(y))
    # determine the values of the function z(x,y)
    for j in range(0, len(y)):
        z[j] = np.exp(-x[i]) + np.cos(y[j])

    # integrate in dy from cx to dx (for this specific x)
    G[i] = trapz(y, z)  # G(x)

# integrate G(x) in dx
print(trapz(x, G))

# Q4
print("q4")
# The three points xn = [0,1,2] are used to interpolate with Lagrange
# polynomials. What are the values of the Lagrange polynomials when
# interpolating at point xp = 1.5?
xn = [0, 1, 2]
xp = 1.5
print(lagrangian(0, xp, xn))
print(lagrangian(1, xp, xn))
print(lagrangian(2, xp, xn))


# q5
# Using the forward scheme, evaluate the derivative of the function in
# the range [1:3] with steps dt = 0.1:
# d^4/dt^4 (e^t + cos(t)^2)
# What is the value of the derivative at t = 2
print("q5")


def func(t, y):
    return np.exp(t) + np.cos(t) ** 2


h = 0.1
t = np.arange(1, 3.1, h)
y = func(t, 0)
derivatives = derivative_fwd(4, h, y)
# value at t = 2
print(derivatives[10])
