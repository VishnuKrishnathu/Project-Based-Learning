from scipy.integrate import odeint
import numpy
import matplotlib.pyplot as plt
import math

def model(x,t,K,F,m, c):
    x1 = x[0]
    x2 = x[1]
    dx1_dt = x2
    dx2_dt = (F-(c*x2)-(K*x1))/m
    dx_dt = [dx1_dt, dx2_dt]
    return dx_dt

def main(value, number,zeta):
    K = float(value[number-1].konstant)
    F = (value[number-1].mass+0.005)*9.81
    m = value[number-1].mass
    displacement = value[number-1].static
    try:
        c = zeta*2*(math.sqrt(K*m))
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    except UnboundLocalError:
        pass
    time = (float(value[number-1].time))*10

    x_1 = [displacement, 0]
    t = numpy.linspace(0,time, 100)
    x = odeint(model, x_1, t, args = (K, F, m, c))

    plt.plot(t, x[:, 0])
    plt.show()
