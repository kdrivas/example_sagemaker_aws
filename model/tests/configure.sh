rm -rf input
mkdir -p input/data/train
mkdir -p input/data/validation

echo "Creating data ..."
python create_data.py

rm -rf input/config && mkdir -p input/config
echo '{"max_depth": 20, "n_jobs": 4, "boosting_type": "gbdt"}' | tee input/config/hyperparameters.json
echo '{"current_host": "localhost", "hosts": ["algo-1-kipw9"]}' | tee input/config/resourceconfig.json
echo '{"train": {"TrainingInputMode": "File"}, "validation": {"TrainingInputMode": "File"}}' | tee input/config/inputdataconfig.json
