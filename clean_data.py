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
    c_ctg = c_ctg.dropna()
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
    CTG_features = CTG_features.apply(pd.to_numeric, errors='coerce')
    c_cdf = CTG_features.to_dict()
    del c_cdf[extra_feature]

    for col in c_cdf:
        vals = np.fromiter(c_cdf[col].values(), dtype=float)
        not_nan_values = vals[~np.isnan(vals)]
        new_col_vals =[np.random.choice(not_nan_values) if np.isnan(k) else k for k in vals]
        c_cdf[col] = new_col_vals


  # -------------------------------------------------------------------------
    return pd.DataFrame(c_cdf)


def sum_stat(c_feat):
    """

    :param c_feat: Output of nan2num_cdf
    :return: Summary statistics as a dicionary of dictionaries (called d_summary) as explained in the notebook
    """
    # ------------------ IMPLEMENT YOUR CODE HERE:------------------------------
    d_summary = {}
    for col in c_feat:
        describe = c_feat[col].describe()
        d_summary[col] = {'min':describe['min'],'Q1':describe['25%'],'median':describe['50%'],'Q3':describe['75%'],'max':describe['max']}
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
    for col in d_summary:
        Q3 = d_summary[col]['Q3']
        Q1 = d_summary[col]['Q1']
        IQR = Q3 - Q1
        LEFT = Q1 - 1.5*IQR
        RIGHT = Q3 + 1.5*IQR
        arr = np.array(c_feat[col])
        c_no_outlier[col] = arr[(arr>LEFT) & (arr<RIGHT)]

    c_no_outlier = pd.DataFrame.from_dict(c_no_outlier, orient='index')
    c_no_outlier = c_no_outlier.transpose()

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
    filt_feature = c_cdf[feature] < thresh
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
    if mode == 'standard':
        nsd_res = (CTG_features - CTG_features.mean()) / CTG_features.std()
    elif mode == 'MinMax':
        nsd_res = (CTG_features - CTG_features.min()) / (CTG_features.max() - CTG_features.min())
    elif mode == 'mean':
        nsd_res = (CTG_features - CTG_features.mean()) / (CTG_features.max() - CTG_features.min())
    else:
        nsd_res = CTG_features
    if flag == True:
        if mode != "none":
            CTG_features.hist(column=[x,y], bins = 100 ,layout = (1,2),figsize=(20, 10),label = 'none ' + mode, color = '#0504aa')
            plt.xlabel('value')
            plt.ylabel('Count')
            plt.legend(loc = "upper right")

        plt.figure()
        nsd_res.hist(column=[x,y], bins=100, figsize=(20, 10),layout = (1,2), label = mode)
        plt.xlabel('value')
        plt.ylabel('Count')
        plt.legend(loc="upper right")
        plt.show()
    # -------------------------------------------------------------------------
    return pd.DataFrame(nsd_res)
