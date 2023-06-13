import psutil  # Import the psutil module for system monitoring
from flask import Flask, render_template  # Import Flask and render_template from the flask module

app = Flask(__name__)  # Create a Flask application instance

@app.route("/")  # Define the route for the root URL ("/")
def index():  # Define the index function that will be executed when the root URL is accessed
    cpu_percent = psutil.cpu_percent()  # Get the CPU utilization percentage
    mem_percent = psutil.virtual_memory().percent  # Get the memory utilization percentage
    Messege = None  # Initialize the message variable as None
    if cpu_percent > 80 or mem_percent > 80:  # Check if CPU or memory utilization is above 80%
        Messege = "High CPU or Memory Utilization detected. Please scale up"  # Set the message accordingly
    return render_template("index.html", cpu_metric=cpu_percent, mem_metric=mem_percent, messege=Messege)  # Render the "index.html" template with the CPU and memory metrics

if __name__ == '__main__':  # Check if the script is being run directly
    app.run(debug=True, host='0.0.0.0')  # Start the Flask application in debug mode and listen on all network interfaces
