#   Abstractive Text Summarization with Pegasus from Huggingface — MLOps Pipeline

##  Overview
This project delivers an end-to-end **MLOps pipeline** for **abstractive text summarization** using the pretrained **Pegasus** transformer model. The pipeline automates data preprocessing, model training, experiment tracking, versioning, deployment, and monitoring. Thanks to Pegasus’s advanced pretraining (MLM + GSG), the model generates high-quality summaries even with small datasets.

### Workflows 

1. Config.yaml
2. Params.yaml
3. Config entity
4. Configuration Manager
5. Update the components- Data Ingestion,Data Transformation, Model Trainer
6. Create our Pipeline-- Training Pipeline,PRediction Pipeline
7. Front end-- Api's, Training APi's, Batch Prtediction API's

---

## Features

### Model
- Pegasus encoder–decoder transformer  
- Fine-tuned for abstractive summarization  
- Effective even with ~1000 training examples  
- Uses Gap Sentence Generation (GSG) + Masked Language Modeling (MLM)

### MLOps Components
- **Data Pipeline:** preprocessing, cleaning, splitting  
- **Experiment Tracking:** MLflow / Weights & Biases  
- **Dataset & Model Versioning:** DVC  
- **Training Automation:** reproducible training workflow  
- **CI/CD:** GitHub Actions for testing & deployment  
- **Containerization:** Docker for reproducible environments  
- **Deployment:** FastAPI / Flask API  
- **Monitoring:** logs + performance tracking

---

## 📂 Project Structure
project/
│── data/
│── src/
│ ├── data_preprocessing.py
│ ├── train.py
│ ├── evaluate.py
│ ├── inference.py
│── models/
│── configs/
│── notebooks/
│── api/
│── docker/
│── README.md

## Installation
```bash
git clone https://github.com/Mohamad-Gamal/Text-Summarizer-machine-learning.git
cd project
pip install -r requirements.txt

## To run the fine-tuning pipeline:
 ```
  python src/train.py --config configs/train_config.yaml

## Inference
```
  python src/inference.py --text "Your long text here..."

## Deployment
  Start the API (FastAPI example):
    ``` uvicorn api.main:app --reload

## Results
  - High-quality abstractive summaries
  - Stable performance after Pegasus fine-tuning
  - End-to-end reproducible MLOps workflow

## Future Improvements
  - Add data & model drift detection
  - Integrate cloud orchestration (Airflow / Prefect)
  - Add batch inference pipelines
