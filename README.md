# dbt-example

Showcase of DBT functionality with a toy dataset

Why use DBT? Because it encourages and facilitates data warehouse and software best practices through it's design:

- Snapshotting (is this data lineage?)

- Documentation

- Testing

- Modularisation

- Separation of environments (e.g. dev, staging, prod etc.)

- DRY

```bash
python -m venv venv
source venv/bin/activate
pip install --no-deps -r requirements.txt
dbt --version
dbt debug # check that everything set up correctly

python -m simdata.init_db --db_name 'dev'

```
