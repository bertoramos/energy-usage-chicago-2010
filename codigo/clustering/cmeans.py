# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 11:54:18 2020

@author: Alberto
"""

from .cluster import Cluster

from sklearn.cluster import KMeans
import skfuzzy as fuzz

import pandas as pd

class CMeansCluster(Cluster):
    
    def __init__(self, df):
        """
        Super class CMeans method

        Parameters
        ----------
        df : pandas.DataFrame / numpy.array
            data to be clustered.

        Returns
        -------
        None.

        """
        super().__init__(df)
        self.__results = []
        self.__clusters_dims = []
    
    def cluster(self, cluster_dims=[2]):
        """
        Applies cluster method

        Parameters
        ----------
        cluster_dims : list, optional
            k values to evaluate. The default is [2].

        Returns
        -------
        None.

        """
        assert all([k > 1 for k in cluster_dims]) and len(cluster_dims) > 0
        
        self.__clusters_dims = cluster_dims.copy()
        self.__clusters_dims.sort()
        
        m = 2
        error = 1e-3
        maxiter = 100
        
        for k in self.__clusters_dims:
            cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(self.df.T, k, m, error=error, maxiter=maxiter)
            self.__results.append([cntr, u, u0, d, jm, p, fpc])
    
    def get_scores(self):
        """
        Evaluates cluster results for each k value

        Returns
        -------
        pandas.DataFrame
            score for each k value.

        """
        scores = [[k, cm[-1]] for k, cm in zip(self.__clusters_dims, self.__results)]
        return pd.DataFrame(scores, columns=["cluster_dim", "score"])
    
    def get_cmeans_of(self, cluster_dim):
        """
        

        Parameters
        ----------
        cluster_dim : TYPE
            k value.

        Returns
        -------
        skfuzzy.cluster.CMeans
            cluster model which k=cluster_dim.

        """
        return self.__results[self.__clusters_dims.index(cluster_dim)]
