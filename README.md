# BMI Calcluator

Calculate BMI and the analyse the BMI Details of the dataset.

## Add your files

```
cd existing_repo
git branch -M master
git push -uf origin master
```

## How to build and run this repo

### How to build the microservice docker and run it

This is my proposed flow: once you are in the repo root folder, build the docker with:

```
docker build -t bmi-calc:latest .
```

Then, simply run the container with:

```
docker run -p 8000:8000 bmi-calc:latest
```

### Check the endpoints and test them

After you have built and run your docker, go to http://127.0.0.1:8000/docs to check the swagger interface and test the endpoints. For example, you can first run the `POST` endpoint to add some votes, and then check what you add via the `GET` endpoint.

## Testing

### Unit tests

You can run unit tests -- you need first to `pip install pytest` -- with the following command:

```
pytest -rA .
```
from the root folder.

