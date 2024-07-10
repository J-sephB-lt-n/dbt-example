# dbt-example

Showcase of DBT functionality with a toy dataset

Why use DBT? Because it encourages and facilitates data warehouse and software best practices through it's design:

- Snapshotting (is this data lineage?)

- Documentation

- Testing

- Modularisation

- Separation of environments (e.g. dev, staging, prod etc.)

- DRY

Specific features I want to document:

- Snapshots

- Source data freshness warnings

- Singular data tests

- Generic data tests

- Unit tests

- Dev/prod environment split

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

Although it is outside the repo, my ~/.dbt/profiles.yml looks like this:

```yaml
dbt_example:
  target: dev
  outputs:
    dev:
      type: duckdb
      path: "databases/dev.duckdb"
      schema: main # default target schema
```
