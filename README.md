# Galvanize Final Project

I am working with an Austin-based medical malpractice insurance company to optimize their coverage decision-making. Before this project, the company's coverage decision was a judgement call; ideally, a predictive algorithm trained on their current providers would be an improvement to their practices.

This project is mainly a deep-dive into an existing company's data. It aims at using data science in a practical setting in order to change the way coverage decisions are made.

### Update: July 12, 2016

Heavy exploratory data analysis is the name of the game. Essentially, I've spend the past weekend and early part of the week getting my hands in the data. The data came in the form of several tables, pulled from a SQL database. This week's sprint aims to learn more about the data, request more data from the company, and potentially build a preliminary model.

Requesting more data is the next step; I am unsure of the signal contained in the initial batch of data. The additional data requested would be in PDF form, which would be particularly nasty to deal with. The PDFs would be the formal request for coverage from a doctor. Basically, the doctor answers questions about their speciality, practice, and suit history, among other information. I've succeeded in pulling out some derivative data from one of the tables, bypassing the need for the PDF data. However, this only dealt with two of the Yes/No questions on the PDFs. I'm really trying to get around manually entering the PDF data! There is some significant signal in the PDF data, hence the strong desire to aggregate and include it in the analysis.

I have had meetings with the lead underwriter and chief technology officer already. Also, I have emailed the CEO about additional data gathered from a third-party web scraping company. It's only Tuesday, by the way.

### Update: July 15, 2016

Today is Friday and the week has gone by very quickly. I've spent most of my time learning about the data in a Jupyter Notebook environment. The EDA notebook is the center of my work as I learn about predictive features. I've bypassed the need for the PDF scraping, luckily, but extracting features from a credits and debits spreadsheet; for example, if a doctor got a discount for being part of a certain committee this was documented in a new column with a '1', as opposed to a '0'. I created several binary features including membership to credible organizations, whether or not that doctor performs invasive procedures, and electronic versus paper records. Additionally, I ran a get_dummies on the 'State' column and feature engineered 'age' from the birthdate, which was more of a pain than you'd expect (anyone who has worked with datetime extensively should know the importance of this date: Jan 1, 1970).

I fit a very basic model (sklearn's RandomForestClassifier) to the dataframe, simply to validate the steps taken. The model did not perform well, as expected, due to a very small number of relevant features. It's important to note that the model has trouble discerning between docs that weren't sued, docs that were sued and won, and docs that were sued and lost. In other words, we need better data; the predictive capacity of the current data is very limited. I decided the best use of my time was to get started on coding up the rest of the pipeline. For instance, a function to take a model and a group of doctors and returning the malpractice prediction alongside probability scores for each of the three classes.

~~~~ python
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
~~~~

My request for more data is being granted. I am going to get my hands on tons of unstructured text data for each doctor, which means this prediction pipeline will soon be centered around NLP. I am already brainstorming on how to incorporate TF-IDF and fit_transform to the train text. THIS is the meat of the project...as far as I know, nothing like that is being done in malpractice insurance. I'm very excited to get going on the next phase of the project.

### Update: July 21, 2016

A little under a week has gone by and I've been very busy. This week has been a bit of a rollercoaster with getting permission, learning about the data, and beginning to model.

The data I got access to had roughly 900,000 doctors and was stored on a SQL server. I had to remote in and query to get a sense of the data. The relational database has 93 tables and plenty of noise and missing data. Though our deadline is approaching, I still am doing EDA due to the immense amount of data I was granted access to.

Just to prove I could link the two existing databases (the first data dump and this followup data), I spent yesterday afternoon querying the SQL server and aggregating some interesting features it contained, such as 'years of experience' and 'rating'.

~~~~ sql
SELECT Doctors.FirstName, Doctors.LastName, Doctors.YearsOfExperience, States.Name as 'State',
    DoctorLocations.Zip, UserRatings.Score
FROM Doctors
  INNER JOIN DoctorLocations
    ON Doctors.DoctorID = DoctorLocations.DoctorID
  INNER JOIN States
    ON DoctorLocations.StateID = States.StateID
  LEFT JOIN UserRatings
    ON UserRatings.DoctorID = Doctors.DoctorID
~~~~

I was able to link the two databases using Each doctor's first name, last name, and zipcode as a link. I then fit a similar random forest model. The text comments are not contained in the relational database (how we initially thought they were) so standby for those updates.

Interestingly enough, the malpractice insurance company I'm working with recently got access to the database of 900,000 docs too, so both their data team and myself have been learning about the data in unison. In other words, we're discovering features in the underlying data together.

##### Drew Rice, 2016.
