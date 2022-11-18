import click
import numpy as np
from numpy import pi
import pandas as pd

# Making command group
@click.group()
def cmd_group():
    """creating a command group were you can add subcommands.
    """    
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
    """Making a sine function that runs from 0 till 2pi. Then making a dataframe of the input and output and printing that.

    Args:
        count (int): number of steps between 0 and 2pi
    """
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
    """Making a tangent function that runs from 0 till 2pi. Then making a dataframe of the input and output and printing that.

    Args:
        count (int): number of steps between 0 and 2pi
    """    
    x = np.linspace(0, 2 * pi, count)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


if __name__ == "__main__":
    cmd_group()