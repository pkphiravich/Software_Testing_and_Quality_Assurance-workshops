Feature: Tutorial สำหรับการทำ behave และ selenium

    Scenario: ตรวจสอบว่าหน้าเว็บที่เข้าไปมี title เหมือนที่คาดไว้ไหม
        Given ฉันเข้าไปที่หน้าเว็บ form ของ selenium
        Then ฉันจะเห็นว่าหน้าเว็บมี heading ที่เขียนว่า web form

    Scenario: สามารถใส่คำลงใน text input แล้วกด submit ได้
        Given ฉันเข้าไปที่หน้าเว็บ form ของ selenium
        When ฉันใส่คำว่า "Hello World" ลงใน text input
        And ฉันกดปุ่ม submit
        Then ฉันควรจะเห็น message ขึ้นว่า "Received!"