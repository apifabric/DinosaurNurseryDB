# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py

from sqlalchemy.dialects.sqlite import *


class Dinosaur(Base):
    """description: Represents a dinosaur attending the nursery school."""
    __tablename__ = 'dinosaurs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    species_id = Column(Integer, ForeignKey('species.id'))
    age = Column(Integer)
    is_enrolled = Column(Boolean, default=True)
    enrollment_date = Column(DateTime)


class Species(Base):
    """description: Represents different dinosaur species."""
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    average_lifespan = Column(Integer)


class Caretaker(Base):
    """description: Represents staff caring for dinosaurs."""
    __tablename__ = 'caretakers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    experience_level = Column(String)
    hire_date = Column(DateTime)


class Activity(Base):
    """description: Represents activities held at the nursery."""
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    location = Column(String)
    scheduled_date = Column(DateTime)


class DinosaurActivity(Base):
    """description: Represents the participation of dinosaurs in activities."""
    __tablename__ = 'dinosaur_activities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    dinosaur_id = Column(Integer, ForeignKey('dinosaurs.id'))
    activity_id = Column(Integer, ForeignKey('activities.id'))
    participation_date = Column(DateTime)


class Meal(Base):
    """description: Represents meals provided at the nursery."""
    __tablename__ = 'meals'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    portion_size = Column(String)
    dietary_category = Column(String)


class DinosaurMeal(Base):
    """description: Represents meals consumed by dinosaurs."""
    __tablename__ = 'dinosaur_meals'
    id = Column(Integer, primary_key=True, autoincrement=True)
    dinosaur_id = Column(Integer, ForeignKey('dinosaurs.id'))
    meal_id = Column(Integer, ForeignKey('meals.id'))
    consumption_date = Column(DateTime)


class Training(Base):
    """description: Represents training sessions for dinosaurs."""
    __tablename__ = 'training'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    focus_area = Column(String)
    session_date = Column(DateTime)


class DinosaurTraining(Base):
    """description: Represents the training attendance of dinosaurs."""
    __tablename__ = 'dinosaur_training'
    id = Column(Integer, primary_key=True, autoincrement=True)
    dinosaur_id = Column(Integer, ForeignKey('dinosaurs.id'))
    training_id = Column(Integer, ForeignKey('training.id'))
    attendance_date = Column(DateTime)


class Supply(Base):
    """description: Represents supplies used at the nursery."""
    __tablename__ = 'supplies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    quantity_on_hand = Column(Integer)
    last_stock_date = Column(DateTime)


class SupplyUsage(Base):
    """description: Represents usage of supplies for nursery activities."""
    __tablename__ = 'supply_usage'
    id = Column(Integer, primary_key=True, autoincrement=True)
    supply_id = Column(Integer, ForeignKey('supplies.id'))
    activity_id = Column(Integer, ForeignKey('activities.id'))
    used_date = Column(DateTime)
    quantity_used = Column(Integer)


class Parent(Base):
    """description: Represents the parents of dinosaurs."""
    __tablename__ = 'parents'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    contact_number = Column(String)
    email = Column(String)


class DinosaurParent(Base):
    """description: Represents the relationship between dinosaurs and their parents."""
    __tablename__ = 'dinosaur_parents'
    id = Column(Integer, primary_key=True, autoincrement=True)
    dinosaur_id = Column(Integer, ForeignKey('dinosaurs.id'))
    parent_id = Column(Integer, ForeignKey('parents.id'))


# end of model classes


