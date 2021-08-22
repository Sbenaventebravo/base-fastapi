from sqlalchemy import Column, Integer, String


class Item():
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
