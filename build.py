min_port = 1
max_port = 30000

with open("every_port.out", "w") as m:
    for port in range(min_port, max_port + 1):
        m.write("python {flask_app} {port} &\n".format(
            flask_app='every_port.py',
            port=port
        ))
