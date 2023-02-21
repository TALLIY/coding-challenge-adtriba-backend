from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sphere-sample-data.db'
db = SQLAlchemy(app)

class sphere_sample_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    source = db.Column(db.String)
    attributed_conversions = db.Column(db.Float)
    attributed_revenue = db.Column(db.Float)
    type = db.Column(db.String)
    spends = db.Column(db.Float)
    partition_id = db.Column(db.String)
    optimisation_target = db.Column(db.String)

    def __repr__(self):
        return '<Entry %r>' % self.date
    
    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date, 
            'source': self.source,
            'attributed_conversions': self.attributed_conversions,
            'attributed_revenue': self.attributed_revenue,
            'type': self.type,
            'spends': self.spends, 
            'partition_id': self.partition_id,
            'optimisation_target': self.optimisation_target
        }
    
@app.route('/', methods=['GET'])
def index():
    results = db.session.query(sphere_sample_data).all()
    results_dict = [result.to_dict() for result in results[1:]]
    return jsonify({'results': results_dict})

if __name__ == "__main__":
    app.run(debug=True)
    