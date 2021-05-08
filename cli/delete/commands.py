import click


@click.group('delete')
def command_group():
    pass


@command_group.command()
def something():
    click.echo('show something list')
