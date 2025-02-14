import os
from textsummarizer.logging import logger

class DataValidation:
    def __init__(self, config):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        logger.info("DataValidation: Starting validation of required files...")
        # Define the directory where the ingestion stage output is located.
        # Update this path if your ingestion output folder is different.
        ingestion_output_dir = os.path.join("artifacts", "data_ingestion", "samsum_dataset")
        
        # Check if the ingestion output directory exists
        if not os.path.exists(ingestion_output_dir):
            logger.error(f"DataValidation: Ingestion output directory not found: {ingestion_output_dir}")
            return False
        
        # List the files or subdirectories in the ingestion output directory
        available_items = os.listdir(ingestion_output_dir)
        logger.info(f"DataValidation: Found items: {available_items}")
        
        # Get the required items from the configuration
        required_items = self.config.ALL_REQUIRED_FILES  # e.g., ["train", "test", "validation"]
        logger.info(f"DataValidation: Required items: {required_items}")
        
        # Check that every required item is present
        validation_status = all(item in available_items for item in required_items)
        logger.info(f"DataValidation: Validation status: {validation_status}")
        
        # Write the validation result to the status file
        try:
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")
            logger.info(f"DataValidation: Wrote validation status to {self.config.STATUS_FILE}")
        except Exception as e:
            logger.exception(f"DataValidation: Failed to write status file: {e}")
            return False
        
        return validation_status

    # Optionally, you can keep your download and extract methods if you need them for other purposes.
    def download_file(self):
        logger.info("DataValidation: No download needed for validation stage.")

    def extract_zip_file(self):
        logger.info("DataValidation: No extraction needed for validation stage.")
