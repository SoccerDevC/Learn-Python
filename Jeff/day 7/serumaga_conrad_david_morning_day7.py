#DAY7: Python for DataScience

"""_summary
1.Numpy, Numerical Python, helps- you work with arrays efficiently
2.Pandas - Functionalities, data cleaning, transformation, merging, filtering

Data Visualization
Plotting - use  library  called matplotlib or seabon - create - line, scatter, bar, histogram
heatmaps

key concepts in Data Science:
1. Data - (text, images, videos) or semi structured data (JSON, XML)
2. Data Mining 
3. Machine Learning
4. Statistical Analysis
5. Data Visualization
6. Big Data
7. Predictive Analysis

"""
"""
#Understanding data- Science workflow
1. Problem definition
2. Data Acquisition data.gov, kaggle
3. 
Data Preparation and preprocessing
-Missing Data
Wrong Format
Null Values
Wrong format
Duplicates"""


# Remaining concepts in advanced Python Topics
#Context Manager
#Multithreading and multiprocessing 

#Context Manager - is an object that defines a temporary context for a block of code

#Example 1: Demonstrste a context manager to open a file and return a context manager instance

# def open_file(filename):
#     """This will open a file and return a context manager instance"""
#     file = open(filename, 'r')
    
#     def __enter__(): 
#         return file
    
#     def __exit__(self, exc_type, exc_value, exec_tb):
#         file.close()
        
#         return __enter__.__exit__
    
# with open_file("my_file.txt") as f:
#     contents = f.read()

#Example 2: Demonstrate a context manager using a time series
# import time

# class Timer:
#     def __enter__(self):
#         self.start_time = time.time()
    
#     def __exit__(self, exc_type, exc_value, traceback):
#         end_time =time.time()
#         execution_time = end_time - self.start_time
#         print(f"The time for this execution {execution_time} seconds elapsed")
        
# #with Example usage
# with Timer() as t:
#     """measure the execution time"""
#     time.sleep(2)
        
        
# #MultiThreading and Multiprocessing
# """Techniques that can be used to improve the performance of a python program"""

# #Multithreading is a technique where multiple threads are created within a single process.
# #Multiprocessing is a technique where multiple threads are created

# #Example of multithreading 
# import threading
# def task(name):
#     print(f"Running task {name}")
    
# #Create multiple threads
# threads = []
# for i in range(5):
#     t = threading.Thread(target = task, args = (f"Thread {i}",))
#     threads.append(t)
#     t.start()
    
# #Wait for all threads to finish before it joins

# for t in threads:
#     t.join()
    

#Example: Demonstrate multi Processing
# import multiprocessing

# def process_task(name):
#     print(f"Processing task {name}")
    
# #Create a pool of processes
# pool = multiprocessing.Pool(processes=6)

# #submit multiple tasks to the pool
# for i in range(6):
#     pool.apply_async(process_task, args=(f"Process {i}",))
    
# #Close the pool and wait for all the processes to finish
# pool.close()
# pool.join()
# 
# #Example 5: Demonstrate use of multithreading and multiprocessing

# import threading
# import multiprocessing

# def task(name):
#     print(f"Running task {name} on thread {threading.current_thread().name} with process {multiprocessing.current_process().name}")

# #create miltiple threads 
# threads = []
# for i in range(4):
#     t = threading.Thread(target=task, args = (f"Thread {i}",))
#     threads.append(t)
#     t.start()

# #wait for all threads to finish 
# for t in threads:
#     t.join()
    
    
#Excercise
#Show a context manager for file handling that automatically opens and closes a file
# class FileContextManager:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#         self.file = None
    
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
    
#     def __exit__(self, exc_type, exc_value, traceback):
#         if self.file:
#             self.file.close()
# with FileContextManager('file.txt', 'r') as f:
#     # Perform file operations
#     data = f.read()
#     print(data)

#Show a context manager for managing a database connection
# import psycopg2

# class DatabaseContextManager:
#     def __init__(self, dbname, user, password, host, port):
#         self.dbname = dbname
#         self.user = user
#         self.password = password
#         self.host = host
#         self.port = port
#         self.conn = None
    
#     def __enter__(self):
#         self.conn = psycopg2.connect(
#             dbname=self.dbname,
#             user=self.user,
#             password=self.password,
#             host=self.host,
#             port=self.port
#         )
#         return self.conn
    
#     def __exit__(self, exc_type, exc_value, traceback):
#         if self.conn:
#             self.conn.close()
# with DatabaseContextManager('mydb', 'myuser', 'mypassword', 'localhost', '5432') as conn:
#     # Perform database operations
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM mytable")
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)

#Show a multi threading and multiprocessing that allows us to run the function for different amounts of time
# import threading
# from multiprocessing import Pool

# def my_function(duration):
    
#     print(f"Running for {duration} seconds")
#     time.sleep(duration)
#     print(f"Completed after {duration} seconds")

# # Multi-threading
# thread1 = threading.Thread(target=my_function, args=(3,))
# thread2 = threading.Thread(target=my_function, args=(5,))
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()

# # Multiprocessing
# pool = Pool()
# pool.map(my_function, [3, 5])
# pool.close()
# pool.join()
