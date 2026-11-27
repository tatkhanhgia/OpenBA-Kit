---
name: roadmap
description: "Xếp ưu tiên tính năng, chia đợt Now / Next / Later"
metadata:
  phase: 01-planning
  category: business-analysis
  version: 1.0.0
  is_core: false
---

# /roadmap — Lộ trình phát triển sản phẩm (Now / Next / Later) [STANDARD WORKFLOW]

Xếp ưu tiên tính năng, chia đợt Now / Next / Later

Các đường dẫn `./` và `../` tính từ thư mục chứa tệp SKILL.md này. Đường dẫn `docs/` tính từ dự án đang làm việc.

## Mục tiêu
Cung cấp hướng dẫn chuyên gia BA để thực thi lệnh `/roadmap`, sinh ra tài liệu chất lượng cao, có thể đưa vào sản xuất ngay lập tức mà không cần chỉnh sửa lại format.

## Quy chuẩn bắt buộc tuân thủ (Rules)
- `../prd/references/rules/01-fr-naming-convention.md`

## Biểu mẫu tham chiếu (Template)
- `../prd/references/_templates/02-roadmap.md`

## Vị trí lưu tệp mặc định
- `docs/{product_name}/02-roadmap.md`

## Workflow thực hiện
1. Đọc danh mục tính năng từ PRD hoặc Backlog.
2. Phân rã tính năng theo mô hình 3 làn: Now (Sprint hiện tại / MVP), Next (Sprint tiếp theo), Later (Tương lai/AI).
3. Xác định rõ ngày phát hành dự kiến (Target Release Date) và Definition of Done cho từng milestone.
4. Xuất file theo template `../prd/references/_templates/02-roadmap.md`.

## Tiêu chí Nghiệm thu (Quality Checklist)
- [ ] Sử dụng ngôn ngữ tiếng Việt chuyên nghiệp, đúng thuật ngữ IT BA.
- [ ] Không chứa các từ ngữ mơ hồ định tính (Rule 16).
- [ ] Tuân thủ quy ước đặt mã chuẩn (FR/BR/ERR/UC/US).
- [ ] Lưu đúng vị trí tệp quy định trong dự án.
