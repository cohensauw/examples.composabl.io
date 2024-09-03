# Copyright (C) Composabl, Inc - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential

from composabl_core import PerceptorImpl

#######
import os
import numpy as np

class ThermalRunawayPredict(PerceptorImpl):
    def __init__(self, *args, **kwargs):
        self.y = 0
        self.thermal_run = 0
        self.ML_list = []
        self.last_T = 0
        self.t_list = []

    async def compute(self, obs_spec, obs):
        # change obs to dictionary using sensors
        if type(obs) != dict:
            obs_keys = ['T', 'Tc', 'Ca', 'Cref', 'Tref','Conc_Error', 'Eps_Yield', 'Cb_Prod']
            obs = dict(zip(obs_keys, obs))

        self.t_list.append(float(obs['T']))
        self.last_T = float(obs['T'])

        t_mean = 0
        if len(self.t_list) > 10:
            t_mean = np.mean(self.t_list[-10:])
        else:
            t_mean = np.mean(self.t_list)


        return {"T_rolling_mean": t_mean}

    def filtered_sensor_space(self, obs):
        return ['T', 'Tc', 'Ca', 'Cref', 'Tref','Conc_Error', 'Eps_Yield', 'Cb_Prod']

