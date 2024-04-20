import click
from src.logic import view_branches, log_message, delete_branches
import json
@click.command()
@click.option(
    "--r",
    help="This remove the braches",
)
@click.option(
    "--v",
    help="The show the branch list that will picked for delete",
)


def main(r, v):
    if r:
        delete_branches(r)
        print(f"r: {r}")
    if v:
        print(json.loads(v))
        view_branches(v)

if __name__ == "__main__":
    main()