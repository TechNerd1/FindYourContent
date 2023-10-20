# Setup
1. Navigate to the Project Directory:
   ```
   cd findyourcontent
    ```
3. Set Up the Virtual Environment:
   - Create a virtual environment for the project. This helps to ensure that the project's dependencies remain isolated.
     ```
     python -m venv myvenv
      ```
4. Activate the Virtual Environment:
   - Windows:
      ```
      .\myvenv\Scripts\activate
       ```
   - On MacOS/Linux:
       ```
       source myvenv/bin/activate
        ```
4. Install Dependencies:
   - With the virtual environment activated, install the required packages listed in requirements.txt.
     ```
     pip install -r requirements.txt
      ```
5. Unzip ```transcripts_fts.zip```
6. Run the Project:
    ```
    streamlit run .\src\Search.py
    ```
