
def return_low_no_suit_score(model,X,threshold=0.81):
    '''
    FUNC:
            return a list of instances with associated probability scores, where the probability of no_suit is less than the given threshold
    NOTE:
            only works for ternary classification, can edit enumerate line for binary
    input:
            model = model fit prior to running this script
            X = values to predict
            threshold = optional, cutoff number between (0,1)
    output:
            list with index, predicted with associated probability score
    '''
    # build an empty list to add to, then return
    low_no_suit_score = []
    # grab probability scores
    preds_prob_scores = model.predict_proba(X)
    # enumerate probaility score list
    for idx, (prob_no_suit, prob_suit_no_indem, prob_suit_indem) in enumerate((preds_prob_scores)):
        if prob_no_suit <= threshold:
            low_no_suit_score.append([idx, round(prob_no_suit,4), round(prob_suit_no_indem,4), round(prob_suit_indem,4)])
    return low_no_suit_score
