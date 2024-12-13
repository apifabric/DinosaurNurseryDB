# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  December 13, 2024 22:07:46
# Database: sqlite:////tmp/tmp.DqbevjbJUc-01JF10Z16CSFXDKHW0979W53T4/DinosaurNurseryDB/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Activity(SAFRSBaseX, Base):
    """
    description: Represents activities held at the nursery.
    """
    __tablename__ = 'activities'
    _s_collection_name = 'Activity'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    scheduled_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    SupplyUsageList : Mapped[List["SupplyUsage"]] = relationship(back_populates="activity")
    DinosaurActivityList : Mapped[List["DinosaurActivity"]] = relationship(back_populates="activity")



class Caretaker(SAFRSBaseX, Base):
    """
    description: Represents staff caring for dinosaurs.
    """
    __tablename__ = 'caretakers'
    _s_collection_name = 'Caretaker'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    experience_level = Column(String)
    hire_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)



class Meal(SAFRSBaseX, Base):
    """
    description: Represents meals provided at the nursery.
    """
    __tablename__ = 'meals'
    _s_collection_name = 'Meal'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    portion_size = Column(String)
    dietary_category = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    DinosaurMealList : Mapped[List["DinosaurMeal"]] = relationship(back_populates="meal")



class Parent(SAFRSBaseX, Base):
    """
    description: Represents the parents of dinosaurs.
    """
    __tablename__ = 'parents'
    _s_collection_name = 'Parent'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact_number = Column(String)
    email = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    DinosaurParentList : Mapped[List["DinosaurParent"]] = relationship(back_populates="parent")



class Species(SAFRSBaseX, Base):
    """
    description: Represents different dinosaur species.
    """
    __tablename__ = 'species'
    _s_collection_name = 'Species'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    average_lifespan = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    DinosaurList : Mapped[List["Dinosaur"]] = relationship(back_populates="species")



class Supply(SAFRSBaseX, Base):
    """
    description: Represents supplies used at the nursery.
    """
    __tablename__ = 'supplies'
    _s_collection_name = 'Supply'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity_on_hand = Column(Integer)
    last_stock_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    SupplyUsageList : Mapped[List["SupplyUsage"]] = relationship(back_populates="supply")



class Training(SAFRSBaseX, Base):
    """
    description: Represents training sessions for dinosaurs.
    """
    __tablename__ = 'training'
    _s_collection_name = 'Training'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    focus_area = Column(String)
    session_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    DinosaurTrainingList : Mapped[List["DinosaurTraining"]] = relationship(back_populates="training")



class Dinosaur(SAFRSBaseX, Base):
    """
    description: Represents a dinosaur attending the nursery school.
    """
    __tablename__ = 'dinosaurs'
    _s_collection_name = 'Dinosaur'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    species_id = Column(ForeignKey('species.id'))
    age = Column(Integer)
    is_enrolled = Column(Boolean)
    enrollment_date = Column(DateTime)

    # parent relationships (access parent)
    species : Mapped["Species"] = relationship(back_populates=("DinosaurList"))

    # child relationships (access children)
    DinosaurActivityList : Mapped[List["DinosaurActivity"]] = relationship(back_populates="dinosaur")
    DinosaurMealList : Mapped[List["DinosaurMeal"]] = relationship(back_populates="dinosaur")
    DinosaurParentList : Mapped[List["DinosaurParent"]] = relationship(back_populates="dinosaur")
    DinosaurTrainingList : Mapped[List["DinosaurTraining"]] = relationship(back_populates="dinosaur")



class SupplyUsage(SAFRSBaseX, Base):
    """
    description: Represents usage of supplies for nursery activities.
    """
    __tablename__ = 'supply_usage'
    _s_collection_name = 'SupplyUsage'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    supply_id = Column(ForeignKey('supplies.id'))
    activity_id = Column(ForeignKey('activities.id'))
    used_date = Column(DateTime)
    quantity_used = Column(Integer)

    # parent relationships (access parent)
    activity : Mapped["Activity"] = relationship(back_populates=("SupplyUsageList"))
    supply : Mapped["Supply"] = relationship(back_populates=("SupplyUsageList"))

    # child relationships (access children)



class DinosaurActivity(SAFRSBaseX, Base):
    """
    description: Represents the participation of dinosaurs in activities.
    """
    __tablename__ = 'dinosaur_activities'
    _s_collection_name = 'DinosaurActivity'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    dinosaur_id = Column(ForeignKey('dinosaurs.id'))
    activity_id = Column(ForeignKey('activities.id'))
    participation_date = Column(DateTime)

    # parent relationships (access parent)
    activity : Mapped["Activity"] = relationship(back_populates=("DinosaurActivityList"))
    dinosaur : Mapped["Dinosaur"] = relationship(back_populates=("DinosaurActivityList"))

    # child relationships (access children)



class DinosaurMeal(SAFRSBaseX, Base):
    """
    description: Represents meals consumed by dinosaurs.
    """
    __tablename__ = 'dinosaur_meals'
    _s_collection_name = 'DinosaurMeal'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    dinosaur_id = Column(ForeignKey('dinosaurs.id'))
    meal_id = Column(ForeignKey('meals.id'))
    consumption_date = Column(DateTime)

    # parent relationships (access parent)
    dinosaur : Mapped["Dinosaur"] = relationship(back_populates=("DinosaurMealList"))
    meal : Mapped["Meal"] = relationship(back_populates=("DinosaurMealList"))

    # child relationships (access children)



class DinosaurParent(SAFRSBaseX, Base):
    """
    description: Represents the relationship between dinosaurs and their parents.
    """
    __tablename__ = 'dinosaur_parents'
    _s_collection_name = 'DinosaurParent'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    dinosaur_id = Column(ForeignKey('dinosaurs.id'))
    parent_id = Column(ForeignKey('parents.id'))

    # parent relationships (access parent)
    dinosaur : Mapped["Dinosaur"] = relationship(back_populates=("DinosaurParentList"))
    parent : Mapped["Parent"] = relationship(back_populates=("DinosaurParentList"))

    # child relationships (access children)



class DinosaurTraining(SAFRSBaseX, Base):
    """
    description: Represents the training attendance of dinosaurs.
    """
    __tablename__ = 'dinosaur_training'
    _s_collection_name = 'DinosaurTraining'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    dinosaur_id = Column(ForeignKey('dinosaurs.id'))
    training_id = Column(ForeignKey('training.id'))
    attendance_date = Column(DateTime)

    # parent relationships (access parent)
    dinosaur : Mapped["Dinosaur"] = relationship(back_populates=("DinosaurTrainingList"))
    training : Mapped["Training"] = relationship(back_populates=("DinosaurTrainingList"))

    # child relationships (access children)
