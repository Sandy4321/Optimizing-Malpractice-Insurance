# Galvanize Final Project

I am working with an Austin-based medical malpractice insurance company to optimize their coverage decision-making. Before this project, the company's coverage decision was a judgement call; ideally, a predictive algorithm trained on their current providers would be an improvement to their practices.

This project is mainly a deep-dive into an existing company's data. It aims at using data science in a practical setting in order to change the way coverage decisions are made.

### Update: July 12, 2016

Heavy exploratory data analysis is the name of the game. Essentially, I've spend the past weekend and early part of the week getting my hands in the data. The data came in the form of several tables, pulled from a SQL database. This week's sprint aims to learn more about the data, request more data from the company, and potentially build a preliminary model.

Requesting more data is the next step; I am unsure of the signal contained in the initial batch of data. The additional data requested would be in PDF form, which would be particularly nasty to deal with. The PDFs would be the formal request for coverage from a doctor. Basically, the doctor answers questions about their speciality, practice, and suit history, among other information. I've succeeded in pulling out some derivative data from one of the tables, bypassing the need for the PDF data. However, this only dealt with two of the Yes/No questions on the PDFs. I'm really trying to get around manually entering the PDF data! There is some significant signal in the PDF data, hence the strong desire to aggregate and include it in the analysis.

I have had meetings with the lead underwriter and chief technology officer already. Also, I have emailed the CEO about additional data gathered from a third-party web scraping company. It's only Tuesday, by the way.

##### Drew Rice, 2016.
