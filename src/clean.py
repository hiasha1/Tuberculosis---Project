import pandas as pd
import matplotlib.pyplot as plt

# This file reads in raw data filese, performs cleaning steps, and writes out
# clean data files that can be used for analysis.


# Cleaning steps:Tb disease symptoms.csv
# read data from a raw file
# rename the columns
# remove unneeded columns
# make a new file with cleaning data
def main():
        '''tb_sym = pd.read_csv("data/raw/Tb disease symptoms.csv")
        #tb_sym.info()
        print(tb_sym.head(10))

#rename the columns
 tb_sym.rename(columns = {'night sweats ':'night_sweats'
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
   # print(tb_sym.columns)

# remove unneeded columns
    tb_sym=tb_sym[["id","gender","fever",
                 "coughing_blood","sputum_mixed_with_blood",
                 "night_sweats","chest_pain","back_pain",
                 "shortness_of_breath","weight_loss",
                 "lumps_around_armpits_and_neck","body_feels_tired",
                 "swollen_lymph_nodes","loss_of_appetite"]]
    print(tb_sym.columns)

# remove the column with less common symptoms 
               
    #tb_sym = tb_sym.chest_pain.value_counts()
    #print(tb_sym)
    # 0 - 521   1 - 479

    #tb_sym =  tb_sym.body_feels_tired.value_counts()
    #print(tb_sym)

    #0  - 521    1 - 480


    tb_sym=tb_sym[["id","gender","fever",
                 "coughing_blood","sputum_mixed_with_blood",
                 "night_sweats","back_pain",
                 "shortness_of_breath","weight_loss",
                 "lumps_around_armpits_and_neck",
                 "swollen_lymph_nodes","loss_of_appetite"]]
    print(tb_sym.columns)


# make a new file with cleaning data
    tb_sym.to_csv("data/clean/tb_symptoms.csv",index=False)'''





# Cleaning steps:3- tuberculosis-case-detection-rate.csv

#read data from the file
#rename the columns name
#remove the rows with 0.0 case_detection_rate
#remove the rows with 3 or less case_detection_rate
#make a new file with cleaning data 

 # read data from a raw file
tb_csv = pd.read_csv("data/raw/3- tuberculosis-case-detection-rate.csv")
#print(tb_csv.head(10))

#rename the columns name
#tb_csv.columns
tb_csv.rename(columns={'Entity':'entity','Code':'code','Year':'year', 'Case detection rate (all forms)':'case_detection_rate'},inplace=True)
#print(tb_csv)


#remove the rows with 0.0 case_detection_rate
tb_csv.drop(tb_csv.loc[tb_csv['case_detection_rate'] == 0.0].index,inplace=True)
#print(tb_csv.shape)

#remove the rows with 3 detection rate
tb_csv.drop(tb_csv.loc[tb_csv['entity'] == 'Montserrat'].index,inplace=True)
#print(tb_csv.shape)

tb_csv.drop(tb_csv.loc[tb_csv['entity'] == 'Monaco'].index,inplace=True)
#print(tb_csv.shape)

tb_csv.drop(tb_csv.loc[tb_csv['entity'] == 'San Marino'].index,inplace=True)
#print(tb_csv.shape)

tb_csv.drop(tb_csv.loc[tb_csv['entity'] == 'Tokelau'].index,inplace=True)
#print(tb_csv.shape)

#remove the rows with less than 40 detection rate
tb_csv.drop(tb_csv.loc[tb_csv['case_detection_rate'] <= 40].index,inplace=True)
print(tb_csv.shape)

# make a new file with cleaning data
tb_csv.to_csv("data/clean/tb_case_detection_rate.csv",index=False)

# add a chart(Case Detection rate)
tbcsv1 = tb_csv.head(8)
tbcsv1.plot.bar(x='code', y='case_detection_rate', rot = 0)
plt.title('Case Detection')
plt.xlabel('code')
plt.ylabel('case_detection_rate')
plt.show()




# Cleaning steps:4- tuberculosis-treatment-success-rate-by-type.csv

#read data from a raw file
#rename the columns name
#remove unneeded columns
#delete rows with null values
#make a new file with cleaning data

#Read data from the file
tb_treat= pd.read_csv("data/raw/4- tuberculosis-treatment-success-rate-by-type.csv")
#print(tb_treat.head(10))

# Rename  Columns
#print(tb_treat.columns)
'''tb_treat.rename(columns={"Entity":"entity","Code":"code","Year":"year"
                         ,"Indicator:Treatment success rate: new TB cases":
                         "treat_success_rate:new_tb_cases",
                         "Indicator:Treatment success rate for patients treated for MDR-TB (%)":
                         "treat_success_rate_for_MDR-TB_cases",
                         "Indicator:Treatment success rate: XDR-TB cases":"treat_success_rate:XDR-TB"}
                        ,inplace = True)
#print(tb_treat.columns)
#tb_treat.shape

# Remove unneeded columns
tb_treat=tb_treat[["entity","code","year","treat_success_rate:new_tb_cases"]]
#print(tb_treat.columns)

tb_treat.drop(tb_treat.loc[tb_treat['treat_success_rate:new_tb_cases'] <= 40].index,inplace=True)
#print(tb_treat.shape)

#delete rows with null value
#tb_treat["treat_success_rate:new_tb_cases"].isnull().sum()
#tb_treat =tb_treat.dropna()

#make a new file with cleaning data
#tb_treat.to_csv("data/clean/treat.csv",index=False)

# add a chart(treatment success rate)
treat1 = tb_treat.head(10)
treat1.plot.bar(x='year', y='treat_success_rate:new_tb_cases', rot = 0)
plt.title('Success rate per year')
plt.xlabel('year')
plt.ylabel('success rate')
plt.show()'''

if __name__ == "__main__":
    main()

