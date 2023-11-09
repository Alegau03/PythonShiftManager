# Python Shift Manager

The program is summarized in the following points:

# 1. Connection to MongoDB database: The program connects to a MongoDB database through PyMongo. The MongoDB database is called "shifts_db," and it contains a collection called "users" that stores user credentials.

# 2. Creating the login window: A login window is created using Tkinter. Users can enter their user name and password.

# 3. Authentication of users: After entering the user name and password, the user clicks the "Login" button. The program verifies the credentials in the MongoDB database. If the credentials are correct, the login window is closed.

Custom "Start Shift" window: If the user has entered valid credentials, a custom "Start Shift" window opens. In this window, the user can start their shift by clicking a "Start Shift" button. The time when the shift starts is recorded, including the date, day of the week, and start time. In addition, a welcome message including the user's name is displayed.

# 4. Shift recording: When the user clicks "End Shift," the end time of the shift is recorded and the data is written to a text file with the user's name as part of the file name. The information recorded includes the date, day of the week, start time, and end time of the shift.

In summary, the code provides an application for user shift registration with a login interface, customized shift registration, and storage of shift information in text files.
