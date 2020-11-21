''' Symbolic formulae for quaternions '''

from sympy import Symbol, cos, sin, acos, sqrt, simplify, trigsimp
from sympy.matrices import Matrix


def qoperate(q1, q2, operator):
    '''Apply the given operator on the 2 quaternions
    operator : "+" or "-" are supported currently
    '''
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    if operator == "+":
        q = w1+w2, x1+x2, y1+y2, z1+z2
    if operator == "-":
        q = w1-w2, x1-x2, y1-y2, z1-z2

    return q


#Send the quaternions in reverse order, this is what I noticed.
#I mean the first quaternion should be the second rotation applied in succession
#Okay, I got it. They are doing body-fixed rotation by default. So, it's corrent.
def qmult(q1, q2):
    ''' Multiply two quaternions

    Parameters
    ----------
    q1 : 4 element sequence
    q2 : 4 element sequence

    Returns
    -------
    q12 : shape (4,) array

    Notes
    -----
    See : http://en.wikipedia.org/wiki/Quaternions#Hamilton_product
    '''
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1*w2 - x1*x2 - y1*y2 - z1*z2
    x = w1*x2 + x1*w2 + y1*z2 - z1*y2
    y = w1*y2 + y1*w2 + z1*x2 - x1*z2
    z = w1*z2 + z1*w2 + x1*y2 - y1*x2
    return w, x, y, z


def qmult_many(qlist):
    """Multiplies multiple quaternions in one go.

    :qlist: List/tuple of quaternions, in the normal order in which you wanna multiply them
    :returns: Resultant quaternion

    """
    q = qlist[0]
    for i in range(len(qlist)-1):
        q = qmult(q, qlist[i+1])
    return q


def quat_around_axis(theta, axis):
    ''' Quaternion for rotation of angle `theta` around axis `axis`

    Parameters
    ----------
    theta : symbol
       angle of rotation
    axis : 3 element sequence
       vector (assumed normalized) specifying axis for rotation

    Returns
    -------
    quat : 4 element sequence of symbols
       quaternion giving specified rotation

    Notes
    -----
    Formula from http://mathworld.wolfram.com/EulerParameters.html
    '''
    # axis vector assumed normalized
    t2 = theta / 2.0
    st2 = sin(t2)
    return (cos(t2),
            st2 * axis[0],
            st2 * axis[1],
            st2 * axis[2])


#I'm not using this as I can't figure out how yaw-pitch-roll related to X-Y-Z axes
#TODO: Modify this function so that it uses X-Y-Z and such
def quat_from_eulers(eulers):
    """Creates a quaternion from a set of Euler angles.
    Eulers are an array of length 3 in the following order::
        [yaw, pitch, roll]
    """
    pitch, yaw, roll = eulers

    halfPitch = pitch * 0.5
    sP = sin(halfPitch)
    cP = cos(halfPitch)

    halfRoll = roll * 0.5
    sR = sin(halfRoll)
    cR = cos(halfRoll)

    halfYaw = yaw * 0.5
    sY = sin(halfYaw)
    cY = cos(halfYaw)

    return (-cY * sP * cR) - (sY * cP * sR),\
            (cY * sP * sR) - (sY * cP * cR),\
            (sY * sP * cR) - (cY * cP * sR),\
            (cY * cP * cR) + (sY * sP * sR)


def quat2axis(quat):
    ''' Angle-axis from Quaternion

    Parameters
    ----------
    theta : symbol
       angle of rotation
    axis : 3 element sequence
       vector (assumed normalized) specifying axis for rotation

    Returns
    -------
    quat : 4 element sequence of symbols
       quaternion giving specified rotation

    Notes
    -----
    Formula from http://mathworld.wolfram.com/EulerParameters.html
    '''
    qw, qx, qy, qz = quat
    angle = simplify(2 * acos(qw))
    x = simplify(qx / sqrt(1-qw*qw))
    y = simplify(qy / sqrt(1-qw*qw))
    z = simplify(qz / sqrt(1-qw*qw))
    return (angle, x, y, z)


def quat2mat(quat):
    ''' Symbolic conversion from quaternion to rotation matrix

    For a unit quaternion

    From: http://en.wikipedia.org/wiki/Rotation_matrix#Quaternion
    '''
    w, x, y, z = quat
    return Matrix([
            [1 - 2*y*y-2*z*z, 2*x*y - 2*z*w, 2*x*z+2*y*w],
            [2*x*y+2*z*w, 1-2*x*x-2*z*z, 2*y*z-2*x*w],
            [2*x*z-2*y*w, 2*y*z+2*x*w, 1-2*x*x-2*y*y]]).applyfunc(lambda i: trigsimp(i))
