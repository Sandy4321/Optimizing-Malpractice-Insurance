
def return_predictions_and_probability_scores(model,X):
    '''
    FUNC:
            return predictions for each provider, with probability scores
    NOTE:
            only works for ternary classification, can edit enumerate line for binary
    input:
            model = model fit prior to running this script
            X = providers to predict
    output:
            list with index, predicted with associated probability score (rounded to four decimal places)
    '''
    # build an empty list to add to, then return
    to_return = []
    # grab probability scores
    preds_prob_scores = model.predict_proba(X)
    # enumerate probaility score list, rounding numbers
    for idx, (prob_no_suit, prob_suit_no_indem, prob_suit_indem) in enumerate((preds_prob_scores)):
        to_return.append([idx, round(prob_no_suit,4), round(prob_suit_no_indem,4), round(prob_suit_indem,4)])
    return to_return
