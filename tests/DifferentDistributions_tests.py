#!/usr/bin/env python
from effective_quadratures.PolyParams import PolynomialParam
from effective_quadratures.PolyParentFile import PolyParent
from effective_quadratures.IndexSets import IndexSet
import effective_quadratures.ComputeStats as stats
import numpy as np
import matplotlib.pyplot as plt
"""

    Test.

    Copyright (c) 2016 by Pranay Seshadri
"""
# Simple analytical function

def rosenbrock_fun(x):
    return (1 - x[0])**2 + 100*(x[1] - x[0]**2)**2

def main():
    no_pts_x1 = 5
    no_pts_x2 = 5
    mu = 1
    sigma = 2
    variance = sigma**2
    method = "tensor grid"
    x1 = PolynomialParam("Gaussian", [], [], mu, variance, [], no_pts_x1)
    x2 = PolynomialParam("Gaussian", [], [], mu, variance, [], no_pts_x2)
    x1x2 = []
    x1x2.append(x1)
    x1x2.append(x2)
    method = "spam"
    growth_rule = "linear"
    level = 4
    dimension = 2
    basis = IndexSet("sparse grid", [], level, growth_rule, dimension)
    uqProblem = PolyParent(x1x2, method, basis)
    pts, wts = PolyParent.getPointsAndWeights(uqProblem)

    #print pts


    x, i, f = PolyParent.getCoefficients(uqProblem, rosenbrock_fun)
    mean, variance = stats.compute_mean_variance(x, i)

    print mean, variance

    # Plot tensor grid
    #plt.scatter(pts[:,0], pts[:,1], s=70, c='b', marker='o')
    #plt.show()

    # Tensor grid
    method = "tensor grid"
    uqProblemT = PolyParent(x1x2, method)
    x, i, f = PolyParent.getCoefficients(uqProblemT, rosenbrock_fun)
    mean, variance = stats.compute_mean_variance(x, i)
    print mean, variance

main()
