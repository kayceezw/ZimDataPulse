# Fixed syntax errors in config.py

def load_config():
    try:
        with open('config.json') as config_file:
            config = json.load(config_file)
            return config
    except IOError as e:
        print(f"Error reading config file: {e}")
        return None

# Additional configuration settings can be added here...