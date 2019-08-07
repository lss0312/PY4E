# many to many relationship
# a table should have an attribute that is unique, say user_id or article_id
# if a user can read many articles and an article can be read by many users, we have to build another table to combine this kind of many-to-many relationship
CREATE TABLE Users (
	id INTERGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name TEXT,
	email TEXT
	) ;

CREATE TABLE Course (
	id INTERGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	title TEXT,
	) 

CREATE TABLE Member (
	user_id INTERGER,
	course_id INTERGER,
	role  INTERGER,
	PRIMARY KEY (user_id, course_id)#means this pair should be unique
	)

SELECT User.name, Member.role, Course.title
FROM Users JOIN Member JOIN Course
ON Member.user_id = User.id AND Member.course.id=Course.id
ORDER BY Course.title, Member.role DESC, User.name
# combine this two table occording the 