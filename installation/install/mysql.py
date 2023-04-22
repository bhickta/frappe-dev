import os
import click


@click.command()
def mysql_secure_installation():
    os.system('sudo mysql_secure_installation')
def mysql_conf():
    command = "sudo sh -c \"echo -e '\\n[mysqld]\\ncharacter-set-client-handshake = FALSE\\ncharacter-set-server = utf8mb4\\ncollation-server = utf8mb4_unicode_ci\\n\\n[mysql]\\ndefault-character-set = utf8mb4\\n' >> /etc/mysql/my.cnf\""
    os.system(command)
    os.system('sudo service mysql restart')

    
if __name__ == '__main__':
    mysql_secure_installation()
    mysql_conf()