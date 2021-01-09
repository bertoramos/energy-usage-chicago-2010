# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 12:26:35 2020

@author: Alberto
"""

from sklearn.manifold import TSNE

def tsne(data, emb_dim=2):
    """
    

    Parameters
    ----------
    data : pandas.DataFrame, numpy.array
        original data.
    emb_dim : int, optional
        number of features of data result. The default is 2.

    Returns
    -------
    numpy.array
        reduced data.

    """
    return TSNE(emb_dim).fit_transform(data)

