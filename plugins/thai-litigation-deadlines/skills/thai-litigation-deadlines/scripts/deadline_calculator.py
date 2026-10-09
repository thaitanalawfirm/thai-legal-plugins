#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
deadline_calculator.py — เครื่องช่วยคำนวณวันครบกำหนดสำหรับคดีตามกฎหมายไทย

สคริปต์นี้เป็น "ตัวช่วย" ไม่ใช่ "ข้อยุติทางกฎหมาย"
ทนายผู้รับผิดชอบต้องตรวจสอบยืนยันผลกับตัวบทกฎหมายและปฏิทินวันหยุดของศาลเสมอ

หลักการที่ใช้ (อ้างอิงตาม ป.พ.พ. ว่าด้วยระยะเวลา — ให้ยืนยันกับตัวบทฉบับปัจจุบัน):
- ระยะเวลาเป็น "วัน": ไม่นับวันแรก เริ่มนับวันรุ่งขึ้นเป็นวันที่หนึ่ง
  => วันครบกำหนด = วันเริ่มต้น + จำนวนวัน
- ระยะเวลาเป็น "เดือน/ปี": คำนวณตามปฏิทิน โดยสคริปต์ใช้วิธีบวกเดือน/ปีจากวันเริ่มต้น
  ไปยังวันที่ตรงกัน  *** การนับเดือน/ปีมีรายละเอียดและข้อยกเว้น ผลที่ได้เป็นค่าประมาณ
  ต้องให้ทนายตรวจสอบ ***
- ถ้าวันครบกำหนดตรงกับเสาร์/อาทิตย์ จะถูกแจ้งเตือน แต่สคริปต์ไม่ทราบวันหยุดราชการเฉพาะ
  ของแต่ละปี จึงต้องตรวจสอบปฏิทินวันหยุดของศาลด้วยตนเอง

วิธีใช้ (command line):
    python deadline_calculator.py 2567-03-10 1 month
    python deadline_calculator.py 2024-03-05 15 day
