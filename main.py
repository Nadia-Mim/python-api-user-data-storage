from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userData.db'
db = SQLAlchemy(app)

# create parent table


class parentType(db.Model):
    __tablename__ = 'parentType'

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    street = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    zipCode = db.Column(db.Integer, nullable=False)
    child = db.relationship('childType')

    def __repr__(self):
        return f"Parent(firstName = {self.firstName}, lastName = {self.lastName}, street = {self.street}, city = {self.city}, state = {self.state}, zipCode = {self.zipCode})"

# create child table


class childType(db.Model):
    __tablename__ = 'childType'

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    parentId = db.Column(db.Integer, db.ForeignKey('parentType.id'))

    def __repr__(self):
        return f"Child(parentId = {self.parentId}, firstName = {self.firstName}, lastName = {self.lastName})"


# please commentout db.create_all() line after the first initialization and creation of database

db.create_all()

# prepare arguments for parent data insert

parent_post_args = reqparse.RequestParser()
parent_post_args.add_argument(
    "firstName", type=str, help="firstName is required", required=True)
parent_post_args.add_argument(
    "lastName", type=str, help="lastName is required", required=True)
parent_post_args.add_argument(
    "street", type=str, help="street is required", required=True)
parent_post_args.add_argument(
    "city", type=str, help="city is required", required=True)
parent_post_args.add_argument(
    "state", type=str, help="state is required", required=True)
parent_post_args.add_argument(
    "zipCode", type=int, help="zipCode is required", required=True)

# prepare arguments for parent data update

parent_update_args = reqparse.RequestParser()
parent_update_args.add_argument(
    "firstName", type=str)
parent_update_args.add_argument(
    "lastName", type=str)
parent_update_args.add_argument(
    "street", type=str)
parent_update_args.add_argument(
    "city", type=str)
parent_update_args.add_argument(
    "state", type=str)
parent_update_args.add_argument(
    "zipCode", type=int)


parent_resource_fields = {
    'id': fields.Integer,
    'firstName': fields.String,
    'lastName': fields.String,
    'address': {'street': fields.String,
                'city': fields.String,
                'state': fields.String,
                'zipCode': fields.Integer}
}

# parent class for create, read, update and delete data


class Parent(Resource):
    @marshal_with(parent_resource_fields)
    # reads data from parent table using parent id
    def get(self, parent_id):
        result = parentType.query.filter_by(id=parent_id).first()
        if not result:
            # shows 404 code and message if the id doesn't exist
            abort(404, message="Could not find parent with that id")
        return result

    @marshal_with(parent_resource_fields)
    # creates data in the parent table
    def post(self, parent_id):
        args = parent_post_args.parse_args()
        parent = parentType(
            firstName=args['firstName'], lastName=args['lastName'], street=args['street'], city=args['city'], state=args['state'], zipCode=args['zipCode'])
        db.session.add(parent)
        db.session.commit()
        # returns the data and success code
        return parent, 201

    @marshal_with(parent_resource_fields)
    # updates parent data using parent id
    def patch(self, parent_id):
        args = parent_update_args.parse_args()
        result = parentType.query.filter_by(id=parent_id).first()
        if not result:
            # # aborts if id doesn't exist
            abort(404, message="Parent does not exist, cannot update...")

        if args['firstName']:
            result.firstName = args['firstName']
        if args['lastName']:
            result.lastName = args['lastName']
        if args['street']:
            result.street = args['street']
        if args['city']:
            result.city = args['city']
        if args['state']:
            result.state = args['state']
        if args['zipCode']:
            result.zipCode = args['zipCode']

        db.session.commit()
        return result

    @marshal_with(parent_resource_fields)
    # deletes parent data and also deletes child data if the parent has a child
    def delete(self, parent_id):
        result = parentType.query.filter_by(id=parent_id).first()
        result1 = childType.query.filter_by(parentId=parent_id).first()
        if not result:
            # aborts if parent id not found
            abort(404, message="Could not find the parent")
        if result1:
            db.session.delete(result1)
            db.session.commit()

        db.session.delete(result)
        db.session.commit()

        # returns 204- deleted successfully notification
        return '', 204

# prepare arguments for child data insert


child_post_args = reqparse.RequestParser()
child_post_args.add_argument(
    "firstName", type=str, help="firstName is required", required=True)
child_post_args.add_argument(
    "lastName", type=str, help="lastName is required", required=True)
child_post_args.add_argument(
    "parentId", type=int, help="parentId is required", required=True)

# prepare arguments for child data update


child_update_args = reqparse.RequestParser()
child_update_args.add_argument(
    "firstName", type=str)
child_update_args.add_argument(
    "lastName", type=str)
child_update_args.add_argument(
    "parentId", type=int)


child_resource_fields = {
    'id': fields.Integer,
    'firstName': fields.String,
    'lastName': fields.String,
    'parentId': fields.Integer
}

# child class for create, read, update and delete data


class Child(Resource):
    @marshal_with(child_resource_fields)
    # reads data from parent table using child id
    def get(self, child_id, parent_id):
        result = childType.query.filter_by(
            id=child_id).first()
        if not result:
            # shows 404 code and message if the id doesn't exist
            abort(404, message="Could not find child with that id")
        return result

    @marshal_with(child_resource_fields)
    # creates data in the child table
    def post(self, child_id, parent_id):
        args = child_post_args.parse_args()
        # check if parent id exist in parent table
        result = parentType.query.filter_by(id=parent_id).first()
        if not result:
            abort(
                # if parent id doesn't exist then it doesn't create child user data
                404, message="Could not find parent with that id, register parent first")
        child = childType(
            firstName=args['firstName'], lastName=args['lastName'], parentId=args['parentId'])
        db.session.add(child)
        db.session.commit()
        # returns child data and success code if user data is created
        return child, 201

    @marshal_with(child_resource_fields)
    # updates child data using child id
    def patch(self, child_id, parent_id):
        args = child_update_args.parse_args()
        result = childType.query.filter_by(
            id=child_id).first()
        if not result:
            # aborts if id doesn't exist
            abort(404, message="Child does not exist, cannot update...")

        if args['firstName']:
            result.firstName = args['firstName']
        if args['lastName']:
            result.lastName = args['lastName']
        if args['parentId']:
            # before updating parent id checks if the parent id exist in parent table
            result1 = parentType.query.filter_by(id=parent_id).first()
            if result1:
                result.parentId = args['parentId']

        db.session.commit()
        return result

    @marshal_with(child_resource_fields)
    # deletes child user data
    def delete(self, child_id, parent_id):
        result = childType.query.filter_by(
            id=child_id).first()
        if not result:
            # aborts if id not found
            abort(404, message="Could not find the child")

        db.session.delete(result)
        db.session.commit()
        # returns 204- deleted successfully notification
        return '', 204


# adds api resource for api links

api.add_resource(Parent, "/parent/<int:parent_id>")
api.add_resource(Child, "/child/<int:child_id><int:parent_id>")

if __name__ == "__main__":
    app.run(debug=True)