try:
    
    
    
    
    # ALS/GenAI: Create an SQLite database
    
    engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    
    Base.metadata.create_all(engine)
    
    
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    
    
    # ALS/GenAI: Prepare for sample data
    
    
    
    session.commit()
    species1 = Species(id=1, name='Tyrannosaurus', average_lifespan=30)
    species2 = Species(id=2, name='Triceratops', average_lifespan=60)
    species3 = Species(id=3, name='Velociraptor', average_lifespan=25)
    species4 = Species(id=4, name='Stegosaurus', average_lifespan=70)
    dino1 = Dinosaur(id=1, name='Rexy', species_id=1, age=8, is_enrolled=True, enrollment_date=date(2023, 1, 10))
    dino2 = Dinosaur(id=2, name='Cera', species_id=2, age=5, is_enrolled=True, enrollment_date=date(2023, 2, 11))
    dino3 = Dinosaur(id=3, name='Blue', species_id=3, age=3, is_enrolled=True, enrollment_date=date(2023, 3, 12))
    dino4 = Dinosaur(id=4, name='Spike', species_id=4, age=2, is_enrolled=True, enrollment_date=date(2023, 4, 13))
    caretaker1 = Caretaker(id=1, name='Alice', experience_level='Intermediate', hire_date=date(2023, 5, 14))
    caretaker2 = Caretaker(id=2, name='Bob', experience_level='Expert', hire_date=date(2023, 6, 15))
    caretaker3 = Caretaker(id=3, name='Charlie', experience_level='Beginner', hire_date=date(2023, 7, 16))
    caretaker4 = Caretaker(id=4, name='Dana', experience_level='Advanced', hire_date=date(2023, 8, 17))
    activity1 = Activity(id=1, name='Jungle Gym', location='Playground', scheduled_date=date(2023, 9, 18))
    activity2 = Activity(id=2, name='Color Fun', location='Art Room', scheduled_date=date(2023, 10, 19))
    activity3 = Activity(id=3, name='Splash Tactics', location='Water Park', scheduled_date=date(2023, 11, 20))
    activity4 = Activity(id=4, name='Mini Cavern Expedition', location='Indoor Cave', scheduled_date=date(2023, 12, 21))
    dino_activity1 = DinosaurActivity(id=1, dinosaur_id=1, activity_id=1, participation_date=date(2023, 9, 18))
    dino_activity2 = DinosaurActivity(id=2, dinosaur_id=2, activity_id=2, participation_date=date(2023, 10, 19))
    dino_activity3 = DinosaurActivity(id=3, dinosaur_id=3, activity_id=3, participation_date=date(2023, 11, 20))
    dino_activity4 = DinosaurActivity(id=4, dinosaur_id=4, activity_id=4, participation_date=date(2023, 12, 21))
    meal1 = Meal(id=1, name='Salad', portion_size='Medium', dietary_category='Herbivore')
    meal2 = Meal(id=2, name='Fish', portion_size='Large', dietary_category='Carnivore')
    meal3 = Meal(id=3, name='Seeds', portion_size='Small', dietary_category='Herbivore')
    meal4 = Meal(id=4, name='Fruit', portion_size='Small', dietary_category='Omnivore')
    dino_meal1 = DinosaurMeal(id=1, dinosaur_id=1, meal_id=2, consumption_date=date(2023, 9, 18))
    dino_meal2 = DinosaurMeal(id=2, dinosaur_id=2, meal_id=1, consumption_date=date(2023, 10, 19))
    dino_meal3 = DinosaurMeal(id=3, dinosaur_id=3, meal_id=4, consumption_date=date(2023, 11, 20))
    dino_meal4 = DinosaurMeal(id=4, dinosaur_id=4, meal_id=1, consumption_date=date(2023, 12, 21))
    training1 = Training(id=1, title='Running Speed', focus_area='Physique', session_date=date(2023, 9, 25))
    training2 = Training(id=2, title='Herbalist Adventure', focus_area='Diet', session_date=date(2023, 10, 26))
    training3 = Training(id=3, title='Rain Hunt', focus_area='Tracking', session_date=date(2023, 11, 27))
    training4 = Training(id=4, title='Pond Stash', focus_area='Storage', session_date=date(2023, 12, 28))
    dino_training1 = DinosaurTraining(id=1, dinosaur_id=1, training_id=1, attendance_date=date(2023, 9, 25))
    dino_training2 = DinosaurTraining(id=2, dinosaur_id=2, training_id=3, attendance_date=date(2023, 10, 26))
    dino_training3 = DinosaurTraining(id=3, dinosaur_id=3, training_id=4, attendance_date=date(2023, 11, 27))
    dino_training4 = DinosaurTraining(id=4, dinosaur_id=4, training_id=2, attendance_date=date(2023, 12, 28))
    supply1 = Supply(id=1, name='Paint Brushes', quantity_on_hand=60, last_stock_date=date(2023, 1, 1))
    supply2 = Supply(id=2, name='Building Blocks', quantity_on_hand=100, last_stock_date=date(2023, 2, 15))
    supply3 = Supply(id=3, name='Water Guns', quantity_on_hand=30, last_stock_date=date(2023, 3, 20))
    supply4 = Supply(id=4, name='Sketch Pads', quantity_on_hand=75, last_stock_date=date(2023, 4, 25))
    supply_usage1 = SupplyUsage(id=1, supply_id=1, activity_id=2, used_date=date(2023, 10, 19), quantity_used=10)
    supply_usage2 = SupplyUsage(id=2, supply_id=2, activity_id=1, used_date=date(2023, 9, 18), quantity_used=15)
    supply_usage3 = SupplyUsage(id=3, supply_id=3, activity_id=3, used_date=date(2023, 11, 20), quantity_used=20)
    supply_usage4 = SupplyUsage(id=4, supply_id=4, activity_id=2, used_date=date(2023, 10, 19), quantity_used=25)
    parent1 = Parent(id=1, name='Grendel', contact_number='1234567890', email='grendel@example.com')
    parent2 = Parent(id=2, name='Aurora', contact_number='0987654321', email='aurora@example.com')
    parent3 = Parent(id=3, name='Zephyr', contact_number='1122334455', email='zephyr@example.com')
    parent4 = Parent(id=4, name='Fjord', contact_number='5566778899', email='fjord@example.com')
    dino_parent1 = DinosaurParent(id=1, dinosaur_id=1, parent_id=2)
    dino_parent2 = DinosaurParent(id=2, dinosaur_id=2, parent_id=1)
    dino_parent3 = DinosaurParent(id=3, dinosaur_id=3, parent_id=4)
    dino_parent4 = DinosaurParent(id=4, dinosaur_id=4, parent_id=3)
    
    
    
    session.add_all([species1, species2, species3, species4, dino1, dino2, dino3, dino4, caretaker1, caretaker2, caretaker3, caretaker4, activity1, activity2, activity3, activity4, dino_activity1, dino_activity2, dino_activity3, dino_activity4, meal1, meal2, meal3, meal4, dino_meal1, dino_meal2, dino_meal3, dino_meal4, training1, training2, training3, training4, dino_training1, dino_training2, dino_training3, dino_training4, supply1, supply2, supply3, supply4, supply_usage1, supply_usage2, supply_usage3, supply_usage4, parent1, parent2, parent3, parent4, dino_parent1, dino_parent2, dino_parent3, dino_parent4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
