from click.utils import echo
import typer
from lib.install import install_font
from lib.uninstall import uninstall_font

app = typer.Typer()

@app.command()
def install(font_name: str):
    install_font(font_name)
    
@app.command()
def uninstall(font_name: str):
    uninstall_font(font_name)


@app.command()
def update():
    # update the font file(s) in the system
    typer.echo("Font update started")

@app.command("update-cache")
def update_cache():
    typer.echo("Font cache reset started")

if __name__ == "__main__":
    app()