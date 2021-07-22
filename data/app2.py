import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy
import flask


db_path="ncaafootball.sqlite"

engine = create_engine(f"sqlite:///{db_path}")
conn = engine.connect()

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

app = Flask(__name__)

@app.route("/")