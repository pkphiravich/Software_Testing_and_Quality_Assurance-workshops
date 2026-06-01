import xml.etree.ElementTree as ET
import os


#read result.txt to get test case statuses
#output example: ["passed","passed","failed"]
def get_test_statuses():
	test_statuses = []
	with open('result.txt','r') as file:
		for line in file:
			status = line.strip()
			test_statuses.append(status)
	return test_statuses

#find all coverage files in the current directory
#output example: ["coverage1.xml","coverage2.xml"]
def get_all_coverage_filenames(rootdir="."):
	filenames = []
	for filename in os.listdir(rootdir):
		if filename.endswith(".xml"):
			file_path = os.path.join(rootdir,filename)
			filenames.append(file_path)
	return sorted(filenames)


def tarantula():
	test_statuses = get_test_statuses() # ได้ลิสต์ของ passed, failed
	coverage_filenames = get_all_coverage_filenames() # ได้ชื่อไฟล์
	#=====complete the code below======#

	#Read each XML file, go through each line of code, find out which lines get executed and which do not.
	#Which data structure should be used for this?
	t = []
	for cr in coverage_filenames:
		xmlcr = ET.parse(cr)
		xmlcrroot = xmlcr.getroot()
		packages = xmlcrroot.find("packages")
		package = packages.find("package")
		classes = package.find("classes")
		class_ = classes.find("class")
		class_ = class_.find("lines")
		all_line = class_.findall("line")
		t.append([l.get("hits") for l in all_line])

	# แปลง string เป็น int
	for i in range(len(t)):
		t[i] = list(map(int, t[i]))

	total_failed = test_statuses.count("failed") # 1
	total_passed = test_statuses.count("passed") # 5

	suspiciousness = []

	number_of_lines = len(t[0])        
	number_of_tests = len(t)           

	
	for line_index in range(number_of_lines):

		failed = 0   # executed & failed
		passed = 0   # executed & passed

		# วนทีละ test
		for test_index in range(number_of_tests):

			hit = t[test_index][line_index]
			status = test_statuses[test_index]

			if hit > 0:
				if status == "failed":
					failed += 1
				elif status == "passed":
					passed += 1

		# คำนวณ tarantula formula
		if total_failed == 0:
			score = 0
		else:
			f = failed / total_failed

			if total_passed == 0:
				p = 0
			else:
				p = passed / total_passed

			u = f + p

			if u == 0:
				score = 0
			else:
				score = f / u

		suspiciousness.append((line_index + 1, score))

	# เรียงจากมากไปน้อย
	suspiciousness.sort(key=lambda x: x[1], reverse=True)

	print("Top 5 suspicious lines:")
	for line, score in suspiciousness[:5]:
		print("Line", line, ":", score)


	#====== end of your code =====

if __name__ == "__main__":
    tarantula()
