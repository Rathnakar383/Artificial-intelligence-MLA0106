% --- Facts ---
% student(Name, Teacher, Subject, Code)
student('Alice', 'Mr. Smith', 'Mathematics', 'M101').
student('Bob', 'Mrs. Johnson', 'Physics', 'P102').
student('Charlie', 'Mr. Smith', 'Mathematics', 'M101').
student('David', 'Mrs. Johnson', 'Physics', 'P102').
student('Eve', 'Mr. Brown', 'Chemistry', 'C103').

% --- Rules ---
% Get all students taught by a specific teacher
students_by_teacher(Teacher) :-
    student(Name, Teacher, Subject, Code),
    format('~w teaches ~w (~w - ~w)~n', [Teacher, Name, Subject, Code]),
    fail.
students_by_teacher(_).

% Get all subjects and codes for a specific student
subjects_by_student(Student) :-
    student(Student, Teacher, Subject, Code),
    format('~w studies ~w (~w) with ~w~n', [Student, Subject, Code, Teacher]),
    fail.
subjects_by_student(_).

% Find teacher by subject code
teacher_by_code(Code) :-
    student(Name, Teacher, Subject, Code),
    format('Code: ~w -> ~w teaches ~w to ~w~n', [Code, Teacher, Subject, Name]),
    fail.
teacher_by_code(_).
