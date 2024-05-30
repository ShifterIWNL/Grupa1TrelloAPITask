from Database import Base, engine

# Create all tables in the database
Base.metadata.create_all(bind=engine)

