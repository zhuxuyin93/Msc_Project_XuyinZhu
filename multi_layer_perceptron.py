from keras.models import Sequential
from keras.layers import Dense
import numpy
from sklearn import cross_validation
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve
from ggplot import *
import pandas as pd

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

    data = numpy.loadtxt("/Users/zxy/Desktop/project/model/train_multi_layer_perceptron_network.csv", delimiter=",")
    X = data[:, 0:18]
    Y = data[:, 19]
    train_x, test_x, train_y, test_y = cross_validation.train_test_split(X, Y, test_size=0.2, random_state=0)

    # create model
    model = Sequential()
    model.add(Dense(80, input_dim=18, init='uniform', activation='relu'))
    model.add(Dense(60, init='uniform', activation='relu'))
    model.add(Dense(1, init='uniform', activation='sigmoid'))

    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Fit the model
    class_weight = {0: 0.70, 1: 0.30}
    model.fit(train_x, train_y, nb_epoch=50, batch_size=10, class_weight=class_weight)

    # get prediction
    probability = model.predict_proba(test_x)

    # set thresold to get the predicted labels
    pred_label = get_predicted_labels(probability, 0.5)

    # result
    get_result(test_y, pred_label)

    # accuracy
    accuracy = accuracy_score(test_y, pred_label)
    print('\n')
    print ("accuracy: %f\n" % accuracy)

    # classification_report
    report = classification_report(test_y, pred_label, digits=5)
    print('classification report\n')
    print(report)

    # auc
    auc = roc_auc_score(test_y, probability)
    print("auc: %f" % auc)

    # output the probability and true label
    result_MLP = open("/Users/zxy/Desktop/project/model/result_MLP.txt", 'wb')

    for i in range(0,len(test_y)):
        line = str(test_y[i])+' '+str(probability[i])[2:-1]
        result_MLP.write(line+'\n')

    result_MLP.close()














