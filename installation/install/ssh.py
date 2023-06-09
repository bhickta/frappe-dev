import os
import click

@click.command()
def ssh():
    commands = [
        'bench config dns_multitenant on',
        'bench setup nginx',
        'sudo service nginx reload'
    ]
    for command in commands:
        os.system(command)

if __name__ == '__main__':
    ssh()