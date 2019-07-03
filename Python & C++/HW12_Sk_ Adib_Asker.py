#Sk adib asker
#Cs100, Section-103
#12/05/2017


class Course_Section:
    ''' this is class represent course section '''
    university = 'NJIT' #5
    #1
    def __init__ (self, section_number, course_name):
        ''' this is class '''
        self.section = section_number
        self.name = course_name
        self.enrolled_students = [] #2
    #3    
    def enroll(self, names, ucid):
        ''' this method enrolls student in the course section '''
        if (names , ucid) not in self.enrolled_students:
            self.enrolled_students.append((names, ucid))
            print(names, 'with ucid', str(ucid), 'has successfully enrolled in section 1 of CS100')
        else:
            print('Already Enrolled.')

    #4     
    def drop(self,names, ucid):
        ''' this method drop students '''
        for word in self.enrolled_students:
            if (names , ucid) in self.enrolled_students:
                self.enrolled_students.remove((word))
                print(names, 'with ucid', str(ucid), 'has successfully drop frome section 1 of CS100!!')
            elif (names , ucid) not in self.enrolled_students:
                print(names, 'with ucid', str(ucid), 'does not exist in section 1 of CS100')
#part2        
class Student:
    ''' this is class represent students name, id, gpa '''
    #1
    letterGradeCode = {'A':4, 'B+':3.5, 'B':3, 'C+':2.5, 'C':2,'D':1,'F':0}#5
    def __init__(self, name, ucid):
        self.name = name
        self.ucid = ucid
        self.transcript = {} #2
    #3
    def grade_obtained(self, c_name, l_grade):
        '''this method add grade'''
        self.transcript[c_name]= l_grade
        print(self.name, 'your grade', l_grade, 'for', c_name, 'has been successfully recorded!')
    #4
    def viewGrade(self, courseName):
        '''this method will check whether you have taken this course'''
        
        if courseName in self.transcript:
            print(self.name, 'your grade for', courseName, 'is', self.transcript[courseName])
            return self.transcript[courseName]
        
        else:
            print(self.name, 'you did not take', courseName)
            return None
    #6
    def calculateGPA(self):
        '''this method will calculate the GPA'''
        GPA = 0
        for grade in self.transcript:
            GPA += self.letterGradeCode[self.transcript[grade]]

        GPA = GPA/len(self.transcript)
        return GPA
        
        
