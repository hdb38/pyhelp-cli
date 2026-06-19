def create_dir(dirname):
    import click
    from pathlib import Path
    click.echo('Create dir 0%')
    dir_path = Path(f'./{dirname}')
    click.echo('Create dir 50%')
    dir_path.mkdir(exist_ok=True)
    click.echo('Create dir 100%')