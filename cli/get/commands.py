import click


@click.group('get')
def command_group():
    pass


@command_group.command()
def something():
    click.echo('show something')
