# Optimizing Malpractice Insurance

This project provides a new way to understand risk in medical malpractice insurance, using data science as a means to change the way coverage decisions are made. I worked with an Austin-based malpractice insurance company to develop the prediction pipeline.

**The input**: a doctor to be evaluated. **The output**: the doctor's probability scores for each classification.

The classes we sought to evaluate for each doctor were **no suit**, **sued and won**, and **sued and lost**.  

![Dashboard Example](https://github.com/drewrice2/Optimizing-Malpractice-Insurance/blob/master/images/Three_classes.png)

The company would cover doctors in each of the three buckets differently, hence the decision to use ternary classification. Domain knowledge helped to identify features to differentiate the classes.

Technologies used:

    SKlearn's Random Forest classifier, GridSearch
    Pandas
    Numpy
    SQL
    

##### Drew Rice, 2016.
