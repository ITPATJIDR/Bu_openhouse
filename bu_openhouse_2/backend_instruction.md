รายละเอียดของโค้ด:

การตั้งค่า Flask และฐานข้อมูล:
```python
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
```

อธิบาย คำสั่ง :
- Flask(__name__) สร้างอินสแตนซ์ของแอปพลิเคชัน Flask
- SECRET_KEY ใช้ในการรักษาความปลอดภัยของ session ข้อมูล
- SQLALCHEMY_DATABASE_URI ระบุที่ตั้งของฐานข้อมูล SQLite
- SQLALCHEMY_TRACK_MODIFICATIONS ปิดการติดตามการเปลี่ยนแปลงใน SQLAlchemy เพื่อประหยัดหน่วยความจำ

การสร้างโมเดลของฐานข้อมูล:
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
```
อธิบาย คำสั่ง :
- โมเดล User แทนตัวตารางในฐานข้อมูล SQLite มีฟิลด์ id, username, password, firstname, และ lastname ซึ่งแต่ละฟิลด์มีประเภทข้อมูลและข้อกำหนดที่แตกต่างกัน

เส้นทางสำหรับหน้าแรก (index):
```python
@app.route('/')
def index():
    return redirect(url_for('register'))
```
อธิบาย คำสั่ง :
- เมื่อเข้าไปที่เส้นทาง / จะถูกเปลี่ยนเส้นทางไปยังหน้า register โดยอัตโนมัติ

เส้นทางสำหรับหน้าลงทะเบียน (register):
```python 
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        firstname = request.form['firstname']
        lastname = request.form['lastname']

        if User.query.filter_by(username=username).first():
            return "Username already exists!"

        new_user = User(username=username, password=password, firstname=firstname, lastname=lastname)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')
```

อธิบาย คำสั่ง :
- เมื่อผู้ใช้กรอกฟอร์มลงทะเบียนแล้วส่งข้อมูล (POST) ข้อมูลจะถูกนำมาเก็บในฐานข้อมูล
- หาก username ที่กรอกมามีอยู่แล้วในระบบ จะส่งข้อความแจ้งเตือนว่า Username already exists!
- หาก username ยังไม่ถูกใช้ ข้อมูลของผู้ใช้ใหม่จะถูกบันทึกลงในฐานข้อมูล
- หลังจากการลงทะเบียนสำเร็จ ผู้ใช้จะถูกเปลี่ยนเส้นทางไปยังหน้า login


เส้นทางสำหรับหน้าเข้าสู่ระบบ (login):
```python 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['firstname'] = user.firstname
            session['lastname'] = user.lastname
            return redirect(url_for('congratulation'))

        return "Invalid credentials", 403

    return render_template('login.html')
```
อธิบาย คำสั่ง :
- ผู้ใช้จะต้องกรอก username และ password เพื่อลงชื่อเข้าใช้
- ระบบจะตรวจสอบ username และตรวจสอบรหัสผ่านที่ถูกเก็บในฐานข้อมูล
- หากข้อมูลถูกต้อง ระบบจะสร้าง session สำหรับผู้ใช้ และเปลี่ยนเส้นทางไปยังหน้า congratulation
- หากข้อมูลไม่ถูกต้อง จะแสดงข้อความ Invalid credentials และส่งสถานะ HTTP 403

เส้นทางสำหรับหน้าขอบคุณ (congratulation):
```python
@app.route('/congratulation')
def congratulation():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    firstname = session.get('firstname')
    lastname = session.get('lastname')
    return render_template('congratulation.html', firstname=firstname, lastname=lastname)
```
อธิบาย คำสั่ง :
- หน้า congratulation จะแสดงชื่อของผู้ใช้ที่ลงชื่อเข้าใช้สำเร็จ
- หากผู้ใช้ยังไม่ได้เข้าสู่ระบบ จะถูกเปลี่ยนเส้นทางไปยังหน้า login


การเริ่มต้นแอปพลิเคชัน:
```python 
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
อธิบาย คำสั่ง :
- หากสคริปต์นี้ถูกเรียกใช้โดยตรง แอปพลิเคชันจะสร้างตารางในฐานข้อมูลตามโมเดลที่กำหนดไว้และเริ่มต้นเซิร์ฟเวอร์ Flask