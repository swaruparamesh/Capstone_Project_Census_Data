Assignment_1:Census Data Standardization and Analysis Pipeline

## Task List

1. **Task 1 - Install Required Libraries and Load Census Data**:
   - Add the following pip install commands to your README or a requirements.txt file:
     ```
     pip install pandas
     pip install openpyxl
     ```
   - In your `project_census_data.py` file, import pandas and load the census data from '/content/sample_data/census_2011.xlsx' into a DataFrame.
   - Rename the desired columns as required.

2. **Task 2 - Standardize State/UT Names**:
   - Write a function to standardize the state/UT names as described.
   - Apply this function to the DataFrame to update the names accordingly.

3. **Task 3 - Rename State/UT Names for Specific Districts**:
   - Read the data from 'Data/Telangana.txt' and update the state/UT names as specified.
   - You may need to write a function to handle this renaming process.

4. **Task 4 - Find Missing Data Percentage**:
   - Write a function to calculate the percentage of missing data for each column.
   - Display or store the results as needed.

5. **Task 5 - Save Data to MongoDB**:
   - Import pymongo in your `project_census_data.py` file.
   - Establish a connection to your MongoDB database and save the DataFrame to MongoDB.

6. **Task 6 - Database Connection and Data Upload to PostgreSQL**:
   - Install psycopg2-binary and psycopg2 as specified in your README or requirements.txt.
   - Establish a connection to your PostgreSQL database.
   - Upload the data from your DataFrame to the PostgreSQL database.

7. **Task 7 - Run Query on the Database and Display Output with Streamlit**:
   - Install Streamlit and include it in your README or requirements.txt.
   - Write a Streamlit app that connects to your database and runs the desired query.
   - Display the query results using Streamlit components.

