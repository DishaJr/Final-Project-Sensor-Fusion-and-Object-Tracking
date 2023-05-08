# ---------------------------------------------------------------------
# Project "Track 3D-Objects Over Time"
# Copyright (C) 2020, Dr. Antje Muntzinger / Dr. Andreas Haja.
#
# Purpose of this file : Kalman filter class
#
# You should have received a copy of the Udacity license together with this program.
#
# https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013
# ----------------------------------------------------------------------
#

# imports
import numpy as np

# add project directory to python path to enable relative imports
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import misc.params as params 

class Filter:
    '''Kalman filter class'''
    def __init__(self):
        pass

    def F(self):
        ############
        # TODO Step 1: implement and return system matrix F
        ############

        return np.array([[1., 0., 0., params.dt, 0., 0.],
                         [0., 1., 0., 0., params.dt, 0.],
                         [0., 0., 1., 0., 0., params.dt],
                         [0., 0., 0., 1., 0., 0.],
                         [0., 0., 0., 0., 1., 0.],
                         [0., 0., 0., 0., 0., 1.]])
        
        ############
        # END student code
        ############ 

    def Q(self):
        ############
        # TODO Step 1: implement and return process noise covariance Q
        ############

        FF = self.F()

        QQ = np.diag([0., 0., 0., params.q, params.q, params.q])

        integral_factor = np.array([
            [params.dt / 3, 0., 0., params.dt / 2, 0., 0.],
            [0., params.dt / 3., 0., 0., params.dt / 2, 0.],
            [0., 0., params.dt / 3, 0., 0., params.dt / 2],
            [params.dt / 2, 0., 0., params.dt, 0., 0.],
            [0., params.dt / 2, 0., 0., params.dt, 0.],
            [0., 0., params.dt / 2, 0., 0., params.dt]])
        QT = integral_factor * np.matmul(FF @ QQ, FF.T)
        return QT.T
        
        ############
        # END student code
        ############ 

    def predict(self, track):
        ############
        # TODO Step 1: predict state x and estimation error covariance P to next timestep, save x and P in track
        ############

        FF = self.F()
        QQ = self.Q()
        
        xx = FF @ track.x
        
        PP = np.matmul(FF @ track.P, FF.T) + QQ
        
        track.set_x(xx)
        track.set_P(PP)
        
        ############
        # END student code
        ############ 

    def update(self, track, meas):
        ############
        # TODO Step 1: update state x and covariance P with associated measurement, save x and P in track
        ############
        
        Gamma = self.gamma(track, meas)
        
        HH = meas.sensor.get_H(track.x)
        SS = self.S(track, meas, HH)
        
        KK = np.matmul(track.P @ HH.T, np.linalg.inv(SS))
        
        xx = track.x + KK @ Gamma
        
        track.set_x(xx)
        
        II = np.identity(n=params.dim_state)
        PP = (II - np.matmul(KK, HH)) @ track.P

        track.set_P(PP)

        track.update_attributes(meas)
        
        ############
        # END student code
        ############ 
        track.update_attributes(meas)
    
    def gamma(self, track, meas):
        ############
        # TODO Step 1: calculate and return residual gamma
        ############

        return meas.z - meas.sensor.get_hx(track.x)
        
        ############
        # END student code
        ############ 

    def S(self, track, meas, H):
        ############
        # TODO Step 1: calculate and return covariance of residual S
        ############

        return np.matmul(H @ track.P, H.T) + meas.R
        
        ############
        # END student code
        ############ 