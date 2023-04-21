import os
import click


@click.command()
def mysql_secure_installation():
    # root_password = click.prompt("Enter current root password")
    # mysql_password = click.prompt("Enter changed root password for mysql")
    # os.system(
    #     f'''echo -e "y\n${root_password}\n${mysql_password}\ny\ny\ny\ny" | sudo mysql_secure_installation''')
    os.system('mysql_secure_installation')
    
if __name__ == '__main__':
    mysql_secure_installation()