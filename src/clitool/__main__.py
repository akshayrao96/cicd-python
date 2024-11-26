""" Main Entry Point
"""
import click

@click.group()
def cli():
    """ Entry command group
    """

@cli.command()
@click.option('--name', default="user", help='name to greet')
def greet(name):
    """ Simple command to greet the user
    """
    click.echo(f"Hello {name}")
