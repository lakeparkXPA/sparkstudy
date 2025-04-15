# simpleApp
from pyspark.sql import SparkSession

logFile = "README.md"
spark = SparkSession.builder.appName("SimpleApp").config('spark.driver.bindAddress', '127.0.0.1').getOrCreate()
logData = spark.read.text(logFile).cache()

num2s = logData.filter(logData.value.contains('2')).count()
num5s = logData.filter(logData.value.contains('5')).count()

print(f"Lines with 2: {num2s}, lines with 5: {num5s}")

spark.stop()