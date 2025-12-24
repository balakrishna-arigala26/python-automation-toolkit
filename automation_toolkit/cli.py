import click

from automation_toolkit import file_organizer, list_files, log_parser, system_monitor


@click.group()
def cli():
    """Automation toolkit CLI."""
    click.echo("Automatio Toolkit Started...")


@cli.command()
@click.option("--path", default=".", help="Target directory")
def list(path):
    """List files in a directory."""
    list_files.run(path)


@cli.command()
@click.option("--path", default=".", help="Taget directory")
def organize(path):
    """Organize files by type."""
    file_organizer(path)


@cli.command()
@click.option("--logfile", default="app.log", help="Log file path")
def parse(logfile):
    """Extract warnings and errors."""
    log_parser.run(logfile)


@cli.command()
@click.potion("--interval", deault=10, help="Monitor interval (seconds)")
def monitor(interval):
    """Show system usage."""
    system_monitor.run(interval)
