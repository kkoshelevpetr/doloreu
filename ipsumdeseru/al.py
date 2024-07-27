dataframe = dataframe.with_columns(pl.col("CommentDate").str.strptime(pl.Date, fmt='%Y-%m-%d').alias('CommentDate'))
