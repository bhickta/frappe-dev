import os
import click


def domain():
    commands = [
        'bench setup add-domain dev.raplbaddi.com',
        'bench setup nginx',
        'sudo service nginx reload'
        ]
    for command in commands:
        os.system(command)

if __name__ == '__main__':
    domain()