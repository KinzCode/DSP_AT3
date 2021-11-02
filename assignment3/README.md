# Description
A Streamlit powered application designed to simplify the EDA process. The application allows the user to upload a CSV file of choice (up to 200MB) and provides the following insights:
1) General Information
2) Numeric Column Information
3) Text Column Information
4) Datetime Column Information

# Authors
Ben McKinnon, Navid Mehnati, Shangqing Yang, Yaqing Zhang

# Structure
.
├── app <-Folder containing streamlit_app.py
	├── streamlit_app.py <- The script containing the GUI and run logic for the application
├── src <- The Folder containing scripts that contain classes used within the streamlit application and the test folder containing unit-tests.
	├── __init__.py <- The script hosting which .py files are included in the src module
	├── data.py <- The script containing the Dataset class.
	├── datetime.py <- The script containing the DateColumn class.
	├── numeric.py <- The script containing the NumericColumn class.
	├── text.py <- The script containing the TextColumn class.
	├──  test <- The folder containing unit tests for the respective .py scripts containing classes used within the streamlit_app.py file.
		├── test_data.py <- The script containing unit tests for data.py
		├── test_datetime.py <- The script containing unit tests for datetime.py
		├── test_numeric.py <- The script containing unit tests for numeric.py
		├── test_text.py <- The script containing unit tests for test.py
├── docker-compose.yml                     
├── DockerFile <- The file containing the docker logic to set up the container.                        
├── requirements.txt <- The package version requirements used within the DockerFile setup.
└── README.md <- The file providing an overview of the repository and codebase.

# Instructions
The following is instructions on how to run the streamlit application provided in this repository:
1) Clone or fork this repository to your local computer.
2) Using your shell, i.e. GitBash, CD to within the "Assignment3" folder.
3) Once in the folder, run the command:  “docker build -t streamlit_at3:final .” (Note, if Docker is not installed on your device it will need to be before you can continue with setup. Docker can be downloaded from https://docs.docker.com/get-docker/)
4) Once complete run the next command: “docker run -dit --rm --name app -p 8501:8501 -v "${PWD}"  streamlit_at3:final”
5) Finally, copy and paste http://localhost:8501/ into your browser.