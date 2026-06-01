Feature: การทดสอบแบบ BDD ด้วย behave

	Scenario: ทดสอบว่าหน้า login ของเว็บมี title ถูกหรือไม่
		Given ฉันเข้าไปที่หน้าเว็บหลักของ Swag Lab
		Then ฉันจะเห็นว่าในหน้าเว็บมี title ที่เขียนว่า "swag labs"


	Scenario: ทดสอบว่าสามารถ login เข้าระบบด้วย username และ password ที่ถูกต้องได้หรือไม่
		Given ฉันเข้าไปที่หน้าเว็บหลักของ Swag Lab
		When ฉันใส่ login ว่า "standard_user"
		And ฉันใส่ password ว่า "secret_sauce"
		And ฉันกดปุ่ม Login
		Then ฉันต้องเห็นคำว่า "Products" ขึ้นในหน้าเว็บ


	Scenario: ทดสอบว่าถ้า login เข้าระบบด้วย username และ password ที่ไม่ถูกต้องระบบ
		Given ฉันเข้าไปที่หน้าเว็บหลักของ Swag Lab
		When ฉันใส่ login ว่า "abcde"
		And ฉันใส่ password ว่า "abcde"
		And ฉันกดปุ่ม Login
		Then ระบบต้องแจ้งเตือนมาว่า "Username and password do not match any user in this service"


	Scenario: ทดสอบว่าเมื่อเพิ่มของ 1 สิ่งลงในตระกร้า, icon ตะกร้า (badge) จะมีเลข 1 ขึ้นมา
		Given ฉันเข้าไปที่หน้าเว็บหลักของ Swag Lab
		When ฉันใส่ login ว่า "standard_user"
		And ฉันใส่ password ว่า "secret_sauce"
		And ฉันกดปุ่ม Login
		And ฉันกดปุ่ม ADD TO CART สักปุ่มบนหน้าจอ
		Then icon รูปบนตะกร้าต้องมีเลข 1 ขึ้นมา

	Scenario: ทดสอบว่าในหน้า checkout ระบบสามารถคํานวณราคาสินค้าในตะกร้าในส่วนของ Price Total ที่เขียนว่า “Item total” ได้ถูกต้อง (ใส่สินค้าอย่างน้อย 3 ชนิด)
		Given ฉันเข้าไปที่หน้าเว็บหลักของ Swag Lab
		When ฉันใส่ login ว่า "standard_user"
		And ฉันใส่ password ว่า "secret_sauce"
		And ฉันกดปุ่ม Login
		And ฉันกดปุ่ม ADD TO CART ของสินค้า Sauce Labs Backpack
		And ฉันกดปุ่ม ADD TO CART ของสินค้า Sauce Labs Bike Light
		And ฉันกดปุ่ม ADD TO CART ของสินค้า Sauce Labs Bolt T-Shirt
		Then icon รูปบนตะกร้าต้องมีเลข 3 ขึ้นมา	
		And ฉันกดปุ่ม icon รูปตะกร้า
		And ฉันกดปุ่ม checkout
		And ฉันกรอก first name ว่า "pk"
		And ฉันกรอก last name ว่า "pp"
		And ฉันกรอก postal code ว่า "1234"
		And ฉันกดปุ่ม continue
		Then ฉันเห็น "Item total: $55.97" ขึ้นในหน้าเว็บ

