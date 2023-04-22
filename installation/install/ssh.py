import os
import click


def domain():
    commands = [
        'bench setup add-domain dev.raplbaddi.com',
        'bench setup nginx',
        'sudo service nginx reload',
        'sudo apt install certbot'
        ]
    for command in commands:
        os.system(command)

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
    domain()
    ssh()
