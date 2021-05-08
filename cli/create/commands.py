import click


@click.group('create')
def command_group():
    pass


@command_group.command()
def something():
    click.echo('create something')
