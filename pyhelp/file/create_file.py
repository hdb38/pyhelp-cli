def create_file(filename, extname):
    import click
    click.echo('New file 0%')
    with open(f'./{filename}.{extname}', 'w', encoding='utf-8'):
        click.echo('New file 50%')
    click.echo('New file 100%')