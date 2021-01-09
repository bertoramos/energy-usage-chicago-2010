# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 11:21:24 2020

@author: Alberto
"""

from .cluster import Cluster


from sklearn.cluster import KMeans

import pandas as pd
import numpy as np

from yellowbrick.cluster import KElbowVisualizer

class KMeansCluster(Cluster):
    
    def __init__(self, df):
        super().__init__(df)
        self.__results = []
    
    def cluster(self, cluster_dims=(2, 10)):
        """
        Applies cluster

        Parameters
        ----------
        cluster_dims : tuple, optional
            range of k values. The default is (2, 10).

        Returns
        -------
        KElbow visualization.

        """
        assert cluster_dims[0] < cluster_dims[1]
        
        model = KMeans()
        visualizer = KElbowVisualizer(model, k=cluster_dims)
        
        visualizer.fit(self.df)
        visualizer.show()
        
    def get_kmeans_of(self, cluster_dim):
        """

        Parameters
        ----------
        cluster_dim : int
            k value.

        Returns
        -------
        sklearn.cluster.KMeans
            Kmeans model which k=cluster_dim.

        """
        return KMeans(cluster_dim).fit(self.df)
