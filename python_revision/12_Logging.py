'''
It allows us to record progress and problems
It has 6 levels: Notset, Debug, Info, Warning, Error, Critical
'''

import logging
import math

# Creating and configuring the logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "log.txt",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = 'w')
logger = logging.getLogger()

# Test message:
logger.debug('This is a harmless debug message.')
logger.info('Just some useful info.')
logger.warning("No warnings")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down")


def quadratic_formula(a,b,c):
    '''Returns the solution of the quadratic formula ax^2 + bx + c = 0.'''
    logger.info("quadratic_formula({0},{1},{2})".format(a,b,c))

    # Computing the discriminant:
    logger.debug("# Compute the discriminant")
    disc = b**2 - 4*a*c

    # Compute the 2 roots
    logger.debug('# Compute the 2 roots')
    root1 = (-b + math.sqrt(disc))/(2*a)
    root2 = (-b - math.sqrt(disc))/(2*a)

    # Returning the roots:
    logger.debug("#Return the roots")
    return(root1,root2)


roots = quadratic_formula(1,0,-1)
print(roots)



