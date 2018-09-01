def inject_command(client, command):
    #stdin, stdout, stderr = client.exec_command("ls")

    stdin, stdout, stderr = client.exec_command(command)
    #stdin, stdout, stderr = client.exec_command(command2)
    console = stdout.read().splitlines()

    client.close()
    return console
