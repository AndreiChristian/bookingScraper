from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegression
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler

# Step 1: Import the dataset
spark = SparkSession.builder.appName('lr_project').getOrCreate()
data = spark.read.csv("./data_linear_regression.csv", inferSchema=True, header=True)

# Step 2: Choose feature and label columns
data.printSchema()

# Email,Address,Avatar,Avg Session Length,Time on App,Time on Website,Length of Membership,Yearly Amount Spent

# Step 3: Merge the feature columns
assembler = VectorAssembler(inputCols=["Avg Session Length", "Time on App", "Time on Website", "Length of Membership"], outputCol="features")
output = assembler.transform(data)

# Step 4: Define the final dataset variable
final_data = output.select("features", 'Yearly Amount Spent')

# Step 5: Split the data into train and test datasets
train_data, test_data = final_data.randomSplit([0.7, 0.3])

# Step 6: Define the linear regression model
lr = LinearRegression(labelCol='Yearly Amount Spent')

# Step 7: Train the model using the training dataset
lrModel = lr.fit(train_data)

# Step 8: Use the test dataset to make predictions
unlabeled_data = test_data.select('features')
predictions = lrModel.transform(unlabeled_data)
predictions.show()

