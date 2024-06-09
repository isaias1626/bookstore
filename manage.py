#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import os

print("DATABASE CONFIGURATION:")
print("ENGINE:", os.environ.get('SQL_ENGINE'))
print("NAME:", os.environ.get('SQL_DATABASE'))
print("USER:", os.environ.get('SQL_USER'))
print("PASSWORD:", os.environ.get('SQL_PASSWORD'))
print("HOST:", os.environ.get('SQL_HOST'))
print("PORT:", os.environ.get('SQL_PORT'))



def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
