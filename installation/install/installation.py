import os
import click

@click.command()
def frappe_installation():
    # Turn of restart prompt
    restart_prompt = '''sudo sh -c "echo '$nrconf{restart} = '\''a'\'';' >> /etc/needrestart/needrestart.conf"'''
    os.system(restart_prompt)
    
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
    for prerequisite in prerequisites:
        os.system(f"sudo apt install -y {prerequisite}")

    # Install nvm, npm and yarn
    commands = [
        'curl -o install.sh https://raw.githubusercontent.com/creationix/nvm/master/install.sh| bash',
        'source ~/.profile',
        'nvm install 16.15.0 -y',
        'sudo apt-get install npm -y',
        'sudo npm install -g yarn'
    ]
    for command in commands:
        os.system(f"{command} \n")
    
    # Upgrade pip
    packages = [
        'pip3 install --upgrade --user pip',
        'sudo pip3 install frappe-bench',
    ]
    for package in packages:
        os.system(package)
    
    click.echo(click.style('Frappe installation completed successfully!', fg='green', bold=True))

if __name__ == '__main__':
    frappe_installation()