รูปแบบวันที่: ปี-เดือน-วัน  (ปีรับได้ทั้ง พ.ศ. และ ค.ศ. — ดูฟังก์ชัน parse_date)
"""

import sys
import datetime


THAI_DOW = ["จันทร์", "อังคาร", "พุธ", "พฤหัสบดี", "ศุกร์", "เสาร์", "อาทิตย์"]


def parse_date(text):
    """แปลงข้อความวันที่เป็น datetime.date รองรับปี พ.ศ. และ ค.ศ.
    ถือว่าปีที่มากกว่า 2400 เป็น พ.ศ. และแปลงเป็น ค.ศ. โดยลบ 543"""
    parts = text.strip().replace("/", "-").split("-")
    if len(parts) != 3:
        raise ValueError("รูปแบบวันที่ต้องเป็น ปี-เดือน-วัน เช่น 2567-03-10")
    year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
    is_buddhist = year > 2400
    if is_buddhist:
        year -= 543
    return datetime.date(year, month, day), is_buddhist


def format_date(d, as_buddhist):
    """จัดรูปแบบวันที่เป็นข้อความ พร้อมชื่อวันในสัปดาห์"""
    year = d.year + 543 if as_buddhist else d.year
    dow = THAI_DOW[d.weekday()]
    era = "พ.ศ." if as_buddhist else "ค.ศ."
    return f"วัน{dow}ที่ {d.day}/{d.month}/{year} ({era})"


def add_months(d, months):
    """บวกจำนวนเดือนให้กับวันที่ จัดการกรณีเดือนปลายทางมีจำนวนวันไม่ถึง"""
    total = d.month - 1 + months
    new_year = d.year + total // 12
    new_month = total % 12 + 1
    # หาวันสุดท้ายของเดือนปลายทาง เพื่อกันกรณีเช่น 31 ม.ค. + 1 เดือน
    if new_month == 12:
        last_day = 31
    else:
        last_day = (datetime.date(new_year, new_month + 1, 1)
                    - datetime.timedelta(days=1)).day
    return datetime.date(new_year, new_month, min(d.day, last_day))


def calculate_deadline(start_date, amount, unit):
    """คำนวณวันครบกำหนด คืนค่า (วันครบกำหนด, คำอธิบายวิธีคำนวณ)"""
    unit = unit.lower()
    if unit in ("day", "days", "วัน"):
        # ไม่นับวันแรก => วันครบกำหนด = วันเริ่มต้น + จำนวนวัน
        end = start_date + datetime.timedelta(days=amount)
        note = (f"ระยะเวลาเป็นวัน: ไม่นับวันแรก เริ่มนับวันรุ่งขึ้นเป็นวันที่หนึ่ง "
                f"=> วันครบกำหนด = วันเริ่มต้น + {amount} วัน")
    elif unit in ("month", "months", "เดือน"):
        end = add_months(start_date, amount)
        note = (f"ระยะเวลาเป็นเดือน: บวก {amount} เดือนจากวันเริ่มต้นไปยังวันที่ตรงกัน "
                f"(เป็นค่าประมาณ การนับเดือนมีรายละเอียดตามกฎหมาย ต้องให้ทนายตรวจสอบ)")
    elif unit in ("year", "years", "ปี"):
        end = add_months(start_date, amount * 12)
        note = (f"ระยะเวลาเป็นปี: บวก {amount} ปีจากวันเริ่มต้นไปยังวันที่ตรงกัน "
                f"(เป็นค่าประมาณ ต้องให้ทนายตรวจสอบ)")
    else:
        raise ValueError("หน่วยต้องเป็น day/month/year หรือ วัน/เดือน/ปี")
    return end, note


def main(argv):
    if len(argv) != 4:
        print(__doc__)
        print("ตัวอย่าง: python deadline_calculator.py 2567-03-10 1 month")
        return 1

    try:
        start_date, is_buddhist = parse_date(argv[1])
        amount = int(argv[2])
        unit = argv[3]
        end_date, note = calculate_deadline(start_date, amount, unit)
    except (ValueError, IndexError) as e:
        print(f"ข้อผิดพลาด: {e}")
        return 1

    today = datetime.date.today()
    days_left = (end_date - today).days

    print("=" * 60)
    print("ผลการคำนวณวันครบกำหนด (ตัวช่วย — ต้องให้ทนายตรวจสอบยืนยัน)")
    print("=" * 60)
    print(f"วันเริ่มต้น (จุดเริ่มนับ) : {format_date(start_date, is_buddhist)}")
    print(f"ระยะเวลา                : {amount} {unit}")
    print(f"วิธีคำนวณ               : {note}")
    print(f"วันครบกำหนด (ประมาณ)    : {format_date(end_date, is_buddhist)}")

    # แจ้งเตือนวันหยุดสุดสัปดาห์
    if end_date.weekday() >= 5:
        print()
        print("⚠️  วันครบกำหนดตรงกับวันเสาร์/อาทิตย์ — โดยหลักเลื่อนเป็นวันทำการถัดไปได้")
    print("⚠️  สคริปต์ไม่ทราบวันหยุดราชการเฉพาะ — ต้องตรวจสอบปฏิทินวันหยุดของศาลเสมอ")

    # สรุปจำนวนวันคงเหลือเทียบกับวันนี้
    print()
    if days_left < 0:
        print(f"🔴  เลยวันครบกำหนดมาแล้วประมาณ {abs(days_left)} วัน — ตรวจสอบด่วน")
    elif days_left == 0:
        print("🔴  วันนี้เป็นวันครบกำหนด")
    elif days_left <= 7:
        print(f"🔴  เหลือเวลาประมาณ {days_left} วัน — เร่งดำเนินการ")
    elif days_left <= 30:
        print(f"🟡  เหลือเวลาประมาณ {days_left} วัน")
    else:
        print(f"🟢  เหลือเวลาประมาณ {days_left} วัน")

    print()
    print("หมายเหตุ: ผลนี้เป็นตัวช่วยคำนวณเบื้องต้น มิใช่ข้อยุติทางกฎหมาย")
    print("ทนายผู้รับผิดชอบต้องยืนยันจุดเริ่มนับ ตัวบทกฎหมาย และปฏิทินวันหยุดของศาล")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
