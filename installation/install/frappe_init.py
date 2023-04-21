import os
import click


@click.command()
def mysql_secure_installation():
    root_password = click.prompt("Enter current root password")
    mysql_password = click.prompt("Enter changed root password for mysql")
    os.system(
        f'''echo -e "y\n${root_password}\n${mysql_password}\ny\ny\ny\ny" | sudo mysql_secure_installation''')


@click.command()
def frappe_install():
    commands = [
        'bench init --frappe-branch version-14 frappe-bench',
        'cd frappe-bench',
        'chmod -R o+rx /home/frappe',
        'bench new-site raplbaddi.com --db-name raplbaddi --db-password Impossible.dev1@'
    ]

    for command in commands:
        os.system(command)

    apps = [
        '--branch version-14 erpnext',
        '--branch version-14 hrms',
        'ecommerce_integrations',
        '--branch version-14 https://github.com/resilient-tech/india-compliance.git',
        'helpdesk'
    ]
    for app in apps:
        os.system(f'bench get-app {app}')
        os.system(f'bench --site raplbaddi.com install-app {app}')

if __name__ == '__main__':
    # mysql_secure_installation()
    frappe_install()
