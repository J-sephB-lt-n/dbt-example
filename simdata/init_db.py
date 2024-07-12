import argparse
import datetime
import duckdb
import pathlib


def create_database(db_name: str) -> None:
    if not db_name.endswith(".duckdb"):
        db_name += ".duckdb"

    db_path = pathlib.Path(f"databases/{db_name}")
    if db_path.exists():
        db_path.unlink()
        print(f"Deleted existing database {db_path}")

    with duckdb.connect(f"databases/{db_name}") as con:
        con.execute(
            f"""
    CREATE SCHEMA IF NOT EXISTS raw_source_data
    ;

    CREATE TABLE IF NOT EXISTS raw_source_data.users (
            _data_loaded_at_utc STRING
        ,   email_address STRING
        ,   signup_datetime STRING
    );

    CREATE TABLE IF NOT EXISTS raw_source_data.orders (
            _data_loaded_at_utc STRING
        ,   order_id STRING
        ,   user_email_address STRING
        ,   amount STRING
        ,   order_datetime STRING
    );

    CREATE TABLE IF NOT EXISTS raw_source_data.bank (
            _data_loaded_at_utc STRING
        ,   order_id STRING
        ,   status STRING
    );
    INSERT INTO raw_source_data.users(_data_loaded_at_utc, email_address, signup_datetime)
    VALUES 
            ('{(datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(hours=-30)).strftime("%Y-%m-%d %H:%M:%S")}', 'a.person@email.com', '2069-07-24 17:05:55')
        ,   ('{(datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(hours=-30)).strftime("%Y-%m-%d %H:%M:%S")}', 'some.ne@el.se', '2420-12-24 13:04:15')
        ,   ('{(datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(hours=-30)).strftime("%Y-%m-%d %H:%M:%S")}', 'email@dre.ss', '2020-03-14 18:27:01')
    ;
    INSERT INTO raw_source_data.orders(_data_loaded_at_utc, order_id, user_email_address, amount, order_datetime)
    VALUES  ('{(datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(hours=-30)).strftime("%Y-%m-%d %H:%M:%S")}', '51469410', 'some.ne@el.se', '800.85', '2025-10-12 06:01:44')
        ,   ('{(datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(hours=-30)).strftime("%Y-%m-%d %H:%M:%S")}', '51469411', 'email@dre.ss', '27.95', '2025-10-12 06:05:39')
    ;
    INSERT INTO raw_source_data.bank(_data_loaded_at_utc, order_id, status)
    VALUES  ('{(datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(hours=-30)).strftime("%Y-%m-%d %H:%M:%S")}', '51469410', 'successful_payment')
    ;
    """
        )

    print(
        f"Database 'databases/{db_name}' created with schema 'raw_source_data' and tables 'users', 'cards', 'orders', and 'bank'."
    )


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        description="Create a DuckDB database with specified tables."
    )
    arg_parser.add_argument(
        "--db_name",
        required=True,
        help="The name of the DuckDB database to be created.",
    )

    # Parse the arguments
    args = arg_parser.parse_args()

    # Create the database with the specified name
    create_database(args.db_name)
