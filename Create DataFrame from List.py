data = [("Alice", 23), ("Bob", 30)]
columns = ["Name", "Age"]

df = spark.createDataFrame(data, columns)
df.show()
