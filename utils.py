from app.config import APP_NAME

def get_welcome_message(name: str) -> str:
    return f"Welcome to {APP_NAME}, {name}!"