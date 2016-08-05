# Optimizing Malpractice Insurance

### The goal
This project provides a new way to understand risk in medical malpractice insurance, using data science as a means to change the way coverage decisions are made. I worked with an Austin-based malpractice insurance company to develop the prediction pipeline.

### The data
Data came from multiple sources in multiple forms. I worked with the company's master relational database in addition to data found in the internal file structure. Challenges included duplicates, missing data, inconsistencies, and more. Also, we gained access to a third-party, scraped relational database of around 900,000 doctors. Challenges here included exploring the 93 tables, SQL queries, and feature extraction.

### The approach
The model used was **SKLearn's RandomForestClassifier**. The classes we sought to evaluate for each doctor were no suit, sued and won, and sued and lost. The decision to use ternary classification was a business decision made by the company; essentially, they would cover doctors differently depending on the classification. Domain knowledge helped to identify features to differentiate the classes.

The input: a doctor to be evaluated. The output: the doctor's probability scores for each classification.

### Deliverables:
- Identified signal, linked data from different sources
- Improved the ability to predict risk
- Established data-quality improvement plan

### Technologies used:
- SKlearn's Random Forest classifier, GridSearch
- Pandas
- Numpy
- SQL

##### Drew Rice, 2016.
