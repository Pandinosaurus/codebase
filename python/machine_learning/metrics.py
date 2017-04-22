from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score, f1_score, log_loss, precision_score, recall_score


def classification_metrics_binary(y_true, y_pred):
    """
    Returns a report with different metrics for a binary classification problem.
    - Accuracy: Number of correct predictions made as a ratio of all predictions. Useful when there are equal number
    of observations in each class and all predictions and prediction errors are equally important.
    - Confusion matrix: C_ij where observations are known to be in group i but predicted to be in group j. In binary
    classification true negatives is C_00, false negatives is C_10, true positives is C_11 and false positives is C_01.
    - Precision: Number of true positives divided by the number of true and false positives. It is the ability of the
    classifier not to label as positive a sample that is negative.
    - Recall: Number of true positives divided by the number of true positives and false negatives. It is the ability
    of the classifier to find all the positive samples.
    - F1 Score: 2*((precision*recall)/(precision+recall)). It measures the balance between precision and recall.
    Parameters:
        y_true (list or array): True labels.
        y_pred (list or array): Predicted labels (binary).
    Returns:
        report (dict): Dictionary with metrics.
    Examples:
        >>> y_true = [0,1,0,0,1]
        >>> y_pred = [0,1,0,1,1]
        >>> classification_metrics_binary(y_true, y_pred)
        {'Recall': 1.0, 'F1': 0.80000000000000004, 'Confusion Matrix': array([[2, 1],
               [0, 2]]), 'Precision': 0.66666666666666663, 'Accuracy': 0.80000000000000004}

    """
    m_acc = accuracy_score(y_true, y_pred)
    m_f1 = f1_score(y_true, y_pred)
    m_precision = precision_score(y_true, y_pred)
    m_recall = recall_score(y_true, y_pred)
    m_conf = confusion_matrix(y_true, y_pred)
    report = {'Accuracy':m_acc, 'Precision':m_precision, 'Recall':m_recall, 'F1':m_f1, 'Confusion Matrix':m_conf}
    return report


def classification_metrics_binary_prob(y_true, y_prob):
    """
    Returns a report with different metrics for a binary classification problem.
    - AUC: The Area Under the Curve represents the ability to discriminate between positive and negative classes. An
    area of 1 represent perfect scoring and an area of 0.5 means random guessing.
    - Log loss: Also called logistic regression loss or cross-entropy loss. It quantifies the performance by
    penalising false classifications. Minimising the Log Loss is equivalent to maximising the accuracy but using
    probability predictions. Log loss penalize heavily classifiers that are confident about incorrect classifications.
    Parameters:
        y_true (list or array): True labels.
        y_prob (list or array): Predicted labels (probability).
    Returns:
        report (dict): Dictionary with metrics.
    Examples:
        >>> y_true = [0,1,0,0,1]
        >>> y_prob = [0.2,0.7,0.4,0.3,0.2]
        >>> classification_metrics_binary_prob(y_true, y_prob)
        {'AUC': 0.58333333333333326, 'Log loss': 0.61135139507835312}
        >>> y_prob = [0.2,0.7,0.4,0.3,0.3]
        >>> classification_metrics_binary_prob(y_true, y_prob)
        {'AUC': 0.75, 'Log loss': 0.53025837345672033}

    """
    m_auc = roc_auc_score(y_true, y_prob)
    m_logloss = log_loss(y_true, y_prob)
    report = {'AUC':m_auc, 'Log loss':m_logloss}
    return report

