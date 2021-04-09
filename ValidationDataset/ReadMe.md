## What is Inside

There is a excel file named `validation (2).xlsx` that containes all the questins, answers and the name of the text file from where the questions and answers are made from. The `validation (2).rar` file contain the text files of different paragraph. The `validation.json` file contains the JSON file of the training dataset. There is also a `preprocess.py` file whis is used to convert your excel file into JSON file. 

**You can add more data in the excel file and run the `preprocess.py` file to get the final JSON file or you can directly use the JSON file for your project. If you add more data in excel file make sure you also make txt file for the paragraphs**

### Nota Bene

- Make sure that the language is in Bangla (including numbers) otherwise it will raise an error while converting to JSON file
- Run the `preprocess2.py` file to convert English numbers into Bangla
- After running `preprocess2.py`file, run the `preprocess.py` file to convert data into JSON file
- Keep all the txt files and the excel file in one single folder
