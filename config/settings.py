from dotenv import load_dotenv
import os 

#OBTIENE LAS VARIABLES DEL .env
load_dotenv()
TOKEN_DISCORD = os.environ.get("TOKEN_DISCORD")