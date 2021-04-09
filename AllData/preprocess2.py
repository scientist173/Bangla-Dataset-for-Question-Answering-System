import argparse
import pandas as pd
import os
import hashlib
import json
import bangla



def substringFinder(substring,text):
	start_indx = text.find(substring)
	if start_indx == -1:
		return -1,-1
	return start_indx, len(substring)+start_indx-1




if __name__ == '__main__':
	ap = argparse.ArgumentParser()
	ap.add_argument("-t", "--text", required=False, help="entire text")
	ap.add_argument("-s", "--substr", required=False, help="substring to find")
	ap.add_argument("-e", "--excel", required=False, help="excel file")
	ap.add_argument("-o", "--output", required=False, help="output file")
	

	

	args = vars(ap.parse_args())
	if args['text'] is not None:
		print(args['text'])
	if args['substr'] is not None:
		print(args['substr'])
	if args['text'] is not None and args['substr'] is not None: 
		ret0,ret1 = substringFinder(args['substr'],args['text'])
		print(ret0)

	outputfile ="alldata.json"
	if args['output'] is not None:
		outputfile=args['output']



	datapath = "path of your excel and txt file folder" #data directoty name/path	
	excelFile = "alldata.xlsx"
	excelfilepath = os.path.join(datapath, excelFile)

	if args['excel'] is not None:
		excelfilepath = args['excel']

	if excelfilepath is not None:
		entire_dict = {}
		entire_dict['version'] = "1.0"
			
		
		df = pd.read_excel (excelfilepath,  dtype=str)
		pf="start"
		
		data_dict = []
		for index, row in df.iterrows():
			#print(row[2])
			if pf != row[2]:
				#Write to json entry
				if pf != "start":
					#dataentry_dict_old = dataentry_dict
					dataentry_dict['questions'] = questions
					dataentry_dict['answers'] = answers
					dataentry_dict['name']=pf
					data_dict.append(dataentry_dict)
				
				#Reset variables
				dataentry_dict = {}
				dataentry_dict['source'] ="manual"


				pf = row[2]
				
				

				#print(pf)
				textfile = open(os.path.join(datapath, pf),mode='r',encoding='utf-8')
				story = textfile.read()

				#print(story)
				textfile.close()
				id = str(hashlib.md5(story.encode()).hexdigest())
				dataentry_dict['id']=id
				dataentry_dict['filename']=pf
				dataentry_dict['story'] = story
				questions = []
				answers = []

				#print(id)
				turn_id = 0
			turn_id = turn_id+1
			qinput_text = row[0]
			ainput_text = str(row[1])
			if ainput_text.replace('.','',1).isdigit():
				print(ainput_text)
				ainput_text = bangla.convert_english_digit_to_bangla_digit(ainput_text)
				print(ainput_text)
			#bangla_numeric_string = bangla.convert_english_digit_to_bangla_digit("123456")
			span_text = row[3]
			span_start,span_end = substringFinder(str(span_text),story)
			#print(span_start)
			#print(span_end)
			question_dict = {}

			question_dict['input_text']=qinput_text
			question_dict['turn_id']=turn_id

			answer_dict = {}



			answer_dict['span_start']=span_start
			answer_dict['span_end']=span_end
			answer_dict['span_text']=span_text
			answer_dict['input_text']=str(ainput_text)
			answer_dict['turn_id']=turn_id

			questions.append(question_dict)
			answers.append(answer_dict)

		dataentry_dict['questions'] = questions
		dataentry_dict['answers'] = answers
		dataentry_dict['name']=pf
		data_dict.append(dataentry_dict)

		entire_dict["data"] = data_dict
		with open(outputfile, 'w', encoding='utf-8') as f:
			json.dump(entire_dict, f, ensure_ascii=False, indent=4)







