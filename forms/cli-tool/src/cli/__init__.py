"""CLI command definitions."""
import click
from rich.console import Console

console = Console()

@click.group()
@click.version_option(version='0.1.0')
def main():
    """CLI Tool - Replace with your tool description."""
    pass

@main.command()
@click.argument('name')
def hello(name):
    """Say hello to NAME.
    
    Example:
        mytool hello World
    """
    console.print(f"[green]Hello, {name}![/green]")

if __name__ == '__main__':
    main()
