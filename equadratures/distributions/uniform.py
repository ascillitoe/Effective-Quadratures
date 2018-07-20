import numpy as np
from distribution import Distribution
from recurrence_utils import jacobi_recurrence_coefficients

class Uniform(Distribution):
    """
    The class defines a Uniform object. It is the child of Distribution.
    
    :param double mean:
		Mean of the Gaussian distribution.
	:param double variance:
		Variance of the Gaussian distribution.
    """
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper
        self.bounds = np.array([self.lower, self.upper])
        self.mean = 0.5 * (self.upper + self.lower)
        self.variance = 1.0/12.0 * (self.upper - self.lower)**2
        self.skewness = 0.0
	
    def getCDF(self, N):
        """
        A uniform cumulative density function.
        :param integer N:
            Number of points for defining the cumulative density function.
        :param double lower:
            Lower bound of the support of the uniform distribution.
        :param double upper:
            Upper bound of the support of the uniform distribution.
        :return:
            An array of N equidistant values over the support of the distribution.
        :return:
            Cumulative density values along the support of the uniform distribution.
        """
        x = np.linspace(self.lower, self.upper, N)
        w = np.zeros((N, 1))
        for i in range(0, N):
            w[i] = (x[i] - self.lower)/(self.upper - self.lower)
        return x, w

    def getPDF(self, N):
        """
        A uniform probability distribution.
        :param integer N:
            Number of points for defining the probability density function.
        :param double lower:
            Lower bound of the support of the uniform distribution.
        :param double upper:
            Upper bound of the support of the uniform distribution.
        :return:
            An array of N equidistant values over the support of the distribution.
        :return:
            Probability density values along the support of the uniform distribution.
        """
        x = np.linspace(self.lower, self.upper, N)
        w = 0*x + (1.0)/(self.upper - self.lower)
        return x, w

    def getRecurrenceCoefficients(self, order):
        """
        Recurrence coefficients for the uniform distribution.
        
        :param Uniform self:
            An instance of the Uniform class.
        :param array order:
            The order of the recurrence coefficients desired.
        :return:
            Recurrence coefficients associated with the uniform distribution.
        """
        ab =  jacobi_recurrence_coefficients(0., 0., self.lower, self.upper, order)
        return ab