import os


def shell_source(script):
    """Sometime you want to emulate the action of "source" in bash,
    settings some environment variables. Here is a way to do it."""
    import os
    import subprocess

    pipe = subprocess.Popen(". %s; env" % script, stdout=subprocess.PIPE, shell=True)
    output = pipe.communicate()[0]
    env = dict((line.split("=", 1) for line in output.splitlines()))
    os.environ.update(env)


class PostgreConnector:
    def __init__(self, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_URL, POSTGRES_DB):
        self.POSTGRES_USER = POSTGRES_USER
        self.POSTGRES_PASSWORD = POSTGRES_PASSWORD
        self.POSTGRES_URL = POSTGRES_URL
        self.POSTGRES_DB = POSTGRES_DB

    def get_env_variable(name):
        env_var = os.environ.get(name)
        if not env_var:
            raise Exception(f"Expected environment variable {name} not set.")
        return env_var

    def path_to_PostgreSQL():
        """Create path to POSGRESQL BD"""
        return f"postgresql+psycopg2://{credentials.POSTGRES_USER}:{credentials.POSTGRES_PASSWORD}@{credentials.POSTGRES_URL}/{credentials.POSTGRES_DB}"


credentials = PostgreConnector(
    POSTGRES_USER=PostgreConnector.get_env_variable("POSTGRES_USER"),
    POSTGRES_PASSWORD=PostgreConnector.get_env_variable("POSTGRES_PASSWORD"),
    POSTGRES_URL=PostgreConnector.get_env_variable("POSTGRES_URL"),
    POSTGRES_DB=PostgreConnector.get_env_variable("POSTGRES_DB"),
)

DB_path = PostgreConnector.path_to_PostgreSQL()
