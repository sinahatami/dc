import pyspark.sql.functions as F
from pyspark.sql import SparkSession
from pyspark.sql.types import *

spark = SparkSession \
    .builder \
    .appName("second query") \
    .getOrCreate()


listeningsPath = "hdfs:/user/user_lsc_78/listenings.csv"
networkPath = "hdfs:/user/user_lsc_78/network.csv"


schema_listening = StructType()\
         .add('user_id', StringType())\
         .add('date', StringType())\
         .add('track', StringType())\
         .add('artist', StringType())\
         .add('album', StringType())


listenings_df = spark.read.csv(listeningsPath, schema_listening)

schema_network = StructType()\
         .add('user_id1', StringType())\
         .add('user_id2', StringType())


network_df = spark.read.csv(networkPath, schema_network)


#QUERY------------------------------------------------------------
res_join = listenings_df.join(network_df)
where_res = res_join.where("user_id == user_id2")
groupBy_res = where_res.groupBy('user_id1', 'track').agg(F.count(listenings_df.track)).sort(F.col("count(track)").desc())
groupBy_res.show(10)
print(groupBy_res.take(3))




user_id = "X" # replace X with actual user id

# get the friends of user X
friends = network_df.filter(network_df["user_id1"] == user_id).select("user_id2")

# get the listenings of friends of user X
friends_listenings = listenings_df.join(friends, listenings_df["user_id"] == friends["user_id2"], "inner")

# get the top 3 most listened songs among friends of user X
result = friends_listenings.groupBy(["track", "artist", "album"]).agg(F.count("*").alias("listens")).sort(F.desc("listens")).limit(3)

result.show()
