import os
import click

@click.command()
def frappe_install():
    os.system('bench init --frappe-branch version-14 frappe-bench')
    os.system('chmod -R o+rx /home/frappe')
    os.chdir('/home/frappe/frappe-bench')
    os.system('bench new-site raplbaddi.com --db-name raplbaddi --db-password Impossible.dev1@')
    
    apps = {
        'erpnext': '--branch version-14 erpnext',
        'hrms': '--branch version-14 hrms',
        'ecommerce_integrations':'ecommerce_integrations --branch main',
        'india-compliance':'--branch version-14 https://github.com/resilient-tech/india-compliance.git',
        'helpdesk':'helpdesk'
    }
    for k, v in apps.items():
        os.system(f'bench get-app {v}')
        print(f"{k} has been pulled")
        os.system(f'bench --site raplbaddi.com install-app {k}')
        print(f"{k} has been installed")

if __name__ == '__main__':
    frappe_install()
