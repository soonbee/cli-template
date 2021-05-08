import click


@click.group('update')
def command_group():
    pass


@command_group.command()
def something():
    click.echo('update something')
