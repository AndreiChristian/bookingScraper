### Steps to follow 1 of 2 :

- Download the csv dataset from here: https://teachyou.eu/wp-content/uploads/2020/02/data_linear_regression.zip
- unzip the data and put it in a folder of your choice (Desktop for instance).
- Start a new project in Jupyter notebook with the same environment you have created this morning.
- Import SparkSession, create a new Spark app instance and import your new dataset (data_linear_regression.csv) with the spark.read.csv
  function (look at the notebook of this morning to see again how it is done)
  from pyspark.sql import SparkSession
  spark = SparkSession.builder.appName(‘lr_project').getOrCreate()
  data = spark.read.csv("Ecommerce_Customers.csv",inferSchema=True,header=True)
- Instead of importing the logistic regression , import the linear regression library
  from pyspark.ml.regression import LinearRegression
- with “data.printSchema()” , look at which columns will be your features columns and which column will be your label column.
- import the vector assembler, choose and merge the features columns from pyspark.ml.linalg import Vectors
  from pyspark.ml.feature import VectorAssembler
  assembler = VectorAssembler(inputCols=["Avg Session Length",…. ], outputCol="features") (indicate the right features columns)

### Steps to follow 2 of 2 :

- Assemble the data (look at the notebook of this morning to see again how it is done)
- Define the final dataset variable
  final_data = output.select("features",'Yearly Amount Spent’)
- Split your dataset in train and test (70%-30%) using randomSplit (look at the notebook of this morning to see again how it is done)
- Indicate to the LinearRegression function which column is the Label column
  lr = LinearRegression(labelCol='Yearly Amount Spent’)
- Fit the model (look at the notebook of this morning to see again how it is done)
- Run the model on your test dataset
  unlabeled_data = test_data.select('features’)
  predictions = lrModel.transform(unlabeled_data)
  predictions.show()
  You successfully have trained a model able to make predictions about the average
  amount spent per client.
