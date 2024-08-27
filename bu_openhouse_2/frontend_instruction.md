# Front-end instruction

Tailwind CSS Documentation : https://tailwindcss.com/docs/installation
<br>Giphy : https://giphy.com/

### 1. Register Button and Login Button

- <strong>Objective</strong> : สไตล์ปุ่มสำหรับการลงทะเบียนหรือเข้าสู่ระบบ
- <strong>Details</strong> : เราจะใช้ปุ่มที่มีชุดคลาส Tailwind CSS เฉพาะเพื่อให้ได้ดีไซน์ที่ทันสมัยและตอบสนองได้ดี ปุ่มจะมีพื้นหลังสีเข้ม (bg-slate-600), เปลี่ยนสีเมื่อเลื่อนเมาส์ไปที่ปุ่ม (hover
  ) และจะมีเอฟเฟกต์การขยายขนาดที่ราบรื่นเมื่อถูกเลือก (focus
  ) ซึ่งจะช่วยเพิ่มความสวยงามและประสบการณ์การใช้งานที่ดีขึ้นแก่ผู้ใช้

- bg-[#000000]

Implementation:

```HTML
<button type="submit" class="w-full p-3 rounded-lg my-8 bg-slate-600 hover:bg-slate-700 text-white focus:scale-95 transition-all">Button</button>
```

&nbsp;

### 2. Border Radius and border color

- <strong>Objective</strong> : เพิ่มสไตล์ให้กับคอนเทนเนอร์ที่มีขอบโค้งมนและสีขอบเฉพาะ

- <strong>Details</strong> : เราจะออกแบบคอนเทนเนอร์ด้วย Tailwind CSS ที่มีขอบโค้งมนและสีขอบเฉพาะ เพื่อให้คอนเทนเนอร์มีโครงสร้างที่ชัดเจนและน่าดึงดูด

- <img src="img/Screenshot 2024-08-25 214721.png"
            alt="img">

Implementation:

```HTML
class="p-10 rounded-xl border-2 border-blue-500"
```

&nbsp;

### 3. Popup message

- <strong>Objective</strong> : สร้างป๊อปอัปเพื่อยืนยันการกระทำของผู้ใช้ก่อนดำเนินการต่อ
- <strong>Details</strong> : เราจะพัฒนาป๊อปอัปโดยใช้ Tailwind CSS ซึ่งจะแสดงขึ้นเมื่อผู้ใช้พยายามส่งฟอร์ม ป๊อปอัปนี้จะถามผู้ใช้เพื่อยืนยันการลงทะเบียนก่อนที่จะส่งฟอร์มจริง ๆ โดยป๊อปอัปจะถูกซ่อนอยู่โดยค่าเริ่มต้นและจะแสดงขึ้นเมื่อถูกเรียกใช้โดยฟังก์ชัน JavaScript

- <img src="img/Screenshot 2024-08-25 220939.png"
            alt="img">

Implementation:

```HTML
<div id="confirmation-modal" class="hidden fixed inset-0 bg-gray-800 bg-opacity-50 flex items-center justify-center z-50">
        <div class="bg-white p-6 rounded-lg text-center">
            <h3 class="text-xl font-semibold mb-4">Confirm the Registration</h3>
            <p class="mb-6">Are you sure you want to register?</p>
            <div class="flex justify-around">
                <button class="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600" onclick="submitForm()">Yes</button>
                <button class="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600" onclick="closeModal()">No</button>
            </div>
        </div>
    </div>
```

```js
<script>
        function showModal(event) {
            event.preventDefault(); // Prevent form submission
            document.getElementById('confirmation-modal').classList.remove('hidden');
        }

        function closeModal() {
            document.getElementById('confirmation-modal').classList.add('hidden');
        }

        function submitForm() {
            document.getElementById('register-form').submit();
        }
    </script>
```

&nbsp;

### 4. Let's Build Congtratulation Page

- <strong>Objective</strong> : สร้างหน้าที่แสดงความยินดีหลังจากการลงทะเบียนหรือเข้าสู่ระบบสำเร็จ
- <strong>Details</strong> : หน้านี้จะแสดงข้อความแสดงความยินดีพร้อมกับ GIF เคลื่อนไหวเพื่อเฉลิมฉลองความสำเร็จของการเข้าสู่ระบบหรือการลงทะเบียนของผู้ใช้ จะมีข้อความส่วนตัวที่ระบุชื่อจริงและนามสกุลของผู้ใช้เพื่อสร้างประสบการณ์ที่อบอุ่นและน่าสนใจ หน้านี้ใช้ Tailwind CSS ในการจัดวางและตกแต่ง พร้อมกับการเพิ่มอนิเมชั่นเด้งสนุก ๆ ในข้อความ "Congratulations!"

- <img src="img/Screenshot 2024-08-25 223747.png"
            alt="img">

Implementation:

```HTML
<div
      class="flex flex-col justify-center items-center gap-5 bg-white p-8 px-20 rounded-lg transition-all"
    >
        <h2 class="font-bold text-[20px] animate-bounce">Congratulations!</h2>
        <!-- gif here -->
        <img
          src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2o2aW02N3JpdTR2N3Nxb211M2pkcXU5cHJuYndwNnV2Nms0b29jbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/BPJmthQ3YRwD6QqcVD/giphy.gif"
          alt="gif"
          class="py-4"
        />
        <p class="font-normal text-[16px]">
          {{ firstname }} {{ lastname }}, you have successfully logged in!
        </p>
  </div>
```

### 5. (optional) Let's add animation

Implementation:

```js
<script>
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("show");
      }
    });
  });

  const hiddenElements = document.querySelectorAll(".animate-class");
  hiddenElements.forEach((el) => observer.observe(el));
</script>
```

```CSS
.animate-class {
    opacity: 0;
    scale: 0.9;
    transition: all 0.5s ease;
    transition-delay: 200ms;
    transform: translateY(50px);
    -webkit-transition: all 0.5s ease;
    -moz-transition: all 0.5s ease;
    -ms-transition: all 0.5s ease;
    -o-transition: all 0.5s ease;
  }

  .show {
    opacity: 1;
    scale: 1;
    transform: translateY(0);
  }

  .text1:nth-child(1) {
    transition-delay: 200ms;
  }
  .text1:nth-child(2) {
    transition-delay: 300ms;
  }
  .text1:nth-child(3) {
    transition-delay: 400ms;
  }
```
