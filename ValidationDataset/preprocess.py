import argparse
import pandas as pd
import os
import hashlib
import json 


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

	outputfile ="validation.json"
	if args['output'] is not None:
		outputfile=args['output']



	datapath = "data2" #data directoty name/path	
	excelFile = "validation (2).xlsx"
	excelfilepath = os.path.join(datapath, excelFile)

	if args['excel'] is not None:
		excelfilepath = args['excel']

	if excelfilepath is not None:
		entire_dict = {}
		entire_dict['version'] = "1.0"
			
		
		df = pd.read_excel (excelfilepath)
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
					dataentry_dict['additional_answers'] = additional_answer
					dataentry_dict['name']=pf
					data_dict.append(dataentry_dict)
					additional_answer['0'] = x
					additional_answer['1'] = y
					additional_answer['2'] = z
				
				#Reset variables
				dataentry_dict = {}
				additional_answer = {}
				dataentry_dict['source'] ="manual"

				pf = row[2]

				print(pf)
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
				additional = []
				x = []
				y = []
				z = []
				#print(pf)
				turn_id = 0
			turn_id = turn_id+1
			qinput_text = row[0]
			ainput_text = row[1]
			span_text = row[3]
			xspan_text = row[4]
			yspan_text = row[5]
			zspan_text = row[6]
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

			x_dict = {}
			span_start,span_end = substringFinder(str(xspan_text),story)
			x_dict['span_start']=span_start
			x_dict['span_end']=span_end
			x_dict['span_text']=xspan_text
			x_dict['input_text']=str(ainput_text)
			x_dict['turn_id']=turn_id

			y_dict = {}
			span_start,span_end = substringFinder(str(yspan_text),story)
			y_dict['span_start']=span_start
			y_dict['span_end']=span_end
			y_dict['span_text']=yspan_text
			y_dict['input_text']=str(ainput_text)
			y_dict['turn_id']=turn_id

			z_dict = {}
			span_start,span_end = substringFinder(str(zspan_text),story)
			z_dict['span_start']=span_start
			z_dict['span_end']=span_end
			z_dict['span_text']=zspan_text
			z_dict['input_text']=str(ainput_text)
			z_dict['turn_id']=turn_id


			questions.append(question_dict)
			answers.append(answer_dict)
			x.append(x_dict)
			y.append(y_dict)
			z.append(z_dict)
			additional_answer['0'] = x
			additional_answer['1'] = y
			additional_answer['2'] = z
			#print(z_dict)
		#additional.append(additional_answer)
		dataentry_dict['questions'] = questions
		dataentry_dict['answers'] = answers
		print(additional_answer)
		dataentry_dict['additional_answers'] = additional_answer
		dataentry_dict['name']=pf
		data_dict.append(dataentry_dict)
		
		entire_dict["data"] = data_dict
		with open(outputfile, 'w', encoding='utf-8') as f:
			json.dump(entire_dict, f, ensure_ascii=False, indent=4)







