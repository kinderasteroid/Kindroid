#include <LiquidCrystal.h>


// Pin configuration for the LCD
const int rs = 12;
const int en = 11;
const int d4 = 5;
const int d5 = 4;
const int d6 = 3;
const int d7 = 2;

LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

// Time variables
unsigned long lastTime = 0;
unsigned long currentTime = 0;
unsigned long elapsedTime = 0;

// Initial time (24-hour format)
int hours = 18;
int minutes = 24;
int seconds = 0;

void setup() {
  analogWrite(6,140);
  lcd.begin(16, 2);
  lcd.print("  Digital Clock  ");
}

void loop() {
  currentTime = millis();

  // Update time every second
  if (currentTime - lastTime >= 1000) {
    lastTime = currentTime;
    updateTime();
    displayTime();
  }
}

void updateTime() {
  seconds++;

  if (seconds == 60) {
    seconds = 0;
    minutes++;

    if (minutes == 60) {
      minutes = 0;
      hours++;

      if (hours == 24) {
        hours = 0;
      }
    }
  }
}

void displayTime() {
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Time:");
  // Display hours with leading zero if necessary
  if (hours < 10) {
    lcd.print("0");
  }
  lcd.print(hours);
  lcd.print(":");

  // Display minutes with leading zero if necessary
  if (minutes < 10) {
    lcd.print("0");
  }
  lcd.print(minutes);
  lcd.print(":");

  // Display seconds with leading zero if necessary
  if (seconds < 10) {
    lcd.print("0");
  }
  lcd.print(seconds);

  // Display AM/PM
  if (hours < 12) {
    lcd.print(" AM");
  } else {
    lcd.print(" PM");
  }
}
