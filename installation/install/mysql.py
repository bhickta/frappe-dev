import os
import click


@click.command()
def mysql_secure_installation():
    os.system('sudo mysql_secure_installation')
    
if __name__ == '__main__':
    mysql_secure_installation()