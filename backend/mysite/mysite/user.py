#import database
#import utils
from typing import Optional, Dict, List


class User:
    """
    Represents a standard user (student).
    Attributes:
        id               – database PK
        username         – unique login name
        is_admin         – False for students
        student_number   – linked 700-number for their own record
    """
    def __init__(self, id: int, username: str, is_admin: bool, student_number: str):
        self.id = id
        self.username = username
        self.is_admin = is_admin
        self.student_number = student_number

    @classmethod
    def register(cls,
                 username: str,
                 password: str,
                 student_number: str) -> 'User':
        """
        Creates a new user with a hashed password and links it to a student record.
        """
        # ensure student exists
        student = database.get_student_by_number(student_number)
        if not student:
            raise ValueError(f"No student with number {student_number}")

        # hash and store
        pw_hash = utils.hash_password(password)
        uid = database.add_user(username, pw_hash, is_admin=False, student_number=student_number)
        return cls(uid, username, False, student_number)

    @classmethod
    def login(cls, username: str, password: str) -> Optional['User']:
        """
        Authenticates and returns a User instance on success.
        """
        row = database.find_user(username)
        if not row:
            return None
        if not utils.verify_password(row["password_hash"], password):
            return None
        return cls(row["id"], row["username"], bool(row["is_admin"]), row["student_number"])

    def view_own_record(self) -> Dict:
        """
        Returns this student's database record as a dict.
        """
        row = database.get_student_by_number(self.student_number)
        if not row:
            raise LookupError("Student record not found.")
        return dict(row)


class Admin(User):
    """
    Represents an admin user, with full CRUD over students.
    """
    def __init__(self, id: int, username: str):
        super().__init__(id, username, True, student_number=None)

    @classmethod
    def register_admin(cls, username: str, password: str) -> 'Admin':
        """
        Create a new admin account (no student_number).
        """
        pw_hash = utils.hash_password(password)
        uid = database.add_user(username, pw_hash, is_admin=True, student_number=None)
        return cls(uid, username)

    def add_student(self, data: Dict) -> int:
        """
        Wrapper around database.add_student for admins.
        """
        return database.add_student(data)

    def edit_student(self, student_number: str, updates: Dict) -> bool:
        return database.update_student(student_number, updates)

    def delete_student(self, student_number: str) -> bool:
        return database.delete_student(student_number)

    def view_all_students(self) -> List[Dict]:
        """
        Returns all student records as a list of dicts.
        """
        rows = database.get_all_students()
        return [dict(r) for r in rows]
