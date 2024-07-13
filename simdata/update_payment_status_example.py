import argparse
import duckdb


def add_bank_entry(db_name: str) -> None:
    """Add a row to the bank table in order to trigger a payment status update"""
    if not db_name.endswith(".duckdb"):
        db_name += ".duckdb"

    with duckdb.connect(f"databases/{db_name}") as con:
        con.execute(
            """
    INSERT INTO raw_source_data.bank(_data_loaded_at_utc, order_id, status, entry_datetime)
    VALUES  ('2026-09-24 21:04:20', '51469411', 'fraud', '2025-10-12 06:19:10')
    ;
    """
        )

    print("Added row to bank table")


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        description="Add an entry (row) into the bank raw source data table"
    )
    arg_parser.add_argument(
        "--db_name",
        required=True,
        help="The name of the DuckDB database to write data into",
    )

    # Parse the arguments
    args = arg_parser.parse_args()

    # Create the database with the specified name
    add_bank_entry(args.db_name)
