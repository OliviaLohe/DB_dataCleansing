-- Turn on foreign keys
PRAGMA foreign_keys = ON;

-- Delete the tables if they already exist
drop table if exists Student;
drop table if exists Course;
drop table if exists Enroll;
drop table if exists Dept;

-- Create the schema for your tables below
CREATE TABLE "Student" (
	"studentID"	INTEGER NOT NULL,
	"studentName"	TEXT NOT NULL,
	"class"	TEXT CHECK(class=="Freshman" or class=="Sophomore" or class=="Junior" or class=="Senior"),
	"gpa"	REAL CHECK(gpa>=0.0 AND gpa<=4.0),
	PRIMARY KEY("studentID")
);

CREATE TABLE "Major" (
	"studentID"	INTEGER NOT NULL,
	"major"	TEXT,
	PRIMARY KEY("studentID","major"),
	FOREIGN KEY("major") REFERENCES "Dept"("deptID"),
	FOREIGN KEY("studentID") REFERENCES "Student"("studentID")
);

CREATE TABLE "Course" (
"CourseNum" INTEGER,
"deptID" TEXT,
"CourseName" TEXT,
"location" TEXT,
"meetDay" TEXT,
"meetTime" TEXT CHECK(meetTime >= '07:00' AND meetTime <= '17:00'),
PRIMARY KEY("courseNum", "deptID"),
FOREIGN KEY("deptID") REFERENCES "Dept"("deptID")
);

CREATE TABLE "Dept" (
	"deptID"	TEXT CHECK(length(deptID<5)),
	"name"	TEXT NOT NULL UNIQUE,
	"building"	TEXT,
	PRIMARY KEY("deptID")
);

CREATE TABLE "Enroll"(
"CourseNum" INTEGER,
"deptID" TEXT,
"studentID" INTEGER,
PRIMARY KEY("CourseNum", "deptID", "studentID"),
FOREIGN KEY("CourseNum") REFERENCES "Course"("CourseNum"),
FOREIGN KEY("deptID") REFERENCES "Dept"("deptID"),
FOREIGN KEY("studentID") REFERENCES "Student"("studentID") 
);