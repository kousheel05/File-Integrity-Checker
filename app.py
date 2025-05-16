from flask import Flask, render_template, request, redirect, url_for
import hashlib
import os

app = Flask(__name__)
HASH_STORE = "stored_hashes.txt"  # File to store original hashes

def calculate_hash(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def load_stored_hashes():
    if not os.path.exists(HASH_STORE):
        return {}
    with open(HASH_STORE, 'r') as f:
        lines = f.readlines()
    return dict(line.strip().split('::') for line in lines if "::" in line)

def save_hash(filename, file_hash):
    with open(HASH_STORE, 'a') as f:
        f.write(f"{filename}::{file_hash}\n")

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    status = ''
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join("uploads", file.filename)
            os.makedirs("uploads", exist_ok=True)
            file.save(filepath)

            current_hash = calculate_hash(filepath)
            stored_hashes = load_stored_hashes()

            if file.filename in stored_hashes:
                if current_hash == stored_hashes[file.filename]:
                    message = "No changes detected. File integrity intact."
                    status = "safe"
                else:
                    message = "File has been modified!"
                    status = "alert"
            else:
                save_hash(file.filename, current_hash)
                message = "File hash stored for future integrity checks."
                status = "stored"

    return render_template('index.html', message=message, status=status)

if __name__ == '__main__':
    app.run(debug=True)
