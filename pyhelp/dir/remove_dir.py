def remove_dir(dirname):
    import click
    from pathlib import Path
    import shutil
    click.echo('remove dir 0%')
    dir_path = Path(f'./{dirname}')
    click.echo('remove dir 50%')

    if not any(dir_path.iterdir()):
        dir_path.rmdir()
    else:
        shutil.rmtree(dir_path)

    click.echo('remove dir 100%')