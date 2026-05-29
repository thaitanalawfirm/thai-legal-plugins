# ปลั๊กอินงานกฎหมายไทย (Thai Legal Plugins)

ชุดปลั๊กอินสำหรับสำนักงานทนายความไทย ใช้ใน Cowork / Claude Code — ครอบคลุมงานตั้งแต่รับเรื่อง ตรวจ conflict ร่างคำคู่ความ บริหารสำนวน ให้ความเห็นทางกฎหมาย ตรวจ compliance ไปจนถึงงานทรัพย์สินทางปัญญา

## ✨ สิ่งที่ได้

- **คลังตัวบทกฎหมาย** 45 ไฟล์ (ประมวลกฎหมาย พ.ร.บ. กฎหมายลำดับรอง ฎีกาบรรทัดฐาน)
- **คลังแบบพิมพ์ศาล** 192 ฟอร์ม (ศาลยุติธรรม คดีผู้บริโภค แรงงาน ปกครอง ภาษี ล้มละลาย ฯลฯ)
- **ปลั๊กอินงาน 14 ตัว** ครอบคลุมขั้นตอนตั้งแต่รับเรื่องไปจนถึงปิดคดี

## 📋 รายการปลั๊กอิน

### คลัง (Library)
| ปลั๊กอิน | ขนาด | บทบาท |
|---|---:|---|
| `thai-legal-library` ⭐ | 1.4 MB | คลังตัวบทกฎหมาย — **ต้องลงก่อนเสมอ** |
| `thai-legal-forms` | 116 MB | คลังแบบฟอร์มศาล — ลงเมื่อต้องใช้แบบฟอร์ม (ดาวน์โหลดจาก Releases) |

### Litigation (คดีความ)
| ปลั๊กอิน | บทบาท |
|---|---|
| `thai-litigation-pleadings` | ร่างคำฟ้อง/คำให้การ |
| `thai-litigation-motions` | ร่างคำร้อง/อุทธรณ์/ฎีกา |
| `thai-litigation-caseprep` | เตรียมคดี รวบรวมพยานหลักฐาน |
| `thai-litigation-deadlines` | คำนวณกำหนดเวลาทางคดี |

### Case Management (บริหารคดี)
| ปลั๊กอิน | บทบาท |
|---|---|
| `thai-client-intake` | รับเรื่อง |
| `thai-conflict-check` | ตรวจ conflict of interest |
| `thai-engagement-fees` | สัญญาว่าจ้างและค่าวิชาชีพ |
| `thai-matter-management` | บริหารสำนวน |

### Advisory (ที่ปรึกษา)
| ปลั๊กอิน | บทบาท |
|---|---|
| `thai-legal-opinion` | ความเห็นทางกฎหมาย |
| `thai-legal-due-diligence` | Legal Due Diligence |
| `thai-compliance-audit` | ตรวจสอบ compliance |

### Corporate & IP
| ปลั๊กอิน | บทบาท |
|---|---|
| `thai-corporate-secretarial` | งานเลขานุการบริษัท |
| `thai-patent` | สิทธิบัตร |
| `thai-trademark` | เครื่องหมายการค้า |

## 🚀 วิธีติดตั้ง

### วิธีที่ 1: ติดตั้งทั้ง marketplace (แนะนำ)

ใน Cowork พิมพ์คำสั่ง:

```
/plugin marketplace add your-github-username/thai-legal-plugins
```

จากนั้นเรียกดูปลั๊กอินที่มีและเลือกลง:

```
/plugin install thai-legal-library@thai-legal-plugins
/plugin install thai-litigation-pleadings@thai-legal-plugins
```

หรือลงทุกตัวเลย:

```
/plugin install --all@thai-legal-plugins
```

### วิธีที่ 2: ติดตั้งแบบฟอร์มศาล (แยกต่างหาก)

แบบฟอร์มศาล (116 MB) เกินขีดจำกัด GitHub marketplace จึงอยู่ใน Releases:

1. ไปที่ https://github.com/your-github-username/thai-legal-plugins/releases/latest
2. ดาวน์โหลดไฟล์ `thai-legal-forms.skill`
3. ลาก/วางในแชท Cowork → กด "Save skill"

## 📐 ลำดับติดตั้งแนะนำ

```
1. thai-legal-library              ← ลงก่อนเสมอ
2. thai-legal-forms                ← ลงเมื่อต้องใช้แบบฟอร์ม
3. ปลั๊กอินงานที่ใช้เป็นประจำ
```

## 🔄 การอัปเดต

```
/plugin update --all@thai-legal-plugins
```

หรืออัปเดตเฉพาะตัว:

```
/plugin update thai-legal-library@thai-legal-plugins
```

## ⚖️ ข้อสำคัญในการใช้

1. **ตัวบทกฎหมายในคลัง** เป็นสำเนาเพื่อค้นอ้างอิง — **ก่อนใช้จริงต้องตรวจกับฉบับปัจจุบันที่** http://www.krisdika.go.th
2. **เลขฎีกาในคลัง** ต้องตรวจกับ "สืบค้นฎีกา 2015" ของศาลฎีกาก่อนอ้างในคำคู่ความ — โดยเฉพาะปี 2566+
3. **แบบฟอร์มศาล** ต้องตรวจกับเว็บไซต์ศาลก่อนยื่นจริงทุกครั้ง — เวอร์ชันในปลั๊กอินอาจตามไม่ทัน
4. **ผลงานทุกชิ้นจากปลั๊กอินเป็นเพียง "ร่างให้ทนายผู้รับผิดชอบตรวจ"** — ห้ามใช้งานโดยไม่ผ่านการตรวจจากทนาย

## 📝 License & ผู้ดูแล

- ภายในสำนักงาน (private repo)
- ผู้ดูแล: [ชื่อผู้ดูแล]
- ติดต่อ: [อีเมล]

## 📜 Changelog

### v1.0.0 — 29 พ.ค. 2569
- เปิดตัวปลั๊กอินครั้งแรก 16 ตัว
- คลังตัวบทกฎหมาย 45 ไฟล์ใน 6 หมวด
- คลังแบบฟอร์มศาล 192 ฟอร์มใน 15 กลุ่ม
