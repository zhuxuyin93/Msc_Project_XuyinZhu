import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesClassifier

def selector_SelectKBest(features, label):
    selector = SelectKBest(chi2, k=15)
    selector.fit(features, label)
    print sorted(zip(map(lambda x: round(x, 4), selector.get_support()), names),reverse=True)

def selector_PCA(features):
    selector = PCA(n_components=15)
    selector.fit(features)
    print sorted(zip(map(lambda x: round(x, 4), selector.explained_variance_ratio_), names), reverse=True)

def selector_RFE(features, label):
    model = LogisticRegression()
    selector = RFE(model, 15)
    selector.fit(features, label)
    print sorted(zip(map(lambda x: round(x, 4), selector.get_support()), names), reverse=True)


def selector_ExtraTreesClassifier(features, label):
    selector = ExtraTreesClassifier()
    selector.fit(features,label)
    print sorted(zip(map(lambda x: round(x, 4), selector.feature_importances_), names), reverse=True)

def selector_RandomForest(features, label):
    selector = RandomForestRegressor()
    selector.fit(features, label)
    print sorted(zip(map(lambda x: round(x, 4), selector.feature_importances_), names),reverse=True)

if __name__ == '__main__':

    data = pd.read_csv("/Users/zxy/Desktop/project/model/train.csv")

    features = pd.DataFrame(data, columns=[ 'Term', 'BorrowerAPR', 'BorrowerRate', 'LenderYield', 'EstimatedEffectiveYield',
                'EstimatedLoss', 'EstimatedReturn', 'ProsperRating (numeric)', 'ProsperScore', 'ListingCategory (numeric)',
                'BorrowerState', 'Occupation', 'EmploymentStatus', 'EmploymentStatusDuration', 'IsBorrowerHomeowner',
                'CurrentlyInGroup', 'CreditScoreRangeLower', 'CreditScoreRangeUpper', 'CurrentCreditLines', 'OpenCreditLines',
                'TotalCreditLinespast7years', 'OpenRevolvingAccounts', 'OpenRevolvingMonthlyPayment', 'InquiriesLast6Months',
                'TotalInquiries', 'CurrentDelinquencies', 'AmountDelinquent', 'DelinquenciesLast7Years', 'RevolvingCreditBalance',
                'BankcardUtilization', 'AvailableBankcardCredit', 'TotalTrades', 'TradesNeverDelinquent (percentage)',
                'TradesOpenedLast6Months', 'DebtToIncomeRatio', 'IncomeRange', 'IncomeVerifiable', 'StatedMonthlyIncome',
                'TotalProsperLoans', 'TotalProsperPaymentsBilled', 'OnTimeProsperPayments', 'ProsperPaymentsLessThanOneMonthLate',
                'ProsperPaymentsOneMonthPlusLate', 'ProsperPrincipalBorrowed', 'ProsperPrincipalOutstanding', 'ScorexChangeAtTimeOfListing',
                'LoanOriginalAmount', 'Recommendations'
                                    ])
    label = pd.DataFrame(data, columns = ['LoanStatus']).values.ravel()
    names = features.columns

    # selecting the best features based on univariate statistical tests
    selector_SelectKBest(features, label)

    # Principal component analysis
    selector_PCA(features)

    # feature ranking with recursive feature elimination
    selector_RFE(features, label)

    # use extra trees to estimate the importance of features
    selector_ExtraTreesClassifier(features, label)

    # random forest
    selector_RandomForest(features, label)


    # selecting the best features based on univariate statistical tests
    # 'ProsperScore', 'ProsperRating (numeric)', 'ProsperPrincipalBorrowed', 'LenderYield', 'IsBorrowerHomeowner',
    # 'InquiriesLast6Months', 'EstimatedLoss', 'EstimatedEffectiveYield', 'CurrentlyInGroup', 'CurrentDelinquencies',
    # 'CreditScoreRangeUpper', 'CreditScoreRangeLower', 'BorrowerRate', 'BorrowerAPR', 'AvailableBankcardCredit',

    # Principal component analysis
    # 'Term', 'BorrowerAPR', 'BorrowerRate', 'LenderYield', 'EstimatedEffectiveYield',
    # 'EstimatedLoss', 'EstimatedReturn', 'ProsperRating (numeric)', 'ProsperScore', 'ListingCategory (numeric)',
    # 'BorrowerState', 'Occupation', 'EmploymentStatus', 'EmploymentStatusDuration', 'IsBorrowerHomeowner',

    # feature ranking with recursive feature elimination
    # 'TradesOpenedLast6Months', 'TotalProsperLoans', 'Term', 'StatedMonthlyIncome', 'Recommendations',
    # 'ProsperScore', 'ProsperRating (numeric)', 'ProsperPrincipalOutstanding', 'ProsperPaymentsLessThanOneMonthLate', 'LenderYield',
    # 'EstimatedEffectiveYield', 'DebtToIncomeRatio', 'CurrentDelinquencies', 'CreditScoreRangeUpper', 'BankcardUtilization',

    # use extra trees to estimate the importance of features
    # 'LenderYield', 'BankcardUtilization', 'EmploymentStatusDuration', 'BorrowerState', 'AvailableBankcardCredit',
    # 'Occupation', 'BorrowerAPR', 'TotalTrades', 'OpenRevolvingMonthlyPayment', 'EstimatedEffectiveYield',
    # 'DebtToIncomeRatio', 'TotalInquiries', 'EstimatedLoss', 'BorrowerRate', 'LoanOriginalAmount',

    # random forest
    # 'EmploymentStatusDuration', 'StatedMonthlyIncome', 'BorrowerRate', 'BankcardUtilization', 'AvailableBankcardCredit',
    # 'EstimatedEffectiveYield', 'BorrowerState', 'OpenRevolvingMonthlyPayment', 'DebtToIncomeRatio', 'LoanOriginalAmount',
    # 'Occupation', 'TotalTrades', 'RevolvingCreditBalance', 'TotalCreditLinespast7years', 'TotalInquiries',
