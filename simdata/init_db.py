import argparse
import duckdb
import pathlib


def create_database(db_name: str) -> None:
    if not db_name.endswith(".db"):
        db_name += ".db"

    db_path = pathlib.Path(db_name)
    if db_path.exists():
        db_path.unlink()
        print(f"Deleted existing database {db_path}")

    with duckdb.connect(f"databases/{db_name}") as con:
        con.execute(
            """
    CREATE SCHEMA IF NOT EXISTS raw_source_data;

    CREATE TABLE IF NOT EXISTS raw_source_data.users (
        email_address STRING,
        signup_datetime STRING
    );

    CREATE TABLE IF NOT EXISTS raw_source_data.cards (
        email_address STRING,
        card_num STRING
    );

    CREATE TABLE IF NOT EXISTS raw_source_data.orders (
        order_id STRING,
        amount STRING,
        pay_ref STRING,
        order_datetime STRING
    );

    CREATE TABLE IF NOT EXISTS raw_source_data.bank (
        pay_ref STRING,
        status STRING
    );
    """
        )
        con.execute(
            """
    INSERT INTO raw_source_data.users(email_address, signup_datetime)
    VALUES ('andrej.karpathy@gmail.com', '2069-07-24 17:05:55')
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
