from src.textsummarizer.logging import logger
from src.textsummarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline




stage_name = "Data Ingestion Stage"

try:
    logger.info(f"stage {stage_name} initiated")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"stage {stage_name} completed")
except Exception as e:
    logger.exception(e)
    raise e

