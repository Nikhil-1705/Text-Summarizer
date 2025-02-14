import sys
print("Current working directory:", sys.path[0])
print("sys.path:", sys.path)

from textsummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textsummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textsummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(">>>>> stage Data Ingestion stage started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(">>>>> stage Data Ingestion stage completed <<<<<\n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e

print("Ingestion stage done. Now starting Data Validation stage.")
logger.info("Ingestion stage done. Now starting Data Validation stage.")

STAGE_NAME = "Data Validation stage"
try:
    logger.info(">>>>> stage Data Validation stage started <<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(">>>>> stage Data Validation stage completed <<<<<\n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e