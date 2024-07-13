from app import db
class User(db.Model):
    __tablename__='users'
    
    user_id=db.Column(db.Interger(10),primary_key=True)
    username=db.Column(db.String(25),unique=True,nullable=False)
    email=db.Column(db.String(50),unique=True, nullable=False)
    password_hash=db.Column(db.String(150),nullable=False)
    role=db.Column(db.String(10),nullable=False)
    is_active=db.Column(db.Boolean,default=True)
    confirmed_admin=db.Column(db.Boolean,default=True)
    
    def __repr__(self):
        return f'<User{self.username}>'
    
    