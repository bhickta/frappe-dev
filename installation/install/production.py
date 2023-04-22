import os
import click


@click.command()
def production():
    commands = [
        'bench --site raplbaddi.com enable-scheduler',
        'bench --site raplbaddi.com set-maintenance-mode off',
        'sudo bench setup production frappe',
        'bench setup nginx',
        'sudo supervisorctl restart all',
        'sudo bench setup production frappe'
    ]
    for command in commands:
        os.system(command)

if __name__ == '__main__':
    production()
