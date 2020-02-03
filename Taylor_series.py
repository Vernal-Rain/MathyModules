#Elaine Lee
#Dec 2019

'''Implementing Taylor series using recursion'''


from math import *

def f(x):
    return sin(x) #just an example function

def nth_deriv(function, pt, n):
    if n==0:
        return function(pt)
    else:
        step = 0.001
        
        '''
        #Using loop:
        start = pt - (n/2)*step
        pts = [start+i*step for i in range(n+1)]
        f_pts = []
        for i in range(n):
            f_pts.append((function(pts[i+1]) - function(pts[i]))/step)
        for j in range(n-1):
            for i in range(len(f_pts) - 1):
                f_pts[i] = (f_pts[i+1] - f_pts[i])/step
            f_pts.pop()
            
        return f_pts[0]'''
        
        return (nth_deriv(function, pt+step, n-1) - nth_deriv(function, pt-step, n-1))/(2*step)

def taylor(f, x, a, n):
    if n == 0:
        return f(a)
    else:
        return nth_deriv(f, a, n) * (x-a)**n / factorial(n) + taylor(f, x, a, n-1)
    

#Testing it out...
if __name__ == "__main__":
    for i in range(10):
        print (str(i)+"th deriv:", nth_deriv(f, pi/2, i))

    print ("Using approx: " + str(taylor(f, pi/2+0.01, pi/2, 5)))
        
    print ("Actual: " + str(f(pi/2+0.01)))
