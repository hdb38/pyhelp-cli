import click
from .file import create_file as c
from .file import init_file as i
from .file import replace_file_name as replace
from .file import remove_file as remove
from .file import list_init as l

from .dir import create_dir as cd
from .dir import remove_dir as rd

from .log import log, level

from .GUI.window import start_GUI

@click.group()
def cli():
    """🔥 PyHelp - Python 文件快速管理工具"""

@cli.command()
def GUI():
    start_GUI()

@cli.command()
@click.option('--filename', '-fn', help='文件名', type=str)
@click.option('--extname','-en', help="拓展名",type=str, default="py")
@click.option('--uselog','-ul', help="是否使用Log", type=bool)
def create_file(filename, extname, uselog):
    if uselog:
        log.Log.write_to_file(level.INFO(), f"Create-file file_name={filename}, extname={extname}")
    c.create_file(filename, extname)
    if uselog:
        log.Log.write_to_file(level.SUCCESS(), f"Create-file file_name={filename}, extname={extname}")


@cli.command()
@click.option('--initfilename', '-ifn', help='要初始化的文件名', type=str)
@click.option('--initfileextname','-ifen', help='要初始化的文件拓展名', default="py", type=str)
@click.option('--initmode', '-im', default='hello', help='模式：hello, click, manim, flask', type=str)
@click.option('--uselog','-ul', help="是否使用Log", type=bool)
def init_file(initfilename, initfileextname, initmode, uselog):
    if uselog:
        log.Log.write_to_file(level.INFO(), "Init-file initfile_name="+initfilename+", initmode="+initmode)
    i.init_file(initfilename,initfileextname,initmode)
    if uselog:
        log.Log.write_to_file(level.SUCCESS(), "Init-file initfile_name="+initfilename+", initmode="+initmode)


@cli.command()
@click.option('--oldfilename', '-ofn', help='旧文件名', type=str)
@click.option('--newfilename', '-nfn', help='新文件名', type=str)
@click.option('--uselog','-ul', help="是否使用Log", type=bool)
def replace_file_name(oldfilename, newfilename, uselog):
    if uselog:
        log.Log.write_to_file(level.INFO(), "Replace-file-name oldfilename="+oldfilename+", newfilename="+newfilename)
    replace.replace_file_name(oldfilename,newfilename)
    if uselog:
        log.Log.write_to_file(level.SUCCESS(), "Replace-file-name oldfilename="+oldfilename+", newfilename="+newfilename)

@cli.command()
@click.option('--uselog','-ul', help="是否使用Log", type=bool)
def init_list(uselog):
    if uselog:
        log.Log.write_to_file(level.INFO(), "List-init")
    l.list_init()
    if uselog:
        log.Log.write_to_file(level.SUCCESS(), "List-init")

@cli.command()
@click.option('--removefilename', '-rfn', help='要删除的文件名', type=str)
@click.option('--removefileextname', '-rfen', help='要删除的文件拓展名', default="py", type=str)
@click.option('--uselog','-ul', help="是否使用Log", type=bool)
def remove_file(removefilename, removefileextname, uselog):
    if uselog:
        log.Log.write_to_file(level.INFO(), "Remove-file removefilename="+removefilename)
    remove.remove_file(removefilename, removefileextname)
    if uselog:
        log.Log.write_to_file(level.SUCCESS(), "Remove-file removefilename="+removefilename)


@cli.command()
@click.option('--dirname','-dn', help='文件夹名称')
@click.option('--uselog','-ul', help="是否使用Log", type=bool)
def create_dir(dirname, uselog):
    if uselog:
        log.Log.write_to_file(level.INFO(), "Create-dir dirname="+dirname)
    cd.create_dir(dirname)
    if uselog:
        log.Log.write_to_file(level.SUCCESS(), "Create-dir dirname="+dirname)


@cli.command()
@click.option('--removedirname','-rdn', help='要删除的文件夹名')
@click.option('--uselog','-ul', help="是否使用Log", type=bool)
def remove_dir(removedirname, uselog):
    if uselog:
        log.Log.write_to_file(level.INFO(), "Remove-dir removedirname="+removedirname)
    rd.remove_dir(removedirname)
    if uselog:
        log.Log.write_to_file(level.SUCCESS(), "Remove-dir removedirname="+removedirname)

@cli.command()
def clean_log():
    click.echo("Clean log 0%")
    log.Log.clean_file()
    click.echo("Clean log 100%")

@cli.command()
def version():
    click.echo("version: 8.0.0")

if __name__ == '__main__':
    cli()