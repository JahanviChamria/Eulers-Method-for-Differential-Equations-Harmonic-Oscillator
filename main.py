import numpy as np
import matplotlib.pyplot as plt

print('''FOR A HARMONIC OSCILLATOR WITH A DRIVING FORCE:
\u03B8''(t) + b\u03B8'(t) + csin(\u03B8(t)) + dsin(wt)= 0
Here, b is the damping parameter and c is determined by the pendulum length (c = g/l).''')
def eulerODE2(f, t0, y00, y10, nmax, h):
    #f: Function
    #t0: Starting time
    #y00: Starting value of y(t)
    #y10: starting value of y'(t)
    #nmax: Number of iterations
    #h: Stepsize
    y0=y00
    y1=y10
    t=t0
    t_values=[t]
    y0_values=[y0]
    y1_values=[y1]
    for i in range(1, nmax+1):
        y0=y0 + y1 * h
        y1 = y1 + f(t,y0,y1) * h
        t=t+h
        t_values.append(t)
        y0_values.append(y0)
        y1_values.append(y1)
    return np.array([t_values, y0_values, y1_values])

#pendulum geometry
length=float(input("Enter the length of the pendulum: "))
c=9.81/length

#damping
b=float(input("Enter the damping value: "))
d=float(input("Enter the frequency of the driving force: "))
omega=float(input("Enter the value of omega: "))

def f_ODE(t,theta0,theta1):
    return -b*theta1 - c*np.sin(theta0) - d*np.sin(omega*t)

t0=float(input("Enter the starting time: "))
theta00=float(input("Enter the starting value of \u03B8(t): "))
theta10=float(input("Enter the starting value of \u03B8'(t): "))
nmax=int(input("Enter the number of iterations: "))
h=float(input("Enter the stepsize: "))

solution=eulerODE2(f_ODE, t0, theta00, theta10, nmax, h)

plt.xlabel('t')
plt.ylabel('theta')
plt.plot(solution[0], solution[1])
plt.show()