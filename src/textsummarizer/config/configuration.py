from textsummarizer.constants import *
from textsummarizer.utils.common import read_yaml, create_directories
from textsummarizer.entity.config import (DataIngestionConfig)

class ConfigurationManager:
    def __init__(self, config_file: str = CONFIG_FILE_PATH, params_file: str = PARAMS_FILE_PATH):
        self.config = read_yaml(config_file)
        self.params = read_yaml(params_file)

        # Fix: Access artifacts_root correctly
        create_directories([self.config["artifacts_root"]])

    # Fix: Ensure method is inside the class with proper indentation
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config["data_ingestion"]  # Fix: Access dictionary correctly
        
        create_directories([config["root_dir"]])

        # Fix: Use dictionary keys correctly
        data_ingestion_config = DataIngestionConfig(
            root_dir=config["root_dir"],
            source_URL=config["source_URL"],
            local_data_file=config["local_data_file"],
            unzip_dir=config["unzip_dir"]
        )

        return data_ingestion_config
