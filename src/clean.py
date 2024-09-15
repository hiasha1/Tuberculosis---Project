import pandas as pd
import os
import logging

# Automated cleaning script
# This file reads in raw data filese, performs cleaning steps, and writes out
# clean data files that can be used for analysis.

#Cleaning steps:
# read data from a raw file
# rename the columns
# remove unneeded columns
# make a new file with cleaning data


def main():
    # read data from a raw file
    tb_csv = pd.read_csv("data/raw/Tb disease symptoms.csv")
    #print(tb_csv.head(10))
    

#rename the columns
    tb_csv.rename(columns = {'night sweats ':'night_sweats'
                         ,'fever for two weeks':'fever',
                         'back pain in certain parts ':'back_pain'
                         ,'weight loss ':'weight_loss',
                         'lumps that appear around the armpits and neck':
                         'lumps_around_armpits_and_neck',
                         'cough and phlegm continuously for two weeks to four weeks':
                         'cough_and_phlegm_2-4_weeks',
                         'coughing blood':'coughing_blood',
                         'sputum mixed with blood':'sputum_mixed_with_blood',
                         'chest pain':'chest_pain',
                         'shortness of breath':'shortness_of_breath',
                         'body feels tired':'body_feels_tired','swollen lymph nodes':
                         'swollen_lymph_nodes',
                         'loss of appetite':'loss_of_appetite'}, inplace=True
    )
    #print(tb_csv.columns)

# remove unneeded columns
    tb_csv=tb_csv[["id","gender","fever",
                 "coughing_blood","sputum_mixed_with_blood",
                 "night_sweats","chest_pain","back_pain",
                 "shortness_of_breath","weight_loss",
                 "lumps_around_armpits_and_neck",
                 "swollen_lymph_nodes","loss_of_appetite"]]
    #print(tb_csv.columns)

# make a new file with cleaning data
    tb_csv.to_csv("data/clean/tb_symptoms.csv",index=False)


if __name__ == "__main__":
    main()