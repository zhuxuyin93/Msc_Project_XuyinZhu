from sklearn import preprocessing
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def categorical_features(data):
    number = preprocessing.LabelEncoder()
    data['Occupation'] = number.fit_transform(data['Occupation'].astype(str))
    data['IsBorrowerHomeowner'] = number.fit_transform(data['IsBorrowerHomeowner'].astype(str))
    data['CurrentlyInGroup'] = number.fit_transform(data['CurrentlyInGroup'].astype(str))
    data['IncomeRange'] = number.fit_transform(data['IncomeRange'].astype(str))
    data['IncomeVerifiable'] = number.fit_transform(data['IncomeVerifiable'].astype(str))
    data['EmploymentStatus'] = number.fit_transform(data['EmploymentStatus'].astype(str))
    data['BorrowerState'] = number.fit_transform(data['BorrowerState'].astype(str))

    return data

def missing_values(data):
    imp = preprocessing.Imputer(missing_values='NaN', strategy='mean', axis=0)
    data[['DebtToIncomeRatio']] = imp.fit_transform(data[['DebtToIncomeRatio']])
    data[['EmploymentStatusDuration']] = imp.fit_transform(data[['EmploymentStatusDuration']])

    return data

def scaling_data(data, features):
    min_max = MinMaxScaler(feature_range=(0, 1))
    data[features] = min_max.fit_transform(data[features])

    return data

if __name__ == '__main__':

    data = pd.DataFrame.from_csv("/Users/zxy/Desktop/project/model/listingWithNetwork.csv")

    features = ['Term', 'BorrowerAPR', 'BorrowerRate', 'LenderYield', 'EstimatedEffectiveYield',
                'EstimatedLoss', 'EstimatedReturn', 'ProsperRating (numeric)', 'ProsperScore', 'ListingCategory (numeric)',
                'BorrowerState', 'Occupation', 'EmploymentStatus', 'EmploymentStatusDuration', 'IsBorrowerHomeowner',
                'CurrentlyInGroup', 'CreditScoreRangeLower', 'CreditScoreRangeUpper', 'CurrentCreditLines', 'OpenCreditLines',
                'TotalCreditLinespast7years', 'OpenRevolvingAccounts', 'OpenRevolvingMonthlyPayment', 'InquiriesLast6Months',
                'TotalInquiries', 'CurrentDelinquencies', 'AmountDelinquent', 'DelinquenciesLast7Years', 'RevolvingCreditBalance',
                'BankcardUtilization', 'AvailableBankcardCredit', 'TotalTrades', 'TradesNeverDelinquent (percentage)',
                'TradesOpenedLast6Months', 'DebtToIncomeRatio', 'IncomeRange', 'IncomeVerifiable', 'StatedMonthlyIncome',
                'TotalProsperLoans', 'TotalProsperPaymentsBilled', 'OnTimeProsperPayments', 'ProsperPaymentsLessThanOneMonthLate',
                'ProsperPaymentsOneMonthPlusLate', 'ProsperPrincipalBorrowed', 'ProsperPrincipalOutstanding', 'ScorexChangeAtTimeOfListing',
                'LoanOriginalAmount', 'Recommendations',
                'Degree', 'In_Degree', 'Out_Degree', 'Degree_Centrality', 'Betweenness_Centrality', 'Closeness_Centrality'
                ]



    # Convert categorical features to numerical form
    data = categorical_features(data)

    # Impute missing values
    data = missing_values(data)

    # scaling data to (0,1)
    data = scaling_data(data, features)

    # write the output
    data.to_csv("/Users/zxy/Desktop/project/model/train.csv")










