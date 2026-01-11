import os

def is_module(folder):
    """Check if a folder is an Odoo module."""
    try:
        files = os.listdir(folder)
        return "__manifest__.py" in files or "__openerp__.py" in files
    except Exception:
        return False

def list_modules(path):
    """List modules in the given path."""
    if not os.path.exists(path):
        print("Error: Path does not exist.")
        return

    modules = []
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path) and is_module(full_path):
            modules.append(item)

    if modules:
        print("\nModules found:")
        for m in sorted(modules):
            print("", m)
    else:
        print("No modules found in this path.")

if __name__ == "__main__":
    repo_path = input("Enter the path to your repo: ").strip()
    list_modules(repo_path)