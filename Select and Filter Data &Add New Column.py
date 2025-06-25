df.filter(df.Age > 25).select("Name").show()
df_with_new = df.withColumn("DoubleAge", df.Age * 2)
df_with_new.show()

