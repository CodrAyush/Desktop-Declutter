import os
import shutil
import json
import logging

# Set up logging
logging.basicConfig(filename='restore.log', level=logging.INFO,
                   format='%(asctime)s - %(levelname)s - %(message)s')

# Load configuration
with open('config.json') as config_file:
    config = json.load(config_file)

desktop_path = os.path.expanduser(config["desktop_path"])
backup_folder = os.path.join(desktop_path, "Backup")

def restore_desktop():
    try:
        # Restore all files from backup to desktop
        for file in os.listdir(backup_folder):
            source = os.path.join(backup_folder, file)
            destination = os.path.join(desktop_path, file)
            
            if os.path.isfile(source):
                shutil.copy2(source, destination)
                logging.info(f"Restored {file} to desktop")
        
        # Remove the organized folders if they're empty
        folders_to_remove = list(config["custom_folders"].keys()) + ["Backup", "Sorted Files"]
        for folder in folders_to_remove:
            folder_path = os.path.join(desktop_path, folder)
            try:
                if os.path.exists(folder_path):
                    shutil.rmtree(folder_path)
                    logging.info(f"Removed folder: {folder}")
            except Exception as e:
                logging.error(f"Error removing folder {folder}: {e}")
                
        logging.info("Desktop restoration completed successfully")
        print("Desktop has been restored to its original state!")
        
    except Exception as e:
        logging.error(f"Error during restoration: {e}")
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    restore_desktop() 