import click
import numpy as np
from numpy import pi
import pandas as pd

# Making command group
@click.group()
def cmd_group():
    pass

# creating subcommand with optional amount of steps
@cmd_group.command()
@click.option(
"-c",
"--count",
default=10,
help="Number of times to print greeting.",
show_default=True, # show default in help
)
# Creating sine function
def sin(count): 
    x = np.linspace(0, 2 * pi, count)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

# creating subcommand with optional amount of steps
@cmd_group.command()
@click.option(
"-c",
"--count",
default=10,
help="Number of times to print greeting.",
show_default=True, # show default in help
)
# Creating tan function
def tan(count):
    x = np.linspace(0, 2 * pi, count)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


if __name__ == "__main__":
    cmd_group()