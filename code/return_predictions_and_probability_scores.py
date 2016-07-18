
def return_probability_scores(model,X):
    '''
    FUNC:
            return probability scores for each provider after running X through a model
    NOTE:
            only works for ternary classification, can edit enumerate line for binary
    input:
            model = model fit prior to running this script
            X = providers to predict
    output:
            list with index, predicted with associated probability score (rounded to four decimal places)
    '''
    # initialize list
    to_return = []
    # grab probability scores
    preds_prob_scores = model.predict_proba(X)
    # enumerate probaility score list, rounding numbers
    for idx, (prob_no_suit, prob_suit_no_indem, prob_suit_indem) in enumerate((preds_prob_scores)):
        to_return.append([idx, round(prob_no_suit,4), round(prob_suit_no_indem,4), round(prob_suit_indem,4)])
    return to_return
