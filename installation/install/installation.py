import os
import click
from tqdm import tqdm

@click.command()
def adding_user():
    click.confirm(f'Do you want to add the user with sudo access and switch to that user? {frappe_user}?', abort=True)
    frappe_user = click.prompt('Enter Frappe User')
    os.system(f'sudo adduser {frappe_user}')
    os.chdir(f'/home/{frappe_user}')
    os.system(f'usermod -aG sudo {frappe_user}')
    os.system(f'su {frappe_user}')
    display_progress_bar()

@click.command()
def frappe_installation():
    # Install prerequisites
    click.confirm('Do you want to install the prerequisites?', abort=True)
    prerequisites = [
        'mariadb-server', 'mariadb-client', 'redis-server',
        'supervisor',
        'curl', 'git',
        'python3-dev', 'python3.10-dev', 'python3-setuptools', 'python3-pip', 'python3-distutils', 'python3.10-venv',
        'software-properties-common',
        'xvfb', 'libfontconfig', 'wkhtmltopdf', 'libmysqlclient-dev'
    ]
    for command in commands:
        os.system(f"sudo apt install -y {prerequisites}")

    # Install nvm, npm and yarn
    commands = [
        'curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash',
        'source ~/.profile',
        'nvm install 16.15.0',
        'sudo apt-get install npm',
        'sudo npm install -g yarn'
    ]
    for command in commands:
        os.system(command)
    
    # Upgrade pip
    packages = [
        'pip3 install --upgrade --user pip',
        'sudo pip3 install frappe-bench',
    ]
    for package in packages:
        os.system(package)
    
    display_progress_bar()
    
def display_progress_bar():
    # Display progress bar
    with tqdm(total=100, desc='Processing', bar_format='{l_bar}{bar:50}{r_bar}') as pbar:
        for i in range(10):
            pbar.update(10)
    click.echo(click.style('Frappe installation completed successfully!', fg='green', bold=True))

if __name__ == '__main__':
    adding_user()
    frappe_installation()
