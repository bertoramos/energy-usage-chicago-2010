# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 19:54:36 2020

@author: Alberto
"""

import pandas as pd

import datetime


class DataLoader:
    
    __kwh_cols = [f"KWH {datetime.date(2008, i, 1).strftime('%B').upper()} 2010" for i in range(1, 13)]
    __therm_cols = [f"THERM {datetime.date(2008, i, 1).strftime('%B').upper()} 2010" for i in range(1, 13)]
    
    def __init__(self, df):
        """
        

        Parameters
        ----------
        df : pandas.DataFrame
            Constructor.

        Returns
        -------
        None.

        """
        self.__df = df
    
    def __get_df(self):
        """
        df property getter

        Returns
        -------
        pandas.DataFrame
            Original dataframe.

        """
        return self.__df
    
    def __energy_cols(self):
        """
        

        Returns
        -------
        list
            columns names list.

        """
        return DataLoader.__kwh_cols
    
    def __gas_cols(self):
        """
        

        Returns
        -------
        list
            columns names list.

        """
        return DataLoader.__therm_cols
    
    def get_full_cols(self, cols):
        """
        

        Parameters
        ----------
        cols : list
            columns names list.

        Returns
        -------
        pandas.DataFrame
            dataframe with all rows and columns in cols.

        """
        return self.__df[cols]
    
    def get_cols(self, cols):
        """
        

        Parameters
        ----------
        cols : list
            columns names list.

        Returns
        -------
        pandas.DataFrame
            dataframe with no-null rows and columns in cols.

        """
        res = self.get_full_cols(cols)
        return res.dropna()
    
    def get_rows(self, rows):
        """
        

        Parameters
        ----------
        rows : pandas.Index
            indeces to select.

        Returns
        -------
        pandas.DataFrame
            dataframe with all columns.

        """
        return self.__df.iloc[rows]
    
    def __getitem__(self, cols):
        """
        allows DataLoader to be subscribed

        Parameters
        ----------
        cols : list
            columns names list.

        Returns
        -------
        pandas.DataFrame
            dataframe with all columns.

        """
        return self.get_cols(cols)
    
    df = property(fget=__get_df)
    
    """"
    energy columns names
    """
    energy_cols = property(fget=__energy_cols)
    
    """
    gas columns names
    """
    gas_cols = property(fget=__gas_cols)

