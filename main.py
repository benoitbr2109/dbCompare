import polars as pl
import urllib

db_path_1 = urllib.parse.quote("G:\\Documents\\Python\\dbCompare\\test1.db") 
db_path_2 = urllib.parse.quote("G:\\Documents\\Python\\dbCompare\\test2.db") 

conn1 = 'sqlite://' + db_path_1

query = "SELECT * FROM tbl1"

def main():
    df = pl.read_database_uri(
        query,
        conn1,
        engine="connectorx",
    )
    print(df)


if __name__ == "__main__":
    main()
