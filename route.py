from flask import Flask, request, jsonify
from database import db, app
from models import Tasks

@app.route('/create_tasks', methods=['POST'])
def ceate_task():
    try:

        data=request.get_json()

        if not data or not 'title' in data or not 'status' in data or not 'body' in data:
            return jsonify({'Error':'Missing required fields'})

        new_task=Task(
            'title': data['title'],
            'body': data['body']
            'status': data['status']
        )
        db.session.add(new_task)
        db.session.commit()

        return jsonify({'message':'Task was created successfully', 'task':{
            'id': new_task.id,
            'title': new_task.title,
            'body': new_task.body,
            'status': new_task.status
        }})
    except Exception as e:
        return jsonify({"error": str(e)})


