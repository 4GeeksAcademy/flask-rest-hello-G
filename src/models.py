from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean,Text,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(120),nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(120), nullable=False)
    last_name: Mapped[str] = mapped_column(String(120), nullable=False)
    bio: Mapped[str] = mapped_column(Text, nullable=True)
    posts: Mapped[list["Post"]] = relationship(back_populates="user")
    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="user")
    

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username":self.username,
            "firstname": self.first_name,
            "lastname": self.lastname,
            # do not serialize the password, its a security breach
        } 
    
    

class Post(db.Model):
    __tablename__="post"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    content: Mapped[str] = mapped_column(Text)
    user: Mapped["User"] = relationship("User", back_populates="posts")
    comments: Mapped[list["Comment"]] = relationship(back_populates="post")
    medias: Mapped[list["Media"]] = relationship(back_populates="post")



    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            # do not serialize the password, its a security breach
        } 
    
class Media(db.Model):
    __tablename__="media"
    id: Mapped[int]= mapped_column(primary_key = True)
    type: Mapped[str]= mapped_column(String(120), nullable= False)
    url: Mapped[str]= mapped_column(String(120), nullable= False)
    post_id: Mapped[int]= mapped_column(ForeignKey("post.id"), nullable = False)
    post: Mapped["Post"] = relationship("Post", backref="medias")
    
    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "url": self.url,
            "post_id": self.post_id,
        } 
    
class follower(db.Model):
    __tablename__ = "follower"

    id: Mapped[int]= mapped_column(primary_key= True)
    user_from_id: Mapped[int]=  mapped_column(ForeignKey("user.id"), nullable=False)
    user_to_id: Mapped[int]= mapped_column(nullable= False)

    def serialize(self):
        return {
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id,
        }
    

class comments(db.Model):
    __tablename__="comment"
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(Text)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    user: Mapped["User"] = relationship("User", backref="comments")
    post: Mapped["Post"] = relationship("Post", back_populates="comments")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "post_id":self.post_id
            # do not serialize the password, its a security breach
        } 



