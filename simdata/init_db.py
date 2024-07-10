import argparse
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
            """
    CREATE SCHEMA IF NOT EXISTS raw_source_data
    ;

    CREATE TABLE IF NOT EXISTS raw_source_data.users (
        email_address STRING,
        signup_datetime STRING
    );

    CREATE TABLE IF NOT EXISTS raw_source_data.cards (
        email_address STRING,
        card_num STRING
    );

    CREATE TABLE IF NOT EXISTS raw_source_data.orders (
            order_id STRING
        ,   user_email_address STRING
        ,   amount STRING
        ,   order_datetime STRING
    );

    CREATE TABLE IF NOT EXISTS raw_source_data.bank (
            order_id STRING
        ,   status STRING
    );
    INSERT INTO raw_source_data.users(email_address, signup_datetime)
    VALUES 
            ('a.person@email.com', '2069-07-24 17:05:55')
        ,   ('some.ne@el.se', '2420-12-24 13:04:15')
        ,   ('email@dre.ss', '2020-03-14 18:27:01')
    ;
    INSERT INTO raw_source_data.orders(order_id, user_email_address, amount, order_datetime)
    VALUES  ('51469410', 'some.ne@el.se', '800.85', '2025-10-12 06:01:44')
        ,   ('51469411', 'email@dre.ss', '27.95', '2025-10-12 06:05:39')
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
