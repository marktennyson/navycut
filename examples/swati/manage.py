from os import environ


def main():
    """
    Run all the manager commands.
    """
    environ.setdefault('NAVYCUT_SETTINGS_MODULE', 'swati.settings')
    
    try:
        from navycut.command import manage_command
    
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Navycut. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    manage_command()

if __name__ == '__main__':
    main()