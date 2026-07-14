# Required Structures
users = {
    'jperez':   {
        'password': '1234',
        'rol': 'student',
        'name': 'Juan Pérez'
    },
    'dromo':    {
        'password': '1234',
        'rol': 'student',
        'name': 'Daniela Romo'
    },
    'mjuarez':  {
        'password': '1234',
        'rol': 'student',
        'name': 'Mauricio Juárez'
    },
    'mlopez':   {
        'password': '1234',
        'rol': 'student',
        'name': 'María López'
    },
    'euc':  {
        'password': '1234',
        'rol': 'student',
        'name': 'Ernesto Uc'
    },
    'cbalam':   {
        'password': '1234',
        'rol': 'student',
        'name': 'Carlos Balam'
    },
    'jpedrozo': {
        'password': '1234',
        'rol': 'professor',
        'name': 'Jorge Pedrozo'
    },
    'dgamboa':  {
        'password': '1234',
        'rol': 'coordinator',
        'name': 'Didier Gamboa'
    }
}

subjects = (
    "Discrete Mathematics",
    "Programming",
    "English II",
    "Differential Calculus",
    "Probability and Statistics",
    "Computer and Server Architecture",
    "Socio-Emotional Skills and Conflict Management"
)

notes = {
    'jperez': {
        'Discrete Mathematics': 8.5,
        'Programming': 9.2,
        'English II': 9.0,
        'Differential Calculus': 7.8,
        'Probability and Statistics': 8.3,
        'Computer and Server Architecture': 6.8,
        'Socio-Emotional Skills and Conflict Management': 9.5
    },
    'dromo': {
        'Discrete Mathematics': 9.0,
        'Programming': 6.7,
        'English II': 9.4,
        'Differential Calculus': 6.2,
        'Probability and Statistics': 9.1,
        'Computer and Server Architecture': 6.5,
        'Socio-Emotional Skills and Conflict Management': 9.8
    },
    'mjuarez': {
        'Discrete Mathematics': 7.5,
        'Programming': 8.0,
        'English II': 8.5,
        'Differential Calculus': 7.0,
        'Probability and Statistics': 7.8,
        'Computer and Server Architecture': 6.2,
        'Socio-Emotional Skills and Conflict Management': 8.9
    },
    'mlopez': {
        'Discrete Mathematics': 9.5,
        'Programming': 9.8,
        'English II': 9.2,
        'Differential Calculus': 9.0,
        'Probability and Statistics': 9.6,
        'Computer and Server Architecture': 9.4,
        'Socio-Emotional Skills and Conflict Management': 10.0
    },
    'euc': {
        'Discrete Mathematics': 8.2,
        'Programming': 6.9,
        'English II': 8.8,
        'Differential Calculus': 6.0,
        'Probability and Statistics': 6.4,
        'Computer and Server Architecture': 8.1,
        'Socio-Emotional Skills and Conflict Management': 9.0
    },
    'cbalam': {
        'Discrete Mathematics': 8.8,
        'Programming': 9.0,
        'English II': 8.5,
        'Differential Calculus': 6.6,
        'Probability and Statistics': 8.9,
        'Computer and Server Architecture': 8.7,
        'Socio-Emotional Skills and Conflict Management': 9.2
    }
}

# 1. Definimos las excepciones personalizadas para nuestras reglas de negocio
class CredencialesInvalidasError(Exception):
    pass

class CalificacionFueraDeRangoError(Exception):
    pass

class OpcionInvalidaError(Exception):
    pass

logged_in = False
username = ""
role = ""

try:
    username = input("User: ")
    password = input("Password: ")
    
    if username not in users or users[username]['password'] != password:
        raise CredencialesInvalidasError("Wrong username/password")

except CredencialesInvalidasError as e:
    print(f"{e}\n")
except EOFError:
    pass

else:
    logged_in = True  
    user_info = users[username]
    role = user_info['rol']
    name = user_info['name']
    print(f"Bienvenid@!, {name} ({role})")

    # ==========================
    # ROL: STUDENT
    # ==========================
    if role == 'student':
        print("=========================================")
        print("  School Report")
        print("=========================================")
        
        approved = set()
        pending = set()
        
        for subj in subjects:
            try:
                grade = float(notes[username][subj])
                
                if grade >= 7.0:
                    print(f"{subj[:26]:<27}: {grade}")
                    approved.add(subj)
                else:
                    pending.add(subj)
            except ValueError:
                print(f"Error en los registros: La calificación de {subj} no es un número válido.")
                
        print("\nApproved:", approved)
        print("Pending :", pending)

    # ==========================
    # ROL: PROFESSOR
    # ==========================
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
        
        try:
            target = input("Student to grade (username): ")
            
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
                        raise OpcionInvalidaError("La materia ingresada no es válida.")
                        
                    new_grade_raw = input("New grade: ")
                    new_grade = float(new_grade_raw)
                    
                    if new_grade < 0 or new_grade > 10:
                        raise CalificacionFueraDeRangoError(f"Grade out of range: {new_grade}. Expected 0-10.")
                        
                    print("\nDo you confirm (yes/no)?")
                    print(f"{subj_target}: {notes[target][subj_target]} ==> {new_grade}")
                    confirm = input()
                    
                    if confirm.lower() == 'yes':
                        notes[target][subj_target] = new_grade
                        print("\nGrade updated!")
                        print(notes[target])
                        
                except ValueError:
                    print("Error: La calificación debe ser un valor numérico.")
                except CalificacionFueraDeRangoError as e:
                    print(e)
                except OpcionInvalidaError as e:
                    print(e)
                
                print("\nWrite other thing to exit\n")
                target = input("Student to grade (username): ")
                
        except EOFError:
            pass

    # ==========================
    # ROL: COORDINATOR
    # ==========================
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