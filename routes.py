from flask import Flask, request, jsonify
from shortener import url_store

app = Flask(__name__)

@app.route('/shorten', methods=['POST'])
def shorten_url():
    """Shorten a long URL"""
    # Gap - Validate URL
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    
    long_url = data.get('url')
    if not long_url:
        return jsonify({"error": "Missing URL"}), 400
    
    short_url = url_store.add_url(long_url)
    return jsonify({"short_url": short_url}), 200

@app.route('/<short_id>', methods=['GET'])
def get_original_url(short_id: str):
    """Get the original URL from a short ID"""
    long_url = url_store.get_url(short_id)
    if long_url is None:
        return jsonify({"error": "URL not found"}), 404
    return jsonify({"original_url": long_url}), 200

if __name__ == '__main__':
    app.run(debug=True, port=8000)