from sklearn.metrics import roc_curve
from ggplot import *
import pandas as pd
from sklearn.metrics import roc_auc_score
from ggplot import meat

def plot_roc_curve(test_y, probability, title):
    auc = round(roc_auc_score(test_y, probability), 4)

    FPR, TPR, _ = roc_curve(test_y, probability)

    df = pd.DataFrame(dict(FPR=FPR, TPR=TPR))
    p = ggplot(df, aes(x='FPR', y='TPR')) + \
        ggtitle("%s (AUC = %s)" % (title,str(auc))) + \
        geom_line() + \
        geom_abline(linetype='dashed')

    print p


if __name__ == '__main__':

    true_discriminant = []
    true_logistic = []
    true_mlp = []

    pred_discriminant = []
    pred_logistic = []
    pred_mlp = []

    result_discriminant = open("/Users/zxy/Desktop/project/model/result_without_network/result_discriminant_analysis.txt")
    result_logistic = open("/Users/zxy/Desktop/project/model/result_without_network/result_logistic_regression.txt")
    result_mlp = open("/Users/zxy/Desktop/project/model/result_without_network/result_MLP.txt")

    for line in result_discriminant:
        result = line.split(' ')
        true_discriminant.append(float(result[0]))
        pred_discriminant.append(float(result[1]))

    for line in result_logistic:
        result = line.split(' ')
        true_logistic.append(float(result[0]))
        pred_logistic.append(float(result[1]))

    for line in result_mlp:
        result = line.split(' ')
        true_mlp.append(float(result[0]))
        pred_mlp.append(float(result[1]))

    # roc curve for linear discriminant analysis
    plot_roc_curve(true_discriminant, pred_discriminant, "Linear discriminant analysis")

    # roc curve for logistic regression
    plot_roc_curve(true_logistic, pred_logistic, "Logistic regression")

    # roc curve for multi-layer perceptron
    plot_roc_curve(true_mlp, pred_mlp, "Multi-layer perceptron")

    # plot three curves in one graph

    FPR1, TPR1, _ = roc_curve(true_discriminant, pred_discriminant)
    FPR2, TPR2, _ = roc_curve(true_logistic, pred_logistic)
    FPR3, TPR3, _ = roc_curve(true_mlp, pred_mlp)

    df1 = pd.DataFrame(dict(FPR=FPR1, TPR=TPR1))
    df2 = pd.DataFrame(dict(FPR=FPR2, TPR=TPR2))
    df3 = pd.DataFrame(dict(FPR=FPR3, TPR=TPR3))

    p = ggplot(aes(x='FPR', y='TPR'), data=df1) + \
        ggtitle("Three ROC curves") + \
        geom_line(color='red') + \
        geom_line(aes(x='FPR', y='TPR'), data=df2,color = 'blue') + \
        geom_line(aes(x='FPR', y='TPR'), data=df3, color='green') + \
        geom_abline(linetype='dashed')

    print p

