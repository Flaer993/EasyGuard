#include <Wire.h>
#include <SPI.h>
#include <Servo.h>
// библиотека для работы с RFID/NFC
#include <Adafruit_PN532.h>
Servo servo;  // Создаем объектServo servo
// пин прерывания
#define PN532_IRQ   9
#define RED 11  // присваиваем имя RED для пина 11
#define GRN 12 // присваиваем имя GRN для пина 12
#define BLU 13
// создаём объект для работы со сканером и передаём ему два параметра
// первый — номер пина прерывания
// вторым — число 100
// от Adafruit был программный сброс шилда
// в cканере RFID/NFC 13,56 МГц (Troyka-модуль) этот пин не используется
// поэтому передаём цифру, большая чем любой пин Arduino
Adafruit_PN532 nfc(PN532_IRQ, 100);

void setup(void)
{
  pinMode(RED, OUTPUT);  // используем Pin11 для вывода
  pinMode(GRN, OUTPUT); // используем Pin12 для вывода
  pinMode(BLU, OUTPUT);  // используем Pin13 для выводаpinMode(RED, OUTPUT);  // используем Pin11 для вывода
  servo.attach(8);   // Указываем объекту класса Servo, что серво присоединен к пину 9
  servo.write(360);
  Serial.begin(9600);
  // инициализация RFID/NFC сканера
  nfc.begin();
  int versiondata = nfc.getFirmwareVersion();
  if (!versiondata) {
    Serial.print("Didn't find RFID/NFC reader");
    digitalWrite(RED, HIGH); // включаем красный свет
    digitalWrite(GRN, LOW);
    digitalWrite(BLU, LOW);
    delay(1000);
    while (1) {
    }
  }

  Serial.println("Found RFID/NFC reader");
  // настраиваем модуль
  nfc.SAMConfig();
  Serial.println("Waiting for a card ...");
}

void loop(void)
{
  uint8_t success;
  // буфер для хранения ID карты
  uint8_t uid[8];
  // размер буфера карты
  uint8_t uidLength;
  // слушаем новые метки
  success = nfc.readPassiveTargetID(PN532_MIFARE_ISO14443A, uid, &uidLength);
  // если найдена карта
  if (success) {
    digitalWrite(RED, LOW);
    digitalWrite(GRN, HIGH); // включаем зеленый свет
    digitalWrite(BLU, LOW);
    delay(1000);
    // выводим в консоль полученные данные
    Serial.println("Found a card");
    Serial.print("ID Length: ");
    Serial.print(uidLength, DEC);
    Serial.println(" bytes");
    Serial.print("ID Value: ");
    nfc.PrintHex(uid, uidLength);
    Serial.println("");

    digitalWrite(RED, LOW);
    digitalWrite(GRN, LOW); // включаем зеленый свет
    digitalWrite(BLU, HIGH);
    servo.write(180); // Поворачиваем серво на 90 градусов
    delay(1000);
    servo.write(0);
    delay(1000);
    servo.write(180);
    delay(1000);
    servo.write(0);
    delay(1000);
    servo.write(180);
    delay(1000);
    servo.write(90);
    delay(5000);
    digitalWrite(RED, LOW);
    digitalWrite(GRN, HIGH); // включаем зеленый свет
    digitalWrite(BLU, LOW);
    delay(1000);

  }
}
