// Constants
const float V_REF = 5.0;     // Analog reference voltage (e.g., 5V or 3.3V)
const float R_BITS = 10.0;   // ADC resolution (bits)
const float ADC_STEPS = (1 << int(R_BITS)) - 1; // Number of steps (2^R_BITS - 1)

const int potentiometerPin = A5;

void setup() {
  Serial.begin(4800); // Initialize serial communication
  Serial.println(ADC_STEPS);
}

void loop() {
  int rawValue = analogRead(potentiometerPin); // Read the analog input
  float voltage = (rawValue / ADC_STEPS) * V_REF; // Convert to voltage

  Serial.print("Voltage: ");
  Serial.print(voltage, 3); // Print voltage with 3 decimal places
  Serial.println(" V");
  
  delay(500); // Small delay to avoid flooding the serial monitor
}