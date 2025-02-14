import os
from textsummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from textsummarizer.entity.config import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
    
    def convert_examples_to_features(self, example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'], max_length=1024, truncation=True)
        
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length=128, truncation=True)
            
        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    
    def convert(self):
        logger.info("Starting dataset loading from: %s", self.config.data_path)
        try:
            dataset_samsum = load_from_disk(self.config.data_path)
            logger.info("Dataset loaded successfully. Converting examples...")
        except Exception as e:
            logger.exception("Failed to load dataset from disk.")
            raise e

        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched=True)
        logger.info("Mapping complete. Saving transformed dataset...")
        
        output_path = os.path.join(self.config.root_dir, "samsum_dataset")
        dataset_samsum_pt.save_to_disk(output_path)
        logger.info("Transformed dataset saved at: %s", output_path)
