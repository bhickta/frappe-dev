import os
import click

@click.command()
def adding_user():
    root_password = click.prompt("Enter changed root password")
    os.system(f"echo 'root:{root_password}' | sudo chpasswd")
    frappe_user = click.prompt('Enter Frappe User')
    click.confirm(f'Do you want to add the user with sudo access and switch to that user? {frappe_user}?', abort=True)
    os.system(f'sudo adduser {frappe_user}')
    os.chdir(f'/home/{frappe_user}')
    os.system(f'usermod -aG sudo {frappe_user}')
    os.system(f'su {frappe_user}')

if __name__ == '__main__':
    adding_user()