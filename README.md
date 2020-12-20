# Kmart - SWE Challenge
This is my solution to the Kmart Software Engineer Coding Challenge (https://github.com/ksaifullah/coding-challenge).
This solution uses: Python3, Docker and CircleCI.


## Installation - Local Machine

1. Fork my repository.
2. Ensure that you have Python3 setup (with [pip](https://pip.pypa.io/en/stable/) on your Path).
3. Run the following command in the project's root directory:

```bash
pip install -r requirements.txt 
```

## Installation - Docker

1. Fork my repository.
2. Ensure that you have Docker [engine](https://docs.docker.com/get-docker/) and Docker [compose](https://docs.docker.com/compose/install/) installed.
3. Run the following commands in the project's root directory:

```bash
docker-compose build
docker-compose up
```

4. Now, in a second terminal, run the following command:
```bash
docker ps   # Use this to find your container id
docker exec -it <INSERT_CONTAINER_ID>  /bin/bash
```
You should now be inside the Docker container, allowing you to run the code without having to modify your local machine environment.

## Usage
From the project root directory, run the following command to open the help menu:

```bash
python .\kmartRunner.py -h
```
To run on an input, the following can be done (where the sample array is [10, 5, 6, -5]

```bash
python .\kmartRunner.py --a 10 5 6 -5
```

This returns:
```bash
 [5, 6]
```
To see a more details, you can add -t to the input
```bash
python .\kmartRunner.py --a 10 5 6 -5 -t
```
This will result in the following output:
```bash
Input: [10, 5, 6, -5]
Output: [5, 6]
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
