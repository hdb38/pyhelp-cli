def click_1():
    return "import click\n\n\n"

def click_2():
    return """@click.command()
@click.option("--name","-n", default="World", help="Your name")
def hello(name):
    print(f"Hello, {name}!")
    
if __name__=="__main__":
    hello()"""