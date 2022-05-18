from core_bas import run_app
from login_manager import login
from PIL import ImageTk,Image
if (login()):
    run_app()
