from flask import Blueprint, jsonify, request
from models import Vocabulary, db

bp = Blueprint('vocabulary', __name__)

# Get all vocabulary records
@bp.route('/vocabulary', methods=['GET'])
def get_all_vocabulary():
    # Get the page number and page size from the query parameters
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Get the search term from the query parameters
    search_term = request.args.get('search_term')

    # Query the vocabulary table using the like operator and paginate method
    query = Vocabulary.query.filter(Vocabulary.term.like(f"%{search_term}%")) if search_term else Vocabulary.query
    vocabulary = query.paginate(page=page, per_page=per_page)

    # Convert the results to a list of dictionaries
    results = []
    for v in vocabulary.items:
        results.append(v.to_dict())

    # Construct the response
    response = {
        'page': vocabulary.page,
        'per_page': vocabulary.per_page,
        'total_pages': vocabulary.pages,
        'total_items': vocabulary.total,
        'items': results
    }

    return jsonify(response)



# Get a single vocabulary record by ID
@bp.route('/vocabulary/<int:id>', methods=['GET'])
def get_vocabulary(id):
    vocabulary = Vocabulary.query.get(id)
    if not vocabulary:
        return jsonify({'error': 'Vocabulary not found'})
    return jsonify(vocabulary.to_dict())

# Create a new vocabulary record
@bp.route('/vocabulary', methods=['POST'])
def create_vocabulary():
    data = request.json
    vocabulary = Vocabulary(**data)
    db.session.add(vocabulary)
    db.session.commit()
    return jsonify(vocabulary.to_dict()), 201

# Update an existing vocabulary record
@bp.route('/vocabulary/<int:id>', methods=['PUT'])
def update_vocabulary(id):
    vocabulary = Vocabulary.query.get(id)
    if not vocabulary:
        return jsonify({'error': 'Vocabulary not found'})
    data = request.json
    for key, value in data.items():
        setattr(vocabulary, key, value)
    db.session.commit()
    return jsonify(vocabulary.to_dict())

# Delete an existing vocabulary record
@bp.route('/vocabulary/<int:id>', methods=['DELETE'])
def delete_vocabulary(id):
    vocabulary = Vocabulary.query.get(id)
    if not vocabulary:
        return jsonify({'error': 'Vocabulary not found'})
    db.session.delete(vocabulary)
    db.session.commit()
    return '', 204
