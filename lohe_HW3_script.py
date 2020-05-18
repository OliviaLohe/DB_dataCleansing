import pandas as pd


shmeeplesoft = pd.read_csv('../shmeeplesoft.raw.txt', header=[0], skiprows=[1])

shmeeplesoft.loc[shmeeplesoft['deptID']=='ENG', 'deptID']='ENGL'
shmeeplesoft.loc[shmeeplesoft['major']=='ENG', 'major']='ENGL'
shmeeplesoft.loc[shmeeplesoft['class']=='JR', 'class']='Junior'
shmeeplesoft.loc[shmeeplesoft['class']=='SR', 'class']='Senior'

tmp = shmeeplesoft.copy()
dataToSplit = tmp.drop('major', axis=1) \
        .join(tmp['major'] \
        .str \
        .split(';', expand=True) \
        .stack() \
        .reset_index(level=1, drop=True).rename('major')) \
        .reset_index(drop=True)
dataToSplit = dataToSplit.fillna(0)
dataToSplit = dataToSplit.astype({'studentID': int, 'CourseNum': int})        
  

studentInfo = dataToSplit.filter(items=['studentID', 'studentName', 'class', 'gpa'])
studentInfo = studentInfo[studentInfo.studentID != 0]
studentInfo = studentInfo[studentInfo.studentName != 0]

deptInfo = dataToSplit.filter(items=['deptID', 'deptName', 'building'])
deptInfo = deptInfo[deptInfo.deptID != 0]
deptInfo = deptInfo[deptInfo.deptName != 0]
deptInfo = deptInfo[deptInfo.building != 0]

courseInfo = dataToSplit.filter(items=['CourseNum', 'deptID', 'CourseName', 'Location', 'meetDay', 'meetTime'])
courseInfo = courseInfo[courseInfo.CourseNum != 0]
courseInfo = courseInfo[courseInfo.deptID != 0]
courseInfo = courseInfo[courseInfo.CourseName != 0]
courseInfo = courseInfo[courseInfo.Location != 0]
courseInfo = courseInfo[courseInfo.meetDay != 0]
courseInfo = courseInfo[courseInfo.meetTime != 0]

enrollInfo = dataToSplit.filter(items=['CourseNum', 'deptID', 'studentID'])
enrollInfo = enrollInfo[enrollInfo.CourseNum != 0]
enrollInfo = enrollInfo[enrollInfo.deptID != 0]
enrollInfo = enrollInfo[enrollInfo.studentID != 0]

majorInfo = dataToSplit.filter(items=['studentID', 'major'])
majorInfo = majorInfo[majorInfo.studentID != 0]
majorInfo = majorInfo[majorInfo.major != 0]

stuIndex = 0
for row in studentInfo.iterrows():
	print('INSERT INTO Student VALUES (' + str(studentInfo.iloc[stuIndex, int(0)]) + ', \'' + str(studentInfo.iloc[stuIndex, 1])
	+ '\', \'' + str(studentInfo.iloc[stuIndex, 2]) + '\', \'' + str(studentInfo.iloc[stuIndex, 3]) + '\');')
	stuIndex=stuIndex+1

deptIndex = 0
for row in deptInfo.iterrows():
	print('INSERT INTO Dept VALUES ( \'' + str(deptInfo.iloc[deptIndex, int(0)]) + '\', \'' + str(deptInfo.iloc[deptIndex, 1])
	+ '\', \'' + str(deptInfo.iloc[deptIndex, 2]) + '\');')
	deptIndex=deptIndex+1

courseIndex = 0
for row in courseInfo.iterrows():
	print('INSERT INTO Course VALUES (' + str(courseInfo.iloc[courseIndex, int(0)]) + ', \'' + str(courseInfo.iloc[courseIndex, 1])
	+ '\', \'' + str(courseInfo.iloc[courseIndex, 2]) + '\', \'' + str(courseInfo.iloc[courseIndex, 3])
	+ '\', \'' + str(courseInfo.iloc[courseIndex, 4]) + '\', \'' + str(courseInfo.iloc[courseIndex, 5]) + '\');')
	courseIndex=courseIndex+1

enrIndex = 0
for row in enrollInfo.iterrows():
	print('INSERT INTO Enroll VALUES (' + str(enrollInfo.iloc[enrIndex, 0]) + ', \'' + str(enrollInfo.iloc[enrIndex, 1])
	+ '\', ' + str(enrollInfo.iloc[enrIndex, 2]) + ');')
	enrIndex=enrIndex+1

majIndex = 0
for row in majorInfo.iterrows():
	print('INSERT INTO Major VALUES (' + str(majorInfo.iloc[majIndex, 0]) + ', \'' + str(majorInfo.iloc[majIndex, 1]) + '\');')
	majIndex=majIndex+1