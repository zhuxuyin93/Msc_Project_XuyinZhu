import pandas as pd
from sklearn import cross_validation
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from sklearn import discriminant_analysis
from sklearn.metrics import roc_curve
from ggplot import *

def get_result(test_y, pred_label):

    tp = 0
    tn = 0
    fp = 0
    fn = 0

    for i in range(0,len(test_y)):
        if test_y[i] == 1 and pred_label[i] == 1:
            tp = tp + 1
        elif test_y[i] ==1 and pred_label[i] == 0:
            fn = fn + 1
        elif test_y[i] ==0 and pred_label[i] == 0:
            tn = tn + 1
        elif test_y[i] ==0 and pred_label[i] == 1:
            fp = fp + 1

    print ("tp:%d tn:%d fp:%d fn:%d" %(tp,tn,fp,fn))

def get_predicted_labels(probability, thresold):
    pred_label = []
    for i in probability:
        if i > thresold:
            pred_label.append(1)
        else:
            pred_label.append(0)
    return pred_label

if __name__ == '__main__':

    data = pd.read_csv("/Users/zxy/Desktop/project/model/train.csv")

    train = pd.DataFrame(data, columns=[

        'TradesOpenedLast6Months', 'TotalProsperLoans', 'Term', 'StatedMonthlyIncome', 'Recommendations',
        'ProsperScore', 'ProsperRating (numeric)', 'ProsperPrincipalOutstanding', 'ProsperPaymentsLessThanOneMonthLate', 'LenderYield',
        'EstimatedEffectiveYield', 'DebtToIncomeRatio', 'CurrentDelinquencies', 'CreditScoreRangeUpper', 'BankcardUtilization',

        # 'In_Degree', 'Out_Degree', 'Betweenness_Centrality', 'Closeness_Centrality'
    ])

    label = pd.DataFrame(data, columns=['LoanStatus']).values.ravel()

    # split train and test data
    train_x, test_x, train_y, test_y = cross_validation.train_test_split(train, label, test_size=0.20, random_state=0)

    # create logistic model
    model = discriminant_analysis.LinearDiscriminantAnalysis()
    model.fit(train_x, train_y)

    # get predictions
    probability = model.predict_proba(test_x)[:,1]

    # set thresold to get the predicted labels
    pred_label = get_predicted_labels(probability, 0.5)

    # result
    get_result(test_y, pred_label)

    # accuracy
    accuracy = accuracy_score(test_y, pred_label)
    print ("accuracy: %f\n" %accuracy)

    # classification_report
    report = classification_report(test_y, pred_label, target_names='LoanStatus', digits=5)
    print('classification report\n')
    print(report)

    # auc
    auc = roc_auc_score(test_y, probability)
    print("auc: %f" %auc)

    # output the probability and true label
    result_discriminant_analysis = open("/Users/zxy/Desktop/project/model/result_discriminant_analysis.txt", 'wb')

    for i in range(0, len(test_y)):
        line = str(test_y[i]) + ' ' + str(probability[i])
        result_discriminant_analysis.write(line + '\n')

    result_discriminant_analysis.close()










