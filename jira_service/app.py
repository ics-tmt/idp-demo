"""
Flask application to expose Jira ticket statistics API.
"""
from flask import Flask, jsonify, request
from .jira_client import fetch_issues

app = Flask(__name__)

@app.route("/api/tickets/broken-by-stories")
def tickets_broken_by_stories():
    """
    Endpoint to return count of tickets broken down by story.

    Query params:
        jql_story: JQL query to filter subtasks or issues to analyze

    Returns a JSON mapping story key to count of tickets.
    """
    jql_story = request.args.get("jql_story")
    if not jql_story:
        return jsonify({"error": "Missing jql_story parameter"}), 400
    issues = fetch_issues(jql_story)
    stats = {}
    for issue in issues:
        parent = issue.get("fields", {}).get("parent")
        key = parent.get("key") if parent else issue.get("key")
        stats[key] = stats.get(key, 0) + 1
    return jsonify(stats)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
