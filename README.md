# BMI Calcluator

Calculate BMI and the analyse the BMI Details of the dataset.


### How to build the the repo in docker and run it

Build the image using below command:

```
docker build -t bmi-calc:latest .
```

Then, simply run the container with:

```
docker run -p 8000:8000 bmi-calc:latest
```

### Check the endpoints and test them

After you have built and run your docker, go to http://127.0.0.1:8000/docs to check the swagger interface and test the endpoints. For example, you can first run the `POST` endpoint to calculate the bmi, and then analyse the statistics of the calculated bmis using `GET` endpoint.


## How to build and run this repo in dev environment using uvicorn:

One time setup:
```
Go to project directory and run below commands -

conda create -n bmi-venv
conda activate bmi-venv
conda install -c conda-forge uvicorn
conda install pip
pip install pytest
pip install -r requirements.txt
export PYTHONPATH=/root/../../bmi-calc <- Path to the project directory
conda deactivate
```

Run the project in dev environment -
```
cd project_dir/app
conda activate bmi-venv
uvicorn main:app --reload --port 8020
Access the Endpoints at http://127.0.0.1:8020/docs
conda deactivate
```

## Testing

### Unit tests

Run below command from the root folder to run the test cases:

```
pytest -rA .
```
