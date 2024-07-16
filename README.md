
# Data Baristas

Software written in Python to Extract, Transform, Load and Analyse data in AWS for a large café chain.








## Authors

- [@b-the-bee - Sam B](https://github.com/b-the-bee)
- [@mara557 - Marko G](https://github.com/mara557)
- [@keithu-data - Keith U](https://github.com/keithu-data)
- [@mvchikolo - Muhammad V](https://github.com/mvchikolo)


## Project Background

This app uses Python ran on an AWS Lambda to Extract data from an S3 Bucket, transform it within the lambda and load the data onto redshift using SQS with a different Lambda. The data is then analysed on an EC2 to provide insights as well as CloudWatch information using Grafana.

We started by building a local proof of concept, then integrating it into AWS.
## Client Requirements

The client requirements are as followed:

```
Based on the sales data from each branch that is provided in RAW CSV files, for each row in each CSV file you must.

Remove the Customer Name and the CARD Number - you should not store those anywhere. 

Keep a Cash/Card payment method 

Reorganise the transaction data so you split out the individual product from each order. 

e.g. "Regular Flavoured iced latte - Hazelnut - 2.75, Large Latte - 2.45" into separate data rows for reporting on, normalise this. 

This is because they want reports/graphs/visualisations later, on things like: 

  

How many coffees did we sell, of which type, each week? 

Which store had the highest sales each week, or day? 

What was the total value of Hazelnut Coffee sales each week, totalled for all stores? 

What was the total value of Large Latte sales each day, totalled for all stores? 

  

They also wish you to build visualisation of you Cloud Architecture performance and operations 
```
## Installation and Setup

**TBC**
## Running Unit Tests

Unit tests run by default through Github Actions, however if you wish to run them yourself, you can type this command in your terminal:

```sh
$ python -m pytest
```
## Project Reflections

How did your design go about meeting the project's requirements?
How did you guarantee the project's requirements?
If you had more time, what is one thing you would improve upon?
What did you most enjoy implementing?