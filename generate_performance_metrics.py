from sklearn.metrics import classification_report


# Create arrays storing the counts for every class
def process_conf_matrix(conf_matrix):

    n_classes = len(conf_matrix)
    y_true = []
    y_pred = []

    for i in range(n_classes):
        for j in range(n_classes):
            actual = i
            predicted = j
            n_counts = conf_matrix[i][j]

            for k in range(n_counts):
                y_true.append(actual)
                y_pred.append(predicted)

    return y_true, y_pred


# Hand-labelled confusion matrix
hand_conf_matrix = \
    [[47, 1, 2, 4, 1, 5],
[8, 39, 2, 6, 2, 3],
[5, 0, 51, 0, 0, 4],
[3, 2, 0, 52, 0, 3],
[4, 0, 0, 0, 39, 5],
[1, 0, 1, 2, 0, 236]]


y_true, y_pred = process_conf_matrix(hand_conf_matrix)

print("Hand-labelled classificaton matrix")
print(classification_report(y_true = y_true, y_pred = y_pred))
print("")
print("")


# Snorkel-labelled confusion matrix
snorkel_conf_matrix = \
    [[35, 3, 2, 5, 5, 10],
[8, 33, 1, 9, 2, 7],
[2, 1, 53, 0, 1, 3],
[1, 3, 0, 47, 0, 9],
[1, 0, 1, 4, 38, 4],
[1, 5, 2, 5, 1, 226]]

y_true, y_pred = process_conf_matrix(snorkel_conf_matrix)

print("Snorkel-annotated classification matrix")
print(classification_report(y_true = y_true, y_pred = y_pred))