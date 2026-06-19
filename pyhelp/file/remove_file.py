def remove_file(removefilename, removeextname):
    import click
    import os
    click.echo('Remove file 0%')
    file_path = os.path.join(os.getcwd(), f"{removefilename}.{removeextname}")
    os.remove(file_path)
    click.echo('Remove file 100%')