from textsummarizer.config.configuration import ConfigurationManager 
from textsummarizer.components.data_validation import DataValidation
from textsummarizer.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            logger.info("DataValidationTrainingPipeline: Starting configuration retrieval...")
            config_manager = ConfigurationManager()
            data_validation_config = config_manager.get_data_validation_config()
            logger.info(f"DataValidationTrainingPipeline: Retrieved config: {data_validation_config}")
        except Exception as e:
            logger.exception("Error retrieving data validation config")
            raise e
        
        try:
            logger.info("DataValidationTrainingPipeline: Instantiating DataValidation object...")
            data_validation = DataValidation(config=data_validation_config)
        except Exception as e:
            logger.exception("Error instantiating DataValidation object")
            raise e

        try:
            logger.info("DataValidationTrainingPipeline: Validating existence of required files...")
            validation_status = data_validation.validate_all_files_exist()
            if validation_status:
                logger.info("DataValidationTrainingPipeline: Validation passed. All required files exist.")
            else:
                logger.error("DataValidationTrainingPipeline: Validation failed. Required files missing.")
        except Exception as e:
            logger.exception("Error during file validation")
            raise e

        logger.info("DataValidationTrainingPipeline: Completed all steps.")
