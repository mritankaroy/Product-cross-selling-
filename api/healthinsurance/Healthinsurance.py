import pandas as pd
import numpy as np
import pickle as pkl

class HealthInsurance:
    def __init__(self):
        self.home_path = ''
        self.annual_premium_scaler =            pkl.load( open( self.home_path + 'features/annual_premium_scaler.pkl' ) )
        self.age_scaler =                       pkl.load( open( self.home_path + 'features/age_min_max_scaler.pkl' ) )
        self.vintage_scaler =                   pkl.load( open( self.home_path + 'features/vintagemin_min_max_scaler.pkl' ) )
        self.target_encode_gender_scaler =      pkl.load( open( self.home_path + 'features/target_encoding_gender.pkl' ) )
        self.target_encode_region_code_scaler = pkl.load( open( self.home_path + 'features/target_encoding_region_encoding.pkl' ) )
        self.fe_police_sales_channel =          pkl.load( open( self.home_path + 'features/fe_policy_sales_channel.pkl' ) )

    def feature_engeneering(self, df2):
        # feature insured
        df2['Insured'] = df2['Previously_Insured'].apply(lambda x: 'yes' if x == 1 else
        'no')

        # feature age_vehicle
        df2['Age_Vehicle'] = df2['Vehicle_Age'].apply(lambda x: 'old' if x == '> 2 Years' else
        'used car' if x == '1-2 Year' else
        'new')

        # feature interest
        df2['Interest'] = df2['Response'].apply(lambda x: 'yes' if x == 1 else
        'no')

        # feature age_group
        df2['Age_Group'] = df2['Age'].apply(lambda x: 'Above_35' if x > 35 else
        'Below_35')

        # feature insured
        df2['Insured'] = df2['Previously_Insured'].apply(lambda x: 'Yes' if x == 1 else
        'No')

        # feature how_much_time
        df2['How_Much_Time'] = df2['Vintage'].apply(lambda x: '<= 145 days' if x <= 145 else
        '> 145 days')

        # feature vehicle_damage
        df2['Vehicle_Damage'] = df2['Vehicle_Damage'].apply(lambda x: 1 if x == 'Yes' else 0)

        return df2

    def data_preparation(self, df4):

        df4['Annual_Premium'] = self.annual_premium_scaler.transform(df4[['Annual_Premium']].values)

        df4['Age'] = self.age_scaler.transform(df4[['Age']].values)

        df4['Vintage'] = self.vintage_scaler.transform(df4[['Vintage']].values)

        df4.loc[:, 'Gender'] = df4['Gender'].map(self.target_encode_gender_scaler)

        df4.loc[:, 'Region_Code'] = df4['Region_Code'].map(self.target_encode_region_code_scaler)

        df4 = pd.get_dummies(df4, prefix='Vehicle_Age', columns=['Vehicle_Age'])

        df4.loc[:, 'Policy_Sales_Channel'] = df4['Policy_Sales_Channel'].map(self.fe_police_sales_channel)

        cols_selected = ['Vintage', 'Annual_Premium', 'Age', 'Region_Code', 'Vehicle_Damage', 'Policy_Sales_Channel', 'Previously_Insured']

        return df4[cols_selected]

    def get_prediction( self, model, original_data, test_data ):
            pred = model.predict_proba(self, test_data)
            original_data['prediction'] = pred[:, 1].tolist()
            original_data.sort_values('prediction', ascending=False, inplace=True)

            return original_data(orient='records', date_format='iso')