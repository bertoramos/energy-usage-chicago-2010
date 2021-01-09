# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 11:18:20 2020

@author: Alberto
"""

import abc

class Cluster(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def __init__(self, df):
        self.__df = df
    
    def __get_df(self):
        return self.__df
    
    def cluster(self, cluster_dims):
        """
        

        Parameters
        ----------
        cluster_dims : tuple
            range of K. cluster_dims[0] < cluster_dims[1]

        Raises
        ------
        NotImplementedError
            base class.

        Returns
        -------
        None.

        """
        raise NotImplementedError()
    
    df = property(fget=__get_df)
