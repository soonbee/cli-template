import click
from .get import commands as get
from .create import commands as create
from .update import commands as update
from .delete import commands as delete


@click.group()
def entry_point():
    pass

entry_point.add_command(get.command_group)
entry_point.add_command(create.command_group)
entry_point.add_command(update.command_group)
entry_point.add_command(delete.command_group)
