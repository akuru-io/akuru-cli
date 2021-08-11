from click.utils import echo
import typer

app = typer.Typer()

@app.command()
def install():
    typer.echo("Font install started")

@app.command()
def uninstall():
    typer.echo("Font uninstall started")

@app.command()
def update():
    typer.echo("Font update started")

@app.command("update-cache")
def update_cache():
    typer.echo("Font cache reset started")

if __name__ == "__main__":
    app()