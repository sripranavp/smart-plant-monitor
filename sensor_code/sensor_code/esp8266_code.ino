#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";
const char* serverName = "http://your-flask-app-ip:5000/predict";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("Connected to Wi-Fi");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverName);

    // Add any necessary headers here
    http.addHeader("Content-Type", "application/json");

    // Example JSON payload
    String jsonPayload = "{\"example_key\":\"example_value\"}";

    int httpResponseCode = http.POST(jsonPayload);

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println(response);
    } else {
      Serial.println("Error in sending request");
    }

    http.end();
  } else {
    Serial.println("WiFi Disconnected");
  }

  delay(60000); // Delay before next request
}
