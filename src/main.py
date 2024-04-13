import click
from src.logic import view_branches, log_message
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
        log_message("Removing branches that are picked for removal")
        print(f"r: {r}")
    
    if v:
        log_message("Viewing branches that are picked for removal")
        print(json.loads(v))
        view_branches(v)
       
    # if location:
    #     area(location)
    # if zone:
    #     area_zone(zone)

if __name__ == "__main__":
    main()