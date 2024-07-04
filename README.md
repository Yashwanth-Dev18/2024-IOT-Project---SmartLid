# SmartLid
  By: Yashwanth Krishna Devanaboina (yd222cj)

## LNU 2024 IOT Project Report
### Project Overview: 

The Smart Lid IoT System is designed to automate the opening and closing of a lid using a servo motor, triggered by an ultrasonic sensor detecting movement. Implemented on a Raspberry Pi Pico W, the system collects data on lid usage, including the count of accesses and the distance of detected objects. This data is transmitted to the Ubidots IoT platform, where it is visualized through gauges and graphs, providing insightful analysis of usage patterns. The project integrates real-time data collection, automation, and IoT capabilities to enhance convenience and provide valuable usage metrics.

The project might take approximately 2 weeks to complete, including setup, programming, testing, and data visualization.

# Objective

**Why I Chose the Project:**
I chose to build the Smart Lid IoT System to address the need for a hands-free, automated solution for frequently accessed containers. This project combines my interests in automation, IoT, and data analytics, providing a practical application that enhances everyday convenience and hygiene. My project prevents conatact between humans ans germs or contaminated areas like trash bins etc. 

**Purpose:**
The primary purpose of this device is to automate the opening and closing of a lid based on proximity detection, improving ease of use and maintaining cleanliness. This is particularly useful in environments where hands-free operation is beneficial, such as kitchens, laboratories, and medical facilities.

**Insights and Data Utilization:**
By collecting data on lid usage, such as the frequency of access and the distance of detected objects, the system can provide valuable insights into usage patterns. This data can help in understanding peak usage times, assessing the effectiveness of the lid's placement, and identifying opportunities for further automation or optimization. We'll be able to see who had access and when precisely. Additionally, the data visualization on the Ubidots platform offers a clear representation of such patterns.


# Material

