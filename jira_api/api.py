import os

from flask import Flask, request, jsonify

from .jira_stats import get_story_ticket_counts

# Serve React frontend from ../frontend
current_dir = os.path.dirname(os.path.abspath(__file__))
frontend_dir = os.path.abspath(os.path.join(current_dir, '..', 'frontend'))
app = Flask(__name__, static_folder=frontend_dir, static_url_path='')


@app.route('/api/story-ticket-counts')
def story_ticket_counts():
    project_key = request.args.get('project_key')
    if not project_key:
        return jsonify({'error': 'project_key is required'}), 400

    jira_url = os.getenv('JIRA_URL')
    jira_user = os.getenv('JIRA_USER')
    jira_token = os.getenv('JIRA_TOKEN')
    if not all([jira_url, jira_user, jira_token]):
        return jsonify({'error': 'JIRA_URL, JIRA_USER, JIRA_TOKEN must be set'}), 500

    auth = (jira_user, jira_token)
    try:
        counts = get_story_ticket_counts(jira_url, project_key, auth)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    return jsonify(counts)


@app.route('/')
def root():
    # Serve React frontend
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(debug=True)
