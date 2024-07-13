# dbt-example

Showcase of dbt functionality with a toy dataset - I use this repo to remind myself of the features of DBT and how they work.

I am using a local DuckDB database.

Why use DBT? Because it encourages and facilitates data warehouse and software best practices through it's design:

- Data lineage (e.g. logging, snapshots)

- Documentation

- Testing

- Modularisation

- Separation of environments (e.g. dev, staging, prod)

- DRY

- Version control

The DBT best practice guide is amazing: <https://docs.getdbt.com/best-practices>

After running each step, you can see the changes made within the database itself using (e.g. run this in the duckdb cli):

```sql
select table_catalog, table_schema, table_name, table_type from information_schema.tables;
```

```bash
python -m venv venv
source venv/bin/activate
pip install --no-deps -r requirements.txt
dbt --version
dbt debug # check that everything set up correctly

python -m simdata.init_db --db_name 'dev' # creates data in database databases/dev.duckdb
dbt source freshness # check freshness of input data
dbt run # run dbt models
dbt test # run all tests

dbt snapshot # create snapshot tables
python -m simdata.update_payment_status_example --db_name 'dev' # adds a row to the bank table so can see pay_status_snapshot table working
dbt run # refresh pipeline to take into account new row in bank table
dbt snapshot

dbt docs generate
dbt docs serve

# tidy up
dbt clean # clean up dbt project
rm databases/* # remove databases
```

although it is outside the repo, my ~/.dbt/profiles.yml looks like this:

```yaml
dbt_example:
  target: dev
  outputs:
    dev:
      type: duckdb
      path: "databases/dev.duckdb"
      schema: main # default target schema
      threads: 4
```

here are links to specific things in this project:

- [A custom generic data test](./tests/generic/test_is_valid_id.sql) (you can see it applied [here](./models/staging/data_tests.yml))
  - You can run `python -m simdata.add_non_valid_order_id --db_name dev` to add a non-valid ID into the source data if you want to see the test fail (you will need to run `dbt run` before `dbt test` in order to see the test fail)
