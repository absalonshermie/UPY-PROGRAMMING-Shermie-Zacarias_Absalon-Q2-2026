# Required Structures
users = {
    'jperez': {'password': '1234', 'rol': 'student', 'name': 'Juan Pérez'},
    'dromo': {'password': '1234', 'rol': 'student', 'name': 'Daniela Romo'},
    'mjuarez': {'password': '1234', 'rol': 'student', 'name': 'Mauricio Juárez'},
    'mlopez': {'password': '1234', 'rol': 'student', 'name': 'María López'},
    'euc': {'password': '1234', 'rol': 'student', 'name': 'Ernesto Uc'},
    'cbalam': {'password': '1234', 'rol': 'student', 'name': 'Carlos Balam'},
    'jpedrozo': {'password': '1234', 'rol': 'professor', 'name': 'Jorge Pedrozo'},
    'dgamboa': {'password': '1234', 'rol': 'coordinator', 'name': 'Didier Gamboa'}
}

subjects = (
    "Discrete Mathematics", "Programming", "English II", "Differential Calculus",
    "Probability and Statistics", "Computer and Server Architecture",
    "Socio-Emotional Skills and Conflict Management"
)

notes = {
    'jperez': {'Discrete Mathematics': 8.5, 'Programming': 9.2, 'English II': 9.0, 'Differential Calculus': 7.8, 'Probability and Statistics': 8.3, 'Computer and Server Architecture': 6.8, 'Socio-Emotional Skills and Conflict Management': 9.5},
    'dromo': {'Discrete Mathematics': 9.0, 'Programming': 6.7, 'English II': 9.4, 'Differential Calculus': 6.2, 'Probability and Statistics': 9.1, 'Computer and Server Architecture': 6.5, 'Socio-Emotional Skills and Conflict Management': 9.8},
    'mjuarez': {'Discrete Mathematics': 7.5, 'Programming': 8.0, 'English II': 8.5, 'Differential Calculus': 7.0, 'Probability and Statistics': 7.8, 'Computer and Server Architecture': 6.2, 'Socio-Emotional Skills and Conflict Management': 8.9},
    'mlopez': {'Discrete Mathematics': 9.5, 'Programming': 9.8, 'English II': 9.2, 'Differential Calculus': 9.0, 'Probability and Statistics': 9.6, 'Computer and Server Architecture': 9.4, 'Socio-Emotional Skills and Conflict Management': 10.0},
    'euc': {'Discrete Mathematics': 8.2, 'Programming': 6.9, 'English II': 8.8, 'Differential Calculus': 6.0, 'Probability and Statistics': 6.4, 'Computer and Server Architecture': 8.1, 'Socio-Emotional Skills and Conflict Management': 9.0},
    'cbalam': {'Discrete Mathematics': 8.8, 'Programming': 9.0, 'English II': 8.5, 'Differential Calculus': 6.6, 'Probability and Statistics': 8.9, 'Computer and Server Architecture': 8.7, 'Socio-Emotional Skills and Conflict Management': 9.2}
}

class CalificacionInvalidaError(Exception): pass

logged_in = False
username = ""
role = ""

try:
    username = input("User: ")
    password = input("Password: ")
    
    if username not in users or users[username]['password'] != password:
        print("Wrong user/password!")
    else:
        logged_in = True  
        user_info = users[username]
        role = user_info['rol']
        name = user_info['name']
        print(f"Bienvenid@!, {name} ({role})")

        if role == 'student':
            print("=========================================")
            print("  School Report")
            print("=========================================")
            approved = set()
            pending = set()
            for subj in subjects:
                grade = float(notes[username][subj])
                if grade >= 7.0:
                    print(f"{subj[:26]:<27}: {grade}")
                    approved.add(subj)
                else:
                    pending.add(subj)
            print(f"\nApproved: {approved}")
            print(f"Pending : {pending}")

        elif role == 'professor':
            print("=========================================")
            print("  Students")
            print("=========================================")
            student_list = []
            for u, info in users.items():
                if info['rol'] == 'student':
                    print(f"User: {u:<10} | Student: {info['name']}")
                    student_list.append(u)
                    
            print("\nWrite other thing to exit\n")
            target = input("Student to grade (username): ")
            
            # Si el usuario teclea "stop", no entra al ciclo y finaliza correctamente.
            while target in student_list:
                print("=========================================")
                print("  Subjects")
                print("=========================================")
                for subj in subjects:
                    print(subj)
                    
                print()
                subj_target = input("Subject to grade: ")
                
                try:
                    if subj_target not in subjects:
                        # Forzamos un KeyError si la materia no es válida
                        raise KeyError(subj_target)
                        
                    new_grade_raw = input("New grade: ")
                    
                    # Validaciones exigidas en la observación de código
                    try:
                        new_grade = float(new_grade_raw)
                    except ValueError:
                        raise CalificacionInvalidaError("La calificación debe ser un número.")
                        
                    if new_grade < 0 or new_grade > 10:
                        raise CalificacionInvalidaError("La calificación debe estar entre 0 y 10.")
                        
                    print("Do you confirm (yes/no)?")
                    print(f"{subj_target}: {notes[target][subj_target]} ==> {new_grade}")
                    confirm = input()
                    
                    if confirm.lower() == 'yes':
                        notes[target][subj_target] = new_grade
                        print("\nGrade updated!")
                        
                except KeyError:
                    print("Esa materia no existe")
                except CalificacionInvalidaError as e:
                    print(e)
                
                print("\nWrite other thing to exit\n")
                target = input("Student to grade (username): ")
                
                # Validación de KeyError para el usuario
                if target not in student_list and target.lower() != "stop":
                     print("Ese usuario no existe")

        elif role == 'coordinator':
            print("=========================================")
            print("  Professors")
            print("=========================================")
            for u, info in users.items():
                if info['rol'] == 'professor':
                    print(f"User: {u:<10} | Professor: {info['name']}")
                    
            print("\n=========================================")
            print("  Students")
            print("=========================================")
            student_list = []
            for u, info in users.items():
                if info['rol'] == 'student':
                    print(f"User: {u:<10} | Student: {info['name']}")
                    student_list.append(u)
                    
            print("\n=========================================")
            print("  Records")
            print("=========================================")
            header = f"{'SUBJECTS':<13} | " + " | ".join(f"{u:<7}" for u in student_list)
            print(header)
            print("-" * len(header))
            
            for subj in subjects:
                row = f"{subj[:13]:<13} | "
                grades_str = []
                for u in student_list:
                    grades_str.append(f"{notes[u][subj]:<7}")
                row += " | ".join(grades_str)
                print(row)

except EOFError:
    pass