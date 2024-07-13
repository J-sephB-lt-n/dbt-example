import argparse
import duckdb


def add_non_valid_order_id(db_name: str) -> None:
    """Adds a row with an invalid order into into the raw_source_data.orders table"""
    if not db_name.endswith(".duckdb"):
        db_name += ".duckdb"

    with duckdb.connect(f"databases/{db_name}") as con:
        con.execute(
            """
    INSERT INTO raw_source_data.orders(_data_loaded_at_utc, order_id, user_email_address, amount, order_datetime)
    VALUES  ('2345-02-14 06:09:42', '1234567', 'a.person@email.com', '844.50', '2025-10-14 17:05:11')
    ;
    """
        )

    print(
        f"Added row with invalid order_id into table raw_source_data.orders in database {db_name}"
    )


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        description="Add a row containing an invalid order ID into the tabl raw_source_data.orders"
    )
    arg_parser.add_argument(
        "--db_name",
        required=True,
        help="The name of the DuckDB database to write data into",
    )

    # Parse the arguments
    args = arg_parser.parse_args()

    # Create the database with the specified name
    add_non_valid_order_id(args.db_name)
