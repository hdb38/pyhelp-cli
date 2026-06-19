def replace_file_name(oldfilename,newfilename):
    import click
    import os
    click.echo('Replace file name 0%')
    old_path = os.path.join(os.getcwd(), f"{oldfilename}.py")
    new_path = os.path.join(os.getcwd(), f"{newfilename}.py")
    click.echo("Replace file name 50%")
    os.rename(old_path, new_path)
    click.echo('Replace file name 100%')
