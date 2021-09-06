from click.utils import echo
import typer
import os
import shutil
import sys
from lib.install import install_font

app = typer.Typer()

@app.command()
def install():
    # download the font from the remote
    # install the font into the system
    install_font()
    
@app.command()
def uninstall():
    # uninstall the font from the system
    typer.echo("Font uninstall started")

@app.command()
def update():
    # update the font file(s) in the system
    typer.echo("Font update started")

@app.command("update-cache")
def update_cache():
    typer.echo("Font cache reset started")

if __name__ == "__main__":
    app()