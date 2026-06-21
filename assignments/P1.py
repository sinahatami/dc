import pyspark.sql.functions as F
from pyspark.sql import SparkSession
from pyspark.sql.types import *

spark = SparkSession \
    .builder \
    .appName("first assignment") \
    .getOrCreate()


listeningsPath = "hdfs:/user/user_lsc_78/listenings.csv"
genresPath = "hdfs:/user/user_lsc_78/genre.csv"


schema_listening = StructType()\
         .add('user_id', StringType())\
         .add('date', StringType())\
         .add('track', StringType())\
         .add('artist', StringType())\
         .add('album', StringType())


listenings_df = spark.read.csv(listeningsPath, schema_listening)

schema_genres = StructType()\
         .add('artist', StringType())\
         .add('genre', StringType())

genres_df = spark.read.csv(genresPath, schema_genres)

networkPath = "hdfs:/user/user_lsc_78/network.csv"
schema_network = StructType()\
         .add('user_id1', StringType())\
         .add('user_id2', StringType())

network_df = spark.read.csv(networkPath, schema_network)



#QUERY---------------------------------------------------------

df_join = listenings_df.join(genres_df, 'artist', "inner").groupBy(['user_id', genres_df.genre]).count()
last_df = df_join.sort(F.col("count").desc())
last_df.show(10)
print(last_df.take(3))




#QUERY---------------------------------------------------------------
# get the list of users
users = network_df.select("user_id1").union(network_df.select("user_id2")).distinct().rdd.flatMap(lambda x: x).collect()

for user_id in users:
  # get the friends of user X
  friends = network_df.filter(network_df["user_id1"] == user_id).select("user_id2")

  # get the listenings of friends of user X
  friends_listenings = listenings_df.join(friends, listenings_df["user_id"] == friends["user_id2"], "inner")

  # get the genres of listenings of friends of user X
  friends_listenings_genres = friends_listenings.join(genres_df, ["artist"], "inner").select("user_id2", "track", "artist", "album", "genre")

  # get the genres of songs listened to by user X
  user_genres = listenings_df.filter(listenings_df["user_id"] == user_id).join(genres_df, ["artist"], "inner").select("genre").distinct()

  # get the top 3 most listened songs among friends of user X with a common genre with X
  result = friends_listenings_genres.join(user_genres, friends_listenings_genres["genre"] == user_genres["genre"], "inner") \
    .groupBy(["track", "artist", "album"]).agg(F.count("*").alias("listens")) \
    .sort(F.desc("listens")).limit(3)

  print("For user", user_id, ":")
  result.show()

