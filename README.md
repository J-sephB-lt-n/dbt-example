# dbt-example

showcase of dbt functionality with a toy dataset

why use dbt? because it encourages and facilitates data warehouse and software best practices through it's design:

- snapshotting (is this data lineage?)

- documentation

- testing

- modularisation

- separation of environments (e.g. dev, staging, prod etc.)

- dry

specific features i want to document:

- snapshots

- source data freshness warnings

- singular data tests

- generic data tests

  - all 4 of the builtin one

  - define 1 myself (e.g. valid_id)

- unit tests

- dev/prod environment split

```bash
python -m venv venv
source venv/bin/activate
pip install --no-deps -r requirements.txt
dbt --version
dbt debug # check that everything set up correctly

python -m simdata.init_db --db_name 'dev'
dbt run
dbt test
dbt clean
rm databases/*
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
```

here are links to specific things in this project:

- [A custom generic data test](./tests/generic/test_is_valid_id.sql) (you can see it applied [here](./models/staging/data_tests.yml))
