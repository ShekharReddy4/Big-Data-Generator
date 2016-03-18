# Big-Data-Generator

			Big Data Generator


This project is Test Data Generator. When you want to create more number of records to test a particular scenario in your product, 
you can use this to generate data. This can generate up to 3 million records. In order to use this, 
you need to pass one input file which contains the IDs/Names for which you want to create test data.
Suppose,  I have created a website and capturing the usage data (who has visited how many times in a day). 
On monthly basis, I want to do an aggregation. I am using third party tool to aggregate data and to get a report. 
I want to test the third party tool with more number of records and I cannot create test data manually. 
I need a code which generates data automatically. In this case, we can for this code to generate data.

My sample requirement:
I have l lakh accounts in my file and I need to generate data for those accounts.
For each account, a record should be created for the given date.
I need to populate a value (basically, an integer which indicates how many times visited)

To use this code, need to pass below information:
Input file path and name (If the input is there in the same folder where you copied my code, 
then no need to pass path, you can give simply file name)
Need to pass the date range for which date you need to generate dates.
Need to pass the integer range in which range you need to generate value.

My Input File Content:
Krishna Reddy
Shekar Reddy
Nishith Reddy

In my file 3 accounts are there and am going to generate test data for date Range 2016-03-12 to 2016-03-14 and 
my integer value should be in the range 10 to 50.

Step 1: 
Copy the below embedded code to some local folder in your computer.


I have copied to the above embedded code to the folder E:\TestDataGeneratorSample folder.
See the below screenshot.


Step 2:

Copy the input file to the path where you copied the above code. This is optional. 
If you have your input file in other folder then instead of copying to other folder, 
you can pass file name along with path. Output file is generating in the same location where you have input file. 
I am placing my input file in the same location where I copied the code. Input file can be text file (.txt file) or comma separated file(.csv).
You need have header in your input file. We are post-fixing “_TestDataGenerator” to the input file name and 
creating output file in .txt .format.

Once you are with above, Open command prompt or Git bash shell.

Go to the folder where you copied my code. I have my code in the folder E:\TestDataGeneratorSample.

Execute below commands:
javac TestDataGenerator.java
Once you executed above command, TestDataGenerator.class  will be generated in the same folder.

Now, execute the below command:
java TestDataGenerator

It will ask for input file name, Date range and Number range.
I have passed my input file and all other details. Please see the below screenshot.

Once you pass the details, it will check for existence of input file. 
If Input file is not existing then it will throw an error “Input file does not exist Please enter Correct Input File”. 
If file exists then output file will be generated.  We are appending “_TestDataGenerator” to the input file to generate output file. 
Once script execution completed, it will print output file status.





See the below screenshot of generated output:



For each account, for each date, the record has been generated. Like this, you can generate any number of records (I have tested up to 3 million records). There is more scope to enhance this application.
