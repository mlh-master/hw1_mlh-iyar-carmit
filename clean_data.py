# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:14:23 2019

@author: smorandv
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def rm_ext_and_nan(CTG_features, extra_feature):
    """

    :param CTG_features: Pandas series of CTG features
    :param extra_feature: A feature to be removed
    :return: A dictionary of clean CTG called c_ctg
    """
    # ------------------ IMPLEMENT YOUR CODE HERE:------------------------------
    c_ctg = CTG_features.copy()
    del c_ctg[extra_feature]
    c_ctg = c_ctg.apply(pd.to_numeric, errors='coerce')
    c_ctg = c_ctg.fillna(1000)
    #df_na = c_ctg.dropna()
    # --------------------------------------------------------------------------
    return c_ctg


def nan2num_samp(CTG_features, extra_feature):
    """

    :param CTG_features: Pandas series of CTG features
    :param extra_feature: A feature to be removed
    :return: A pandas dataframe of the dictionary c_cdf containing the "clean" features
    """
    c_cdf = {}
    # ------------------ IMPLEMENT YOUR CODE HERE:------------------------------
    c_cdf_1 = CTG_features.to_dict()
    del c_cdf_1[extra_feature]
    c_cdf_1 = c_cdf_1.apply(pd.to_numeric, errors='coerce')


   for col in c_cdf_1:
        not_nan_values = c_cdf_1[~np.isnan(c_cdf_1[col])]
        rows = len(np.isnan(c_cdf_1[col]))
        c_cdf_1[col] =  {k: np.random.choice(not_nan_values,1) for k in c_cdf_1[col] if np.isnan(c_cdf_1[col])}
    # random_val = pd.CTG_features(val, columns=c_cdf_1.columns, index=c_cdf_1.index)
    c_cdf = c_cdf.update(c_cdf_1)

    #############################
    #c_cdf = CTG_features.copy()
    #del c_cdf[extra_feature]
    #c_cdf = pd.to_numeric(c_cdf, errors='coerce')
    #for i in range(len(c_cdf)):
     #   c_cdf.loc[:][i] = c_cdf.loc[:][i].fillna(np.random.choice(c_cdf.loc[:][i]))
    # -------------------------------------------------------------------------
    return pd.DataFrame(c_cdf)


def sum_stat(c_feat):
    """

    :param c_feat: Output of nan2num_cdf
    :return: Summary statistics as a dicionary of dictionaries (called d_summary) as explained in the notebook
    """
    # ------------------ IMPLEMENT YOUR CODE HERE:------------------------------

    # -------------------------------------------------------------------------
    return d_summary


def rm_outlier(c_feat, d_summary):
    """

    :param c_feat: Output of nan2num_cdf
    :param d_summary: Output of sum_stat
    :return: Dataframe of the dictionary c_no_outlier containing the feature with the outliers removed
    """
    c_no_outlier = {}
    # ------------------ IMPLEMENT YOUR CODE HERE:------------------------------

    # -------------------------------------------------------------------------
    return pd.DataFrame(c_no_outlier)


def phys_prior(c_cdf, feature, thresh):
    """

    :param c_cdf: Output of nan2num_cdf
    :param feature: A string of your selected feature
    :param thresh: A numeric value of threshold
    :return: An array of the "filtered" feature called filt_feature
    """
    # ------------------ IMPLEMENT YOUR CODE HERE:-----------------------------

    # -------------------------------------------------------------------------
    return filt_feature


def norm_standard(CTG_features, selected_feat=('LB', 'ASTV'), mode='none', flag=False):
    """

    :param CTG_features: Pandas series of CTG features
    :param selected_feat: A two elements tuple of strings of the features for comparison
    :param mode: A string determining the mode according to the notebook
    :param flag: A boolean determining whether or not plot a histogram
    :return: Dataframe of the normalized/standardazied features called nsd_res
    """
    x, y = selected_feat
    # ------------------ IMPLEMENT YOUR CODE HERE:------------------------------

    # -------------------------------------------------------------------------
    return pd.DataFrame(nsd_res)
