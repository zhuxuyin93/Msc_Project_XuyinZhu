from sklearn.metrics import roc_curve
from ggplot import *
import pandas as pd
from sklearn.metrics import roc_auc_score
from ggplot import meat

def plot_roc_curve(test_y, probability, test_y_network, probability_network, title):

    auc = round(roc_auc_score(test_y, probability), 4)

    FPR1, TPR1, _ = roc_curve(test_y, probability)
    FPR2, TPR2, _ = roc_curve(test_y_network, probability_network)

    df1 = pd.DataFrame(dict(FPR=FPR1, TPR=TPR1))
    df2 = pd.DataFrame(dict(FPR=FPR2, TPR=TPR2))

    p = ggplot(aes(x='FPR', y='TPR'), data=df1) + \
        ggtitle("%s" %title) + \
        geom_line(color='blue') + \
        geom_line(aes(x='FPR', y='TPR'), data=df2,color = 'red') + \
        geom_abline(linetype='dashed')

    print p


if __name__ == '__main__':

    true_discriminant = []
    true_logistic = []
    true_mlp = []

    pred_discriminant = []
    pred_logistic = []
    pred_mlp = []

    true_discriminant_network = []
    true_logistic_network = []
    true_mlp_network = []

    pred_discriminant_network = []
    pred_logistic_network = []
    pred_mlp_network = []

    result_discriminant = open("/Users/zxy/Desktop/project/model/result_without_network/result_discriminant_analysis.txt")
    result_logistic = open("/Users/zxy/Desktop/project/model/result_without_network/result_logistic_regression.txt")
    result_mlp = open("/Users/zxy/Desktop/project/model/result_without_network/result_MLP.txt")

    result_discriminant_network = open("/Users/zxy/Desktop/project/model/result_with_network/result_discriminant_analysis.txt")
    result_logistic_network = open("/Users/zxy/Desktop/project/model/result_with_network/result_logistic_regression.txt")
    result_mlp_network = open("/Users/zxy/Desktop/project/model/result_with_network/result_MLP.txt")

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

    for line in result_discriminant_network:
        result = line.split(' ')
        true_discriminant_network.append(float(result[0]))
        pred_discriminant_network.append(float(result[1]))

    for line in result_logistic_network:
        result = line.split(' ')
        true_logistic_network.append(float(result[0]))
        pred_logistic_network.append(float(result[1]))

    for line in result_mlp_network:
        result = line.split(' ')
        true_mlp_network.append(float(result[0]))
        pred_mlp_network.append(float(result[1]))

    # roc curve for linear discriminant analysis
    plot_roc_curve(true_discriminant, pred_discriminant, true_discriminant_network, pred_discriminant_network, "Linear discriminant analysis")

    # roc curve for logistic regression
    plot_roc_curve(true_logistic, pred_logistic, true_logistic_network, pred_logistic_network, "Logistic regression")

    # roc curve for multi-layer perceptron
    plot_roc_curve(true_mlp, pred_mlp, true_mlp_network, pred_mlp_network, "Multi-layer perceptron")

    # plot three curves in one graph

    FPR1, TPR1, _ = roc_curve(true_discriminant_network, pred_discriminant_network)
    FPR2, TPR2, _ = roc_curve(true_logistic_network, pred_logistic_network)
    FPR3, TPR3, _ = roc_curve(true_mlp_network, pred_mlp_network)

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

