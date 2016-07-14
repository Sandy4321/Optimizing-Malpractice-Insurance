def return_low_no_suit_score(model,X):
    '''
    FUNC:
            return a list of scores where the probability of no_suit is less than 80%
            model must be fit prior to running this func
    input:
            X = values to predict
    output:
            list with index, predicted with associated probability score
    '''
    # build an empty list to add to, then return
    low_no_suit_score = []
    # grab probability scores
    preds_prob_scores = model.predict_proba(X)
    # enumerate probaility score list
    # threshold of 80% probability
    for idx, (prob_no_suit, prob_suit_no_indem, prob_suit_indem) in enumerate((preds_prob_scores)):
        if prob_no_suit <= 0.8:
            low_no_suit_score.append([idx, round(prob_no_suit,4), round(prob_suit_no_indem,4), round(prob_suit_indem,4)])
    return low_no_suit_score
