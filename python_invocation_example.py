from dbt.cli.main import dbtRunner, dbtRunnerResult

# initialize
dbt = dbtRunner()

# run the command
res: dbtRunnerResult = dbt.invoke(["test", "--select", "staging"])

# inspect the results
for r in res.result:
    print(f"{r.node.name}: {r.status}")
