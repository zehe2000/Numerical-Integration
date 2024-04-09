import argparse
import math

def trapezoidal_integration (lower_limit, upper_limit, f, n):
    h= (upper_limit-lower_limit)/n
    res=0
    for i in range(0,n):
        x_i=lower_limit+i*h
        x_next=lower_limit+(i+1)*h
        res+=h*((f(x_i)+f(x_next))/2)

    return res

def main():
    parser = argparse.ArgumentParser(description="Trapezoidal integration.")
    parser.add_argument('lower_limit', type=float, help='Lower limit of integration')
    parser.add_argument('upper_limit', type=float, help='Upper limit of integration')
    parser.add_argument('n', type=int, help='Number of trapezoids')
    args = parser.parse_args()

    def f(x):
        return math.exp(x)
    
    result = trapezoidal_integration(args.lower_limit, args.upper_limit, f, args.n)
    print(f"The solution of integration is: {result}")

if __name__ == "__main__":
    main()