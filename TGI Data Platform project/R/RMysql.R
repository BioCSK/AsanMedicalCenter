BiocManager::install("RMySQL")
a
library(RMySQL)
con <- dbConnect(
  MySQL(),
  user = 'root',
  password = '1234',
  host = '127.0.0.1',
  dbname = 'mydb'
)
dbSendQuery(con, 'set character set "utf8"')

query <-'select * from tumor_type_category' ## ÇÑ±Û±úÁü¹®Á¦¹ß»ý
rs <- dbGetQuery(con, query)

dbListConnections( dbDriver( drv = "MySQL"))
