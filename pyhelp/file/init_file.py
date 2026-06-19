from .init_file_template import hello
from .init_file_template import click_
from .init_file_template import manim_
from .init_file_template import flask_
from .init_file_template import numpy_
def init_file(initfilename, initfileextname,initmode):
    import click
    if initmode not in ['hello', 'click', 'manim', 'flask', 'numpy']:
        raise RuntimeError("不支持的模式！仅支持 hello/click/manim/flask/numpy")

    click.echo('Init file 0%')
    with open(f'./{initfilename}.{initfileextname}', 'w', encoding='utf-8') as f:
        if initmode == 'hello':
            f.write(hello.hello())

        elif initmode == 'click':
            f.write(click_.click_1())
            click.echo('Init file 30%')
            f.write(click_.click_2())

        elif initmode == 'manim':
            f.write(manim_.manim_1())
            click.echo('Init file 30%')
            f.write(manim_.manim_2())
            click.echo('Init file 60%')
            f.write(manim_.manim_3())
        
        elif initmode == 'flask':
            f.write(flask_.flask_1())
            click.echo('Init file 30%')
            f.write(flask_.flask_2())
            click.echo('Init file 60%')
            f.write(flask_.flask_3())
        
        elif initmode == 'numpy':
            f.write(numpy_.numpy_1())
            click.echo("Init file 50%")
            f.write(numpy_.numpy_2())

        click.echo('Init file 100%')