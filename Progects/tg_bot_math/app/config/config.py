from environs import Env

env = Env().read_env()
TOKEN_API = env.str("TOKEN_API")
