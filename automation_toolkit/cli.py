import click


@click.command()
@click.option(
    "--interval", default=10, show_default=True, help="Monitor interval in seconds"
)
def main(interval):
    """Python Automation Toolkit CLI"""
    click.echo(f"Monitoring every {interval} seconds")


if __name__ == "__main__":
    main()
