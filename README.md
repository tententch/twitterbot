# บอทคิดคำคมบนทวิตเตอร์
AI คิด content สำหรับทวิตเตอร์ด้วย RNN
![alt text](https://docs.google.com/uc?id=18immzSiLKzugpQEtAnkCvoIuDZGwQ-qa)


ระบบถูกเทรนด์ด้วยข้อความติดเทรนด์บนทวิตเตอร์ทั้งหมด 7000 ทวิต
ซึ่งในช่วงที่ผมทำ เป็นช่วงที่หนัง"ฮาวทูทิ้ง ทิ้งอย่างไรไม่ให้เหลือเธอ"กำลังติดเทรนด์
ข้อความส่วนใหญ่เลยน่าสนใจเพราะเป็นทวิตเกี่ยวกับความรักเป็นหลัก น่าจะเหมาะกับเอามาเทรนด์คำคมใหม่ๆ

# Prepare Data Set
ในไฟล์ howtoting.xlsx คือไฟล์ข้อมูลดิบที่ยังไม่ได้ผ่านการคลีน จะสังเกตได้ว่า มีทั้งโฆษณา อีโมจิคอน และอื่นๆอีกมากมายที่่เอามาใช้งานก็คงไม่ดี
เลยต้องมีการคลีนดาต้าก่อนในไฟล์ Thai.py

ในนั้นมีระบบดังนี้
-การลบอิโมจิและตัวอักษณพิเศษ
-การแบ่งคำด้วย pythainlp(ขอบคุณที่ทำ Open Souce ดีๆแบบนี้ออกมานะครับ ได้ประโยชน์มากเลย)
  สาเหตุที่ต้องแบ่งคำคือ Module ที่เราได้ใช้การเทรนด์ดาต้าคือ Textgenrnn ซึ่งเป็นโมดูลที่ใช้กับภาษาอังกฤษมาก่อน ซึ่งการเขาจะใช้การเว้นวรรคแทนคำหนึ่งคำ
  เช่น I Love You ก็สามารถบอกได้เลยว่ามี I และ Love และ You อยู่บนหน้าจอ (ไอ่สัด อย่างง่าย)
  แต่ปัญหาของภาษาไทยคือ เวลาพิมพ์ประโยค คำมันจะติดกันแบบที่ผมกำลังพิมพ์อยู่
  คอมพิวเตอร์มันไม่รู้ว่าตัวอักษรไหนถึงไหนถึงจะเป็น 1 คำ และไอ่ pythainlp เนี่ย ช่วยเว้นวรรคคำให้ ซึ่งถือว่าความแม่นยำดีระดับนึงเลย
 -ต้องพยายามเลี่ยงคำที่ไม่ควรมี เช่น เ-็ด, -ี, ค-ย, นายก(เดี๋ยวแม่งสร้างประโยคเสี่ยงๆมา) ก็คลีนคำพวกนี้ไปซะ
 
 เมื่อเข้าใจแล้ว ก็รันไฟล์ Thai.py ได้เลย 
 ผลลัพธ์ที่ได้ จะเป็นไฟล์ text ชื่อว่า test.txt ซึ่งจะเป็น String ที่คลีนมาเรียบร้อยแล้ว เหมาะสำหรับการเอาไปเทรนด์
 
 # Trainning Data
 ไม่ต้องอธิบายอะไรมากมาย เอาเป็นว่ารันฟังก์ชั่น train() ที่อยู่ในไฟล์ model.py เพื่อสร้าง weigh ขึ้นมา
 ซึ่งผม config ให้มันเหมาะสำหรับภาษาไทยแล้ว คือเทรนด์เป็นคำ ไม่ใช่ตัวอักษณ(ซึ่งห่วยมาก) Epoch ซัก 20 ก็รู้เรื่องละ
 
 # Testing Data
 เมื่อเราได้โมเดลมาแล้ว (ไฟล์ textgenrnn_weights.hdf5) ก็ลองทดสอบดูด้วยฟังก์ชั่น model_() ในไฟล์ model.py
 ระบบจะ return ค่าออกมาเป็น array ประโยคนึงที่เว้นวรรค เช่น ['คน เรา มี ค่า เสียสละ'] อะไรประมาณนี้ ซึ่งความแปลกใหม่ของประโยคจะถูกกำหนดด้วย Temparature
 ยิ่งค่าใกล้เข้า 1.0 คือจะยิ่งแปลกใหม่ ผมเลยตั้งให้ทุกครั้งที่มันคิดประโยค มันจะสุ่มจำนวณคำ สุ่มค่า Temparature เป็น 0.8 และ 1.0
 
 ถือว่าจบด้านโมเดลสำหรับคิดคำคมใหม่ๆขึ้นมา
 
 # ตกแต่งหน่อย
 คือ output ที่เราได้มันจะเป็นอเรย์ที่มีเว้นวรรคด้วย
 ซึ่งเราก็เขียนโค้ดให้เอาข้อความอเรย์ออกมาง่ายๆ และลบ spacebar ไปเพื่อความเนียนของข้อความ
 ทั้งหมดจะทำอยู่ในไฟล์ tweet.py แล้วครับ
 
 # ให้ AI ของเราอัพคำคมลงทวิตเตอร์
 คือไหนๆก็คิดคำคมมาแล้ว ต้องโชว์ศักยภาพหน่อย ก็ใช้โมดูล tweepy ซึ่งสามารถ install ได้จาก command line เลย
 แต่ต้องมี developer account ของ twitter ด้วยนะ ก็ไปสร้างกันมา ส่งอีเมลล์ไปบอกเขาก็ได้ว่าตั้งใจจะทำอะไร(ภาษาอังกฤษนะ)
 จากนั้นไปสร้างพวก Customer Key และอื่นๆ เพื่อเอามาใส่ในฟังก์ชั่น main ของ tweet.py ที่ผมทำเอาไว้
 
 
 หมายถึงบรรทัดนี้
 
 auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
 auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")


 
 
 แล้วก็ตั้งคำพูดเพิ่มเติมแล้วก็พวก Hashtag ได้ตามใจชอบ 
 ขี้เกียจอธิบายการทำงาน คือระบบที่ออกแบบมาผมให้มันทวิตคำคมใหม่ๆทุกๆ 1 ชม. ด้วยการสุ่ม Hashtag จากคำที่มันคิดได้
 เอาเป็นว่าลองแกะๆโค้ดแล้วปรับปรุงเองละกัน
 
 # Quick start
 ด้านบนที่อธิบายมา คือระบบที่เล่นได้ทั้งหมด
 แต่ถ้าใครไม่คิดอะไรมาก แค่อยากเล่นเล่นๆเฉยๆ
 แนะนำ 2 อย่าง
 อย่างแรก ลง Env ให้ครบตามนี้ 
 
 ========================
 tweepy
 
 
 textgenrnn
 
 
 keras
 
 
 h5py
 
 
 scikit-learn
 
 
 tqdm
 
 
 tensorflow
 
 ========================
 
 จากนั้นก็แก้ไขพวก Key ต่างๆที่ได้จาก Developer Account ของทวิตเตอร์ซะ
 แล้วรัน tweet.py
 ก็เห็นผลละ
 
 