I bought an [IOT Kit](https://www.amazon.se/Freenove-Raspberry-Included-Compatible-513-Page/dp/B0BJ1PV4MM/ref=sr_1_6?crid=TXL7CFHWE8XQ&dib=eyJ2IjoiMSJ9._zwwQWVsgmjpBKtPxxaX2bvRxdggWuvXNmzixA7W8V0it459V9k9EYixw5YfSRUVNiL_H4YXUvVupqek-eAc9mjKofWhG40XVJIAfXXwMrrBudbQuQD_j53J3uJIDLSn7gA24-1uHzxJ8EY4s-AT49q7eZcpWAjvz5PfluLcFSYoclf8x006BNO6GRmc3VBh3XoevmNjugI2bwbzavGBs8hzLfVe3ULBzL_hrA4hWP8vOH6w5VB34up86xHbeJk1JWPsXYQF5mDOWAFqtpH06Urvd1DHR9rx-xYSr_rICzw.ZLmNlpfJ2MZGbjCpmnpLm5qOlemaXXOUGS_yNUk0GwM&dib_tag=se&keywords=iot+kit+with+raspberry+pi+pico+w&qid=1719669936&sprefix=iot+kit+with+raspberry+pi+pico+w%2Caps%2C79&sr=8-6) which costs 499sek in Amazon.
I used the components that I needed for the project from the IOT kit.


### Materials Used in Smart Lid IoT System

Here's a list of all the components I used for the SmartLid.

| Component           | Purpose                                                                 | Specifications                                                                                                                                                  |
|---------------------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Raspberry Pi Pico W | Microcontroller to control the system.                                   | Dual-core ARM Cortex M0+ processor, 2.4 GHz wireless connectivity, 264KB RAM, 2MB Flash.                                                                          |
| Ultrasonic Sensor   | Measures distance to trigger lid mechanism.                              | Operating voltage: 5V, Measuring angle: 15 degrees, Ranging distance: 2cm – 400 cm, Accuracy: ±3mm.                                                                |
| Servo Motor         | Opens and closes the lid mechanically.                                   | Operating voltage: 4.8V – 6V, Torque: 1.8 kgf·cm (4.8V), Speed: 0.1 sec/60 degrees (4.8V), Angle: 180 degrees.                                                    |
| Jumper Wires        | Connects components to Raspberry Pi Pico W.                              | Male-to-male, female-to-female, and male-to-female variations, standard 20cm length.                                                                              |
| Breadboard          | Provides a platform for temporary circuit construction.                  | 830 tie points, ABS plastic material.                                                                                                                             |
|                                                                                                                                          |


[Click here](https://www.amazon.se/Freenove-Raspberry-Included-Compatible-513-Page/dp/B0BJ1PV4MM/ref=sr_1_6?crid=TXL7CFHWE8XQ&dib=eyJ2IjoiMSJ9._zwwQWVsgmjpBKtPxxaX2bvRxdggWuvXNmzixA7W8V0it459V9k9EYixw5YfSRUVNiL_H4YXUvVupqek-eAc9mjKofWhG40XVJIAfXXwMrrBudbQuQD_j53J3uJIDLSn7gA24-1uHzxJ8EY4s-AT49q7eZcpWAjvz5PfluLcFSYoclf8x006BNO6GRmc3VBh3XoevmNjugI2bwbzavGBs8hzLfVe3ULBzL_hrA4hWP8vOH6w5VB34up86xHbeJk1JWPsXYQF5mDOWAFqtpH06Urvd1DHR9rx-xYSr_rICzw.ZLmNlpfJ2MZGbjCpmnpLm5qOlemaXXOUGS_yNUk0GwM&dib_tag=se&keywords=iot+kit+with+raspberry+pi+pico+w&qid=1719669936&sprefix=iot+kit+with+raspberry+pi+pico+w%2Caps%2C79&sr=8-6) to purchase the Iot Kit that I used for the project.


# Computer Setup for Programming the Raspberry Pi Pico W

**Chosen IDE:** 
Visual Studio Code

**How the Code is Uploaded:** 
Using the VS Code extension "Pico-W-Go" or you can right-click on the folder and click on "Uplaod Project to Pico".

**Computer Setup:**

1. **Install Visual Studio Code:**
   - Download and install VS Code from the [official website](https://code.visualstudio.com/).

2. **Install Python:**
   - Download and install Python from the [official website](https://www.python.org/).
   - Ensure Python is added to your PATH during installation.

3. **Install Node.js:**
   - Download and install Node.js from the [official website](https://nodejs.org/).

4. **Flash MicroPython Firmware onto the Raspberry Pi Pico W:**
   - Download the MicroPython firmware (.uf2 file) from the [official Raspberry Pi website](https://micropython.org/download/RPI_PICO_W/).
   - Connect the Pico W to your computer while holding the BOOTSEL button.
   - Drag and drop the downloaded .uf2 file into the RPI-RP2 drive that appears.

5. **Set Up VS Code for Pico W Development:**
   - Open VS Code and go to the Extensions view by clicking the square icon in the sidebar or pressing `Ctrl+Shift+X`.
   - Search for and install the following extensions:
     - `"ms-python.python"`: Microsoft’s Python extension for VS Code.
     - `"visualstudioexptteam.vscodeintellicode"`: AI-assisted code completion.
     - `"ms-python.vscode-pylance"`: Fast, feature-rich language support for Python.
     - `"paulober.pico-w-go"`: Extension specifically for Raspberry Pi Pico W development.
   - Reload VS Code to activate the extensions.

6. **Configure Pico-W-Go:**
   - Open the command palette in VS Code (`Ctrl+Shift+P`).
   - Type and select `Pico-W-Go: Configure project`.
   - Follow the prompts to set up the project directory and configure settings.

7. **Connect the Raspberry Pi Pico W:**
   - Connect your Raspberry Pi Pico W to your computer via USB.
   - Open the command palette (`Ctrl+Shift+P`), type and select `Pico-W-Go: New project`.
   - Choose a directory for your project.

8. **Writing and Uploading Code:**
   - Create a new Python file in your project directory (e.g., `main.py`).
   - Write your MicroPython code.
   - To upload the code to your Pico W, right-click the file and select `Run on Pico-W`.


# Circuit Diagram for Smart Lid IoT System

![alt text](<SmartLid Circuit Diagram.png>)

### Here are the Breadboard connections:
**Servo Motor:**

    1. The Gnd of the servo meter is connected to Ground(38th pin) of Raspberry Pi Pico W.
    2. The power of the servo meter is connected to VBUS(40th pin) of Raspberry Pi Pico W.
    3. The signal of the servo meter is connected to GP15(20th pin) of Raspberry Pi Pico W.

**Ultrasonic Motion Sensor:**

    1. The Gnd of the ultrasonic motion sensor is connected to Ground(38th pin) of Raspberry Pi Pico W.
    2. The Echo of the ultrasonic motion sensor is connected to GP3(5th pin) of Raspberry Pi Pico W.
    3. The Trig of the ultrasonic motion sensor is connected to GP2(4th pin) of Raspberry Pi Pico W.
    4. The VCC of the ultrasonic motion sensor is connected to VBUS(40th pin) of Raspberry Pi Pico W.


# IOT Platform - Ubidot


Ubidots is a cloud-based platform that's perfect for IoT projects. Here's why I picked it for my smart lid project:



**Data Collection:**
    
Ubidots offered APIs and MQTT support, making it easy to send data from my Raspberry Pi Pico W.


**Data Storage:**
    
It stores all the data efficiently, no matter how much I collect.

**Data Visualization:**
    
I can create custom dashboards with graphs, charts, and gauges to see my data in real-time. Ubidots can send alerts when certain conditions are met, which is great for monitoring. However, if you are making us of the aggregation functions, then the data won't be updated in the dashboard unless it is refreshed. But I fixed this issue by implementing my calculations and aggregation functions in the code rather than having it in the server. Ubidot works well with other services like Google Sheets, Zapier, and IFTTT.



Easy to use with plenty of resources to help beginners like me.

**Affordability:**

Free Plan is Good for small projects and learning. I personally have used the free plan and it was sufficient. Paid Plans are also available for more features and when scaling up.

**Analysis:**


Pros: Simple and great for beginners.


Cons: Limited in features and scalability.


Ubidots can handle more devices easily as the project grows. Higher-tier plans offer more advanced data analysis and alert features. Ubidots supports global deploymnt, making it great for larger projects. In conclusion, I chose Ubidots because it’s easy to use, affordable, and perfect for collecting and visualizing data from my smart lid project. It's also flexible enough to grow with my project. 


On the other hand, there are other platforms you could go for such as Datacake, Amazon IOT, IBM IOT, and TIG-Stack.

# The Code

Firstly, the entire code for this project comprises of two files; Boot.py and Main.py. The boot file is the first file that a microcontroller runs before any other file in the project folder uploaded to it. Thus, in the Boot file, I have constructed code which establishes connection with the wifi. The main.py file has the code for the device functionalty and data transfer. The libraries that were imported to successfully execute the task include machine, utime, and urequests.



    def build_json(count_variable, count_value, distance_variable, distance_value,
                  avg_distance_variable, avg_distance_value):
        try:
            data = {
                count_variable: {"value": count_value},
                avg_distance_variable: {"value": avg_distance_value},
                distance_variable: {"value": distance_value}
            }
            return data

The build_json function helps me create a dictionary that holds three key-value pairs. Each key corresponds to a variable name (like count, average distance, or distance), and its value is another dictionary with the actual measurement. The function takes in six parameters: the names and values for the count of objects detected, the last measured distance, and the average distance. Inside the function, I created a dictionary with these variables, where each key is a variable name and its value is another dictionary containing the actual measurement. This dictionary is then returned, making it easy to send my measurements to a server or use them elsewhere in my code.


    def send_data(device, count_variable, count_value, distance_variable,
                  distance_value, avg_distance_variable, avg_distance_value):
        try:
            url = "https://industrial.api.ubidots.com/api/v1.6/devices/" + device
            headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

            data = build_json(count_variable, count_value, distance_variable,
                              distance_value, avg_distance_variable,
                              avg_distance_value)

            if data is not None:
                # print("Sending data to Ubidots:", data)
                req = requests.post(url=url, headers=headers, json=data)
                # print("Response from Ubidots:", req.json())
                req.close()


The send_data function sends my measurement data to the Ubidots server. Here's how it works...

I got the URL for the Ubidots API using the device name and set up the headers with my authentication token and content type from the platform. The build_json function was called to create a dictionary with my measurement data. If the data dictionary is not empty, sending it to the Ubidots server using a POST request. After sending, the request is being closed to free up space and make it simple for the microcontroller and server to communicate.


        current_time = utime.localtime()
        current_hour = current_time[3]

        # Checking if it's midnight (00:00:00)
        if current_hour == 0 and current_time[4] == 0 and current_time[5] < 1:
            # Reset count and AVG_dist
            count = 0
            AVG_dist = 0

In this part of the code, I'm using the using the utime library to get the local time. Then, I check if it's midnight(00:00:00), and reset the variables back to zero. This is due to the reason that the whole point of my data visualization is to be able to see the no of times someone had access. This will only be possible if the count and distance variables reset to zero in order to tune it to right representation.


# Transmitting the Data

The data transfer takes place every time the ultrasonic motion sensor triggers the signal. The sensor only triggers when the movement detected is less than 30cm radius. So, when we wave to open the lid, the data such as the distance at which our hand was placed and the time of the access and count will be trasnfered to the IOT platform(Ubidot). Thus, the data transfer frequency depends on when the device is used or when the ultrasonic motion sensor is triggered.

1. **Wireless Protocol: WiFi**

WiFi was chosen due to its widespread availability and ease of use for IoT devices. It allows for relatively high data transfer rates and is suitable for environments where the device is within range of a WiFi network. WiFi typically offers a range of up to 100 meters indoors. However, it consumes more power compared to protocols like LoRa, making it less suitable for battery-powered devices unless they have access to frequent recharging or a stable power source. The power supply that I've set is a power cable connecting to the wall. So, since the power supply was never the concern I chose Wifi, and it worked perfectly as anticipated.

2. **Transport Protocol: HTTP**

HTTP was chosen for its simplicity web services, including Ubidots. It was smooth and did not require much code to initiate it. HTTP POST requests are straightforward to implement.I imported the urequests and it helped me. When it comes to impact on Device Range and Battery Consumption; HTTP over WiFi does not significantly affect the range beyond what is inherent to the WiFi protocol itself. However, the power consumption can be higher compared to more lightweight protocols like MQTT. For devices that need to conserve battery, HTTP might not be the best choice.


    def build_json(count_variable, count_value, distance_variable, distance_value,
               avg_distance_variable, avg_distance_value):
    data = {
        count_variable: {"value": count_value},
        avg_distance_variable: {"value": avg_distance_value},
        distance_variable: {"value": distance_value}
    }
    return data


JSON is a lightweight data-interchange format that is easy to read and write for both humans and machines. It is widely supported across many platforms like the one I used, "Ubidot". The data is then formatted into a JSON object with keys representing the variable names (count, avgdist, and distance) and their corresponding values.

The measured data (count of objects, average distance, and current distance) is packaged into a JSON object using the build_json function.

    url = "https://industrial.api.ubidots.com/api/v1.6/devices/" + device
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}


The URL for the Ubidots API endpoint is created, and the necessary headers for authentication and content type are set. This is how I managed to transfer data into the Ubitdot. 


    # UBIDOT SETUP
    TOKEN = "BBUS-8yF1VY42uoq9fySuVCSmgQQ7ctdo4o"
    DEVICE_LABEL = "picolid"
    count_VAR = "count"
    avg_VAR = "avgdist"
    dist_VAR = "distance"

I also had to create the variables in ubidot Platfor and have them assigned to global variables like u can see aobve.


![alt text](<Ubidot variables.png>)

The above image is an insight into the Ubidot platform and how you can create variables in it.


# Presenting the Data

The data can be represented in the form of various graphs, charts, gauges, etc. These are known as widgets. Widgets allow us to visualize the raw data that we get from our IOT device with the help of the back-end code. 
We have to create a dashboard, give it a name, and set our widgets accordingly. We are going to be using variables that we created for our device as shown in the picture above. The graphical representation widgets that I have implemented all have variables assigned to them depending on the info that I want to dipslay from the graph.

### Constructing the IOT Ubidot Dashboard:

On the left land side menu, we can create a dashboard and give it a name. Then we can create widgets. I have created 1 graph, 2 charts, 1 gauge and also added a clock widget.

The Widget in the prject's dashboard are...
    1. SmartLid Access Chart
    2. Avg Distance Detection Gauge
    3. Distance Chart
    4. SmartLid Hourly Access Chart

1. ### SmartLid Access Chart

![alt text](<SmartLid Main Access.png>)
The above grapgh has the count variable allocated. This graph shows when the lid got opened throughout the day. The grapgh has a span for 24 hours. It'll show the access to the conatiner the last 24 hours. More data can be viewed to tuning it into large range. The variable being assigned to this is count. This count is received by the server from the pico's backend code.

2. ### Avg Distance Detection Gauge

![alt text](<SmartLid Gauge.png>)
The above gauge widget on the dashboard indicates the average distance scaled over the past 24 hours. It shows how much distance, on average, the hand was placed in front of the sensor during that time period. The min 0 and the max is 30 because the max distance which can be recorded is 30. Thus the average will not exceed 30. Since, in our code we reset the distance variable to zero at midnight. The average is the average of that particular day.

I faced a problem using the aggregate function, "average". The dashboard wouldn't refresh the data instantaneously when we use aggregate functions through the Ubidot server. So, instead I calculated the average in the code in the backend and sent that value as raw data to the server. This way, I solved the delayed data update problem. So now, a user don't have to refresh the page in order to view the updates, instead the the platform will update instantabeously.

3. ### Distance Chart

![alt text](<SmartLid Distance Chart.png>)
This chart shows us the exact distance at particular times when the sensor recorded. The chart shows us the distance detected at each instance of lid being opening. The data is spanned out to many days.

4. ### SmartLid Hourly Access Chart

![alt text](<SmartLid Hourly Access.png>)
This chart shows the hourly aggregated information on the access. This is an extention to the first grapgh. This is a more consolidated grapgh which shows how many number of times the lid got opened in the spam of the hourly intervals of time. Here I am using the aggregation method called "count", and the variable assigned to this is also called "count".


# Final Design

Here are the final results...
![alt text](<Project Final Results.png>)

![alt text](<Final Design Pic2.jpg>)

![alt text](<Final Design Pic1.jpg>)


The project was largely successful, achieving its primary goal of accurately tracking and displaying the average hand distance using a sensor. Here are my detailed thoughts:

**Successes:**

1. Data Accuracy: 
  The system consistently provided accurate distance measurements.

2. User Interface: 
  The gauge widget and dashboard were designed to be user-friendly, facilitating easy interpretation of data.
Real-time Updates: The real-time nature of the updates ensured that the information displayed was always current.

3. Efficient Code:
  The code efficiently measures and transmits sensor data using WiFi, and leverages HTTP and JSON for straightforward data handling. The use of functions for building JSON and sending data ensures modularity and readability. Overall, it's a solid implementation for real-time IoT data transmission.

**Areas for Improvement:**

1. Sensor Calibration:
The sensor calibration process could be enhanced to ensure even greater accuracy, particularly in varying lighting conditions or environments. This is because every day once or twice it would detect movement even though there's isn't anything due to varying light and harsh wind consitions near the window.




